# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
from odoo import models, fields, api


# class aipl_gst(models.Model):
#     _name = 'aipl_gst.aipl_gst'
#     _description = 'aipl_gst.aipl_gst'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class b2b(models.Model):
    _name = "aipl.gst.b2b"
    _description = "aipl.gst.b2b"
    _rec_name = "trdnm"

    gstin = fields.Char(string="GSTIN")
    fp = fields.Char(string="FP")
    trdnm = fields.Char(string="Trade Name")
    supfildt = fields.Date(string="Supply Filed Date")
    ctin = fields.Char(string="CTIN")
    dt = fields.Date(string="Date")
    val = fields.Float(string="Value")
    rev = fields.Char(string="Reverse")
    itcavl = fields.Char(string="ITC Available")
    diffprcnt = fields.Float(string="Difference Percentage")
    pos = fields.Char(string="POS")
    typ = fields.Char(string="Type")
    inum = fields.Char(string="Invoice Number")
    rsn = fields.Char(string="Reason")
    rt = fields.Float(string="Rate")
    num = fields.Float(string="Number")
    txval = fields.Float(string="Taxable Value")
    cess = fields.Float(string="Cess")
    igst = fields.Float(string="IGST")
    cgst = fields.Float(string="CGST")
    sgst = fields.Float(string="SGST")


class cdnr(models.Model):
    _name = "aipl.gst.cdnr"
    _description = "aipl.gst.cdnr"
    _rec_name = "trdnm"

    gstin = fields.Char(string="GSTIN")
    fp = fields.Char(string="FP")
    trdnm = fields.Char(string="Trade Name")
    supfildt = fields.Date(string="Supply Filed Date")
    supprd = fields.Char(string="Supprd")
    ctin = fields.Char(string="CTIN")
    dt = fields.Date(string="Date")
    val = fields.Float(string="Value")
    rev = fields.Char(string="Revision")
    itcavl = fields.Char(string="ITC Available")
    diffprcnt = fields.Float(string="Difference Percentage")
    pos = fields.Char(string="POS")
    typ = fields.Char(string="Type")
    suptyp = fields.Char(string="Supply Type")
    ntnum = fields.Char(string="Note Number")
    rsn = fields.Char(string="Reason")
    rt = fields.Float(string="Rate")
    num = fields.Float(string="Number")
    txval = fields.Float(string="Taxable Value")
    cess = fields.Float(string="Cess")
    igst = fields.Float(string="IGST")
    cgst = fields.Float(string="CGST")
    sgst = fields.Float(string="SGST")


class purchase_registry(models.Model):
    _name = "aipl.purchase.register"
    _description = "aipl.purchase.register"
    _rec_name = "org_name"

    org_name = fields.Char(string="Organisation Name")
    gstin = fields.Char(string="GSTIN")
    financial_year = fields.Char(string="Financial Year")
    tax_period = fields.Char("Tax Period")
    gstin_supplier = fields.Char(string="GSTIN Supplier")
    supplier_name = fields.Char(string="Supplier Name")
    a = fields.Char(string="A")
    document_type = fields.Char(string="Document Type")
    document_number = fields.Char(string="Document Number")
    document_date = fields.Date(string="Document Date")
    taxable_value = fields.Float(string="Taxable Value")
    integrated_tax = fields.Float(string="Integrated Tax")
    central_tax = fields.Float(string="Central Tax")
    state_tax = fields.Float(string="State Tax")
    cess = fields.Float(string="Cess")
