import json

import requests

from odoo import models, fields
# from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    secret_key = fields.Char(compute='_compute_secret_key')

    # gst_verified = fields.Boolean(string="GST Verified", default=False, readonly=True)
    # pan_number = fields.Char(string="PAN Number")

    def _compute_secret_key(self):
        for record in self:
            record.secret_key = self.env.user.company_id.get_secret_key

    def get_detail_from_gst(self):
        gst_secret_key = self.env.user.company_id.get_secret_key
        if (type(self.vat) is str) and (gst_secret_key is not False):
            url = "https://gmbportsgst.app:5443/gstin/GETGSTINUser?Secretkey={0}&GSTIN={1}".format(gst_secret_key,
                                                                                                   self.vat
                                                                                                   )
            response = requests.get(url)
            if response.status_code == 200:
                response_data = json.loads(response.content)
                if response_data['GSTIN'] is None:
                    raise ValidationError('The GSTIN "%s" is not valid!' % self.vat)
                else:
                    for record in self:
                        record.name = response_data['lgnm']
                        record.write({
                            'street': response_data['address'],
                            'street2': response_data['stj'],
                            'city': response_data['ctj'],
                            'state_id': False,
                            'zip': 390011,
                            'country_id': self.env.ref('base.in').id,
                            # 'gst_verified': True,
                            'l10n_in_pan': self.vat[2:12]
                        }
                        )

                        company = self.env['res.company'].search([('id', '=', self.env.user.company_id.id)], limit=1)
                        company.write({
                            'pend_cnt': response_data['pendCnt'],
                        }
                        )
                        # for resComp in company:



                        # # record.type = response_data['address']
                        # record.street = response_data['stj']
                        # record.city = response_data['ctj']
                        # record.l10n_in_pan = self.vat[2:12]
            else:
                raise ValidationError('The GSTIN "%s" is not valid!' % self.vat)
        else:
            raise ValidationError('Secret key not valid contact your administrator')

    # @api.onchange('vat')
    # def onchange_gst_verified(self):
    #     for rec in self:
    #         if rec.vat:
    #             rec.gst_verified = False
