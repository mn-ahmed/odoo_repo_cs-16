# -*- coding: utf-8 -*-
from crypt import methods
from typing import final
from odoo import http
from odoo.http import request
import xlrd
from datetime import datetime
from odoo.exceptions import UserError
import os
import json
import io


class AiplGst(http.Controller):
    def import_excel():
        try:
            book = xlrd.open_workbook(
                filename="community/AIPL-Odoo/aipl_gst/uploads/data.xls",
                encoding_override="utf-8",
            )
        except FileNotFoundError:
            raise Exception("No such file or directory found")
        except xlrd.biffh.XLRDError:
            raise Exception("Only excel files are supported.")

        try:
            for sheet in book.sheets():
                if sheet.name == "Purchase Reigster":
                    h1, h2 = [], []
                    for row in range(sheet.nrows):
                        if row == 0:
                            h1.append(sheet.row_values(row))
                        if row == 1:
                            h2.append(sheet.row_values(row))
                    # print(h2[0][4])
                    records = dict()
                    if h1[0][0].startswith("GSTIN"):
                        records["gstin"] = h1[0][1]
                        records["financial_year"] = h1[0][3]
                        records["org_name"] = h2[0][1]
                        records["tax_period"] = h2[0][3]
                    elif h1[0][1].startswith("GSTIN"):
                        records["gstin"] = h1[0][2]
                        records["financial_year"] = h1[0][4]
                        records["org_name"] = h2[0][2]
                        records["tax_period"] = h2[0][4]
                    elif h1[0][2].startswith("GSTIN"):
                        records["gstin"] = h1[0][3]
                        records["financial_year"] = h1[0][7]
                        records["org_name"] = h2[0][5]

                    start_at = 0
                    for row in range(sheet.nrows):
                        line = sheet.row_values(row)
                        if line[0].startswith("GSTIN"):
                            start_at = row

                    final_list = list()
                    for row in range(start_at + 1, sheet.nrows):
                        # print("A"*100)
                        # print(sheet.row_values(row))
                        sheet_list = sheet.row_values(row)
                        records["gstin_supplier"] = sheet_list[0]
                        records["supplier_name"] = sheet_list[1]
                        records["a"] = sheet_list[2]
                        records["document_type"] = sheet_list[3]
                        records["document_number"] = sheet_list[4]
                        # records['document_date'] = sheet_list[5]
                        records["document_date"] = datetime(
                            *xlrd.xldate_as_tuple(sheet_list[5], 0)
                        )
                        records["taxable_value"] = sheet_list[6]
                        records["integrated_tax"] = sheet_list[7]
                        records["central_tax"] = sheet_list[8]
                        records["state_tax"] = sheet_list[9]
                        records["cess"] = sheet_list[10]

                        final_list.append(records.copy())
            print(final_list)
            request.env["aipl.purchase.register"].create(final_list)
        except Exception as e:
            print(e)

    # @http.route('/aipl_gst/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    @http.route("/aipl/purchaseRegistry", auth="public", website=True)
    def aipl_gst(self, **kw):
        return http.request.render("aipl_gst.upload_xml")

    @http.route(
        "/aipl/excel", auth="public", methods=["post"], website=True, csrf=False
    )
    def aipl_gst_upload(self, **kw):
        if kw.get("file_excel", False):
            file = kw.get("file_excel")
            fl = file.read()
            # fn = os.path.basename(file.filename)
            with open("community/AIPL-Odoo/aipl_gst/uploads/data.xls", "wb") as file:
                file.write(fl)
            AiplGst.import_excel()

    @http.route("/aipl/testing", auth="public", website=True)
    def test(self, **kw):
        return http.request.render("aipl_gst.testing")

    @http.route("/aipl_gst/", auth="public")
    def index(self, **kw):
        return http.request.render("aipl_gst.form1")

    @http.route(
        "/aipl_purchase/form1_response",
        methods=["post"],
        type="http",
        auth="public",
        csrf=False,
    )
    def form1_response(self, **kw):
        # data = json.loads(http.request.form.get('data'))
        # file = http.request.files['file']
        if kw.get("json_file", False):
            # name = kw.get('json_file').filename
            file = kw.get("json_file")
            fl = file.read()
            formatted_fl = fl.replace(b"'", b'"')
            fl_json = json.load(io.BytesIO(formatted_fl))
            fp = fl_json["data"]["rtnprd"]
            dt = request.env["aipl.gst.b2b"].search_count([("fp", "=", fp)])
            if dt > 1:
                raise UserError("Data Already Exists.")
            json_uploader(fl_json).json_to_model()


class json_uploader:
    def __init__(self, fl):
        self.raw_json = fl

    def json_to_model(self):
        raw_data = self.raw_json
        raw_data = raw_data["data"]
        raw_data_list = list()

        b2b = raw_data["docdata"]["b2b"]
        for level1 in b2b:
            for z in level1["inv"]:
                items = z["items"]

                supfildt = datetime.strptime(level1["supfildt"], "%d-%m-%Y").strftime(
                    "%Y-%m-%d"
                )
                dt = datetime.strptime(z["dt"], "%d-%m-%Y").strftime("%Y-%m-%d")

                final_dict = dict()
                final_dict.update(
                    {
                        "gstin": raw_data["gstin"],
                        "fp": raw_data["rtnprd"],
                        "trdnm": level1["trdnm"],
                        "supfildt": supfildt,
                        "ctin": level1["ctin"],
                        "dt": dt,
                        "val": z["val"],
                        "rev": z["rev"],
                        "itcavl": z["itcavl"],
                        "diffprcnt": z["diffprcnt"],
                        "pos": z["pos"],
                        "typ": z["typ"],
                        "inum": z["inum"],
                        "rsn": z["rsn"],
                        "rt": items[0]["rt"],
                        "num": items[0]["num"],
                        "txval": items[0]["txval"],
                        "cess": items[0].get("cess", 0),
                        "igst": items[0].get("igst", 0),
                        "cgst": items[0].get("cgst", 0),
                        "sgst": items[0].get("sgst", 0),
                    }
                )
                raw_data_list.append(final_dict.copy())
                del final_dict
        request.env["aipl.gst.b2b"].create(raw_data_list)

        cdnr = raw_data["docdata"]["cdnr"]
        raw_data_list = list()
        for level1 in cdnr:
            for z in level1["nt"]:
                items = z["items"]
                supfildt = datetime.strptime(level1["supfildt"], "%d-%m-%Y").strftime(
                    "%Y-%m-%d"
                )
                dt = datetime.strptime(z["dt"], "%d-%m-%Y").strftime("%Y-%m-%d")
                final_dict = dict()
                final_dict["gstin"] = raw_data["gstin"]
                final_dict["fp"] = raw_data["rtnprd"]
                final_dict["trdnm"] = level1["trdnm"]
                final_dict["supfildt"] = supfildt
                final_dict["supprd"] = level1["supprd"]
                final_dict["ctin"] = level1["ctin"]
                final_dict["dt"] = dt
                final_dict["val"] = z["val"]
                final_dict["rev"] = z.get("rev", "")
                final_dict["itcavl"] = z["itcavl"]
                final_dict["diffprcnt"] = z["diffprcnt"]
                final_dict["pos"] = z.get("pos", "")
                final_dict["typ"] = z["typ"]
                final_dict["suptyp"] = z.get("suptyp", "")
                final_dict["ntnum"] = z["ntnum"]
                final_dict["rsn"] = z["rsn"]
                final_dict["rt"] = items[0]["rt"]
                final_dict["num"] = items[0]["num"]
                final_dict["txval"] = items[0]["txval"]
                final_dict["cess"] = items[0].get("cess", 0)
                final_dict["igst"] = items[0].get("igst", 0)
                final_dict["cgst"] = items[0].get("cgst", 0)
                final_dict["sgst"] = items[0].get("sgst", 0)
                raw_data_list.append(final_dict.copy())
        request.env["aipl.gst.cdnr"].create(raw_data_list)
