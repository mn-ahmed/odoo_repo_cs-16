from odoo import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    tax_ids = fields.Many2many('account.tax', string='Products')
