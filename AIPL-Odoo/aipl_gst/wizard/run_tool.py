# -*- coding: utf-8 -*-

from odoo import models, fields, api


class run_tool(models.TransientModel):
    _name = "aipl.runtool.wizard"
    _description = "run_tool.wizard"

    date = fields.Date(string="Date")

    def run_tool(self):
        print(self)
        fetch_data = self.env.cr.execute(
            """select * from aipl_gst_b2b b2b inner join aipl_purchase_register pr on b2b.gstin=pr.gstin
                            where b2b.ctin = pr.gstin_supplier and b2b.txval = pr.taxable_value 
                            and pr.document_date = b2b.dt
                            and pr.central_tax = b2b.cgst
                            and pr.state_tax = b2b.sgst
                            and pr.integrated_tax = b2b.igst;
                            """
        )
        fetch_data = self.env.cr.dictfetchall()
        for records in fetch_data:
            print(records)
            self.env["aipl.gst.b2b"].create(
                {
                    "gstin": records["gstin"],
                    "ctin": records["ctin"],
                    "dt": records["dt"],
                    "txval": records["txval"],
                    "cgst": records["cgst"],
                    "sgst": records["sgst"],
                    "igst": records["igst"],
                    "cess": records["cess"],
                }
            )
