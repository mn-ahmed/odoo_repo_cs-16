# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cs_split_accounting(models.Model):
#     _name = 'cs_split_accounting.cs_split_accounting'
#     _description = 'cs_split_accounting.cs_split_accounting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
