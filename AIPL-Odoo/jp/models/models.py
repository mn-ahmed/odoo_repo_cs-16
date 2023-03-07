# -*- coding: utf-8 -*-

from odoo import models, fields, api


class jp(models.Model):
    _name = "jp.jp"
    _description = "jp.jp"

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends("value")
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class name_insert(models.Model):
    _name = "jp.name_insert"
    _description = "Name Insert Model"

    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="Mobile No")
    org_name = fields.Char(string="Org Name")
    last_name = fields.Char(string="Last Name")
    city = fields.Char(string="City")
    district = fields.Char(string="District")
    bhalaman_mobile_no = fields.Char(string="Bh Mobile No")
    bhalaman_name = fields.Many2one("jp.bhalaman_name", "bhalaman_name")
    topic = fields.Char(string="Topic")
    matter = fields.Char(string="Matter")


class bhalaman_name(models.Model):
    _name = "jp.bhalaman_name"
    _description = "Bhalaman Name"

    name = fields.Char(string="Name")
    category = fields.Selection([("vip", "VIP"), ("normal", "Normal")])
    # bhalaman_name_id = fields.Many2one('jp.name_insert', 'name_insert')
