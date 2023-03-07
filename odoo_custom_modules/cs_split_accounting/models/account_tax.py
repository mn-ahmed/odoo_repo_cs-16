from odoo import models, api, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    is_split_account = fields.Boolean(string='Split Account', default=False,
                                      help="Check this if the price you use on the product and invoices includes this tax."
                                      )
