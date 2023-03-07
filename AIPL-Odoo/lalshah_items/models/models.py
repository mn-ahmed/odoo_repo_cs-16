# -*- coding: utf-8 -*-

from odoo import models, fields, api
import math


class lalshah_items(models.Model):
    _name = "lalshah_items.lalshah_items"
    _description = "lalshah_items.lalshah_items"
    _rec_name = "item_name"

    item_name = fields.Char(string="Item Name")
    item_description = fields.Text(string="Item Description")
    item_unit = fields.Char(string="Unit")
    item_hsn = fields.Integer(string="HSN")
    item_porate = fields.Float(string="PO Rate")
    item_gstrate = fields.Float(string="GST Rate")
    item_porate_inc_gstrate = fields.Float(string="PO Rate (Inc GST)")
    margin = fields.Float(string="Margin")
    ns_rate = fields.Float(string="NS Rate", compute="_compute_ns_rate", store=True)
    cs_rate = fields.Float(string="CS Rate")
    status = fields.Boolean(string="Status", required=True, default=True)
    updated_timestamp = fields.Datetime(
        string="Timestamp", default=lambda self: fields.datetime.now(), readonly=True
    )

    @api.onchange("item_porate", "margin")
    def onchange_item_porate(self):
        print(self)
        if self.item_porate and self.margin:
            self.ns_rate = self.item_porate + (self.item_porate * self.margin / 100)

    def action_activate(self):
        for record in self:
            record.status = True
            record.updated_timestamp = fields.datetime.now()
        return True

    def action_deactivate(self):
        for record in self:
            record.status = False
            record.updated_timestamp = fields.datetime.now()
        return True

    @api.depends("ns_rate")
    @api.onchange("item_porate", "margin", "ns_rate")
    def _compute_ns_rate(self):
        for record in self:
            record.ns_rate = float(math.ceil(float(record.ns_rate) * 4) / 4)
