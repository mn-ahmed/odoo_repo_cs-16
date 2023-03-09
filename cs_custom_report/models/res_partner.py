import json

import requests

from odoo import models, fields
# from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    secret_key = fields.Char(compute='_compute_secret_key')
    legal_name = fields.Char('Legal Name', readonly=True)

    # gst_verified = fields.Boolean(string="GST Verified", default=False, readonly=True)
    # pan_number = fields.Char(string="PAN Number")

    def _compute_secret_key(self):
        for record in self:
            record.secret_key = self.env.user.company_id.get_secret_key

    def get_detail_from_gst(self):
        gst_secret_key = self.env.user.company_id.get_secret_key
        if (type(self.vat) is str) and (type(gst_secret_key) is str):
            url = "https://gmbportsgst.app:5443/gstin/GETGSTINUser?Secretkey={0}&GSTIN={1}".format(gst_secret_key,
                                                                                                   self.vat
                                                                                                   )
            # url = "http://192.168.2.153:9988/gstin/GETGSTINUser?Secretkey={0}&GSTIN={1}".format(gst_secret_key,
            #                                                                                        self.vat
            #                                                                                        )
            response = requests.get(url)
            if response.status_code == 200:
                response_data = json.loads(response.content)
                if response_data['GSTIN'] is None:
                    raise ValidationError('The GSTIN "%s" is not valid!' % self.vat)
                else:
                    state_rec = self.env['res.country.state'].search([('l10n_in_tin', '=', str(self.vat)[0:2])])
                    for record in self:
                        record.write({
                            'street': get_address_line_1(response_data['address']),
                            'street2': get_address_line_2(response_data['address']),
                            'city': response_data['city'],
                            'state_id': state_rec and state_rec.id or False,
                            'zip': response_data['pincode'],
                            'country_id': self.env.ref('base.in').id,
                            # 'gst_verified': True,
                            'l10n_in_pan': self.vat[2:12],
                            'legal_name': response_data['lgnm']
                        }
                        )

                        company = self.env['res.company'].search([('id', '=', self.env.user.company_id.id)], limit=1)
                        company.write({
                            'pend_cnt': response_data['pendCnt'],
                        })
            else:
                raise ValidationError('The GSTIN "%s" is not valid!' % self.vat)
        else:
            raise ValidationError('Secret key not valid contact your administrator')

    # @api.onchange('vat')
    # def onchange_gst_verified(self):
    #     for rec in self:
    #         if rec.vat:
    #             rec.gst_verified = False


def get_address_line_1(address):
    main_list = address.split()

    if len(main_list) > 5:
        return ' '.join(str(main_list[i]) for i in range(5))
    else:
        return address


def get_address_line_2(address):
    main_list = address.split()

    if len(main_list) >= 5:
        return ' '.join(str(main_list[i]) for i in range(5, len(main_list)))
    else:
        return ''
