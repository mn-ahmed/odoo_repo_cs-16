from odoo import fields, api, models
from odoo.exceptions import UserError
import json
import requests


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gst_verified = fields.Boolean(string="GST Verified", default=False, readonly=True)
    pan_number = fields.Char(string="PAN Number")

    def fetch_address(self):
        appyflow = self.env.user.company_id.appyflow_key
        for rec in self:
            if rec.vat:
                url = 'https://appyflow.in/api/verifyGST?gstNo=' + str(rec.vat) + "&key_secret=" +str(appyflow)
                result = json.loads(requests.get(url).content)
                if not result.get('error'):
                    tax = result.get('taxpayerInfo', False)
                    if tax:
                        results = tax.get('pradr', {}).get('addr', {})
                        temp_street = [results.get('bno', False), results.get('flno', False)]
                        temp_street = '/'.join(map(str, temp_street))
                        street = [temp_street, results.get('bnm')]
                        state_rec = self.env['res.country.state'].search([('name', '=', results.get('stcd'))])
                        rec.write({
                            'street': ', '.join(map(str, street)),
                            'street2': results.get('st', False),
                            'city': results.get('city', False) and results.get('city') or results.get('dst', False),
                            'state_id': state_rec and state_rec.id or False,
                            'zip': results.get('pncd', False),
                            'country_id': self.env.ref('base.in').id,
                            'gst_verified': True,
                            'pan_number': tax.get('panNo', False)
                        })
                else:
                    raise UserError(result.get('message'))

    @api.onchange('vat')
    def onchange_gst_verified(self):
        for rec in self:
            if rec.vat:
                rec.gst_verified = False


class ResCompany(models.Model):
    _inherit = 'res.company'

    appyflow_key = fields.Char("AppyFlow Client Secret Key")