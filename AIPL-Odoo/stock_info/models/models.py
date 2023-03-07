# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
import re

class stock_info(models.Model):
    _name = 'stock_info.stock'
    _description = 'stock_info.stock_info'  
    
    product_id = fields.Many2one('product.product', string='Product')
    product_name = fields.Char(related='product_id.name')
    mir_stock = fields.Integer(string='MIR Stock')
    sar_stock = fields.Integer(string='SAR Stock')
    
    def confirm(self):
        self.product_id.name = re.sub(' +', ' ', self.product_id.name)
        product_name = self.product_id.name.translate(str.maketrans({
            '/': '',
            ' ': '-',
        })).lower()
        default_code = re.sub(' +', ' ', self.product_id.default_code)
        default_code = default_code.translate(str.maketrans({
            '/': '',
            ' ': '-',
        })).lower()
        return {
                "type": "ir.actions.act_url",
                "url": f"{request.httprequest.host_url}@/shop/{default_code}-{product_name}-{self.product_id.product_tmpl_id.id}",
                "target": "self",
            }
