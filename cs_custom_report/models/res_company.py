from odoo import models, api, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    get_secret_key = fields.Char("GST Client Secret Key")
    pend_cnt = fields.Integer(string="Pending Count", readonly=True)