# -*- coding: utf-8 -*-

from odoo import models, fields, api


class jrk_product(models.Model):
    _name = "jrk.product"
    _description = "jrk product"

    No = fields.Char()
    Description = fields.Char()
    Target = fields.Char()
    Group = fields.Char()
    Marketing_Terminology = fields.Char()
    Brand = fields.Char()
    Brand_Category = fields.Char()
    Item_Class = fields.Char()
    Item_Category_Code = fields.Char()
    Item_Subcategory_Code = fields.Char()
    Product_Group_Code = fields.Char()


class jrk_purchase(models.Model):
    _inherit = "purchase.order.line"

    # company_name = fields.Char(string="Company  Name")
    deets = fields.Many2one("jrk.product", string="Deets")
