# -*- coding: utf-8 -*-

from odoo import models, fields, api
from xlrd import open_workbook
from io import StringIO
import base64
from odoo.exceptions import UserError


class upload_stock(models.TransientModel):
    _name = 'stock_info.upload_stock'
    _description = 'stock_info.upload_stock'
    
    upload_file = fields.Binary(string='Upload file')

    def upload_excel(self):
        try:
            file_data = base64.b64decode(self.upload_file)
            wb = open_workbook(file_contents=file_data)
        except FileNotFoundError as e:
            raise UserError(
                'No such file or directory found. \n%s.' % self.file_name
            ) from e
        sheet = wb.sheet_by_index(0)
        stock_list, stock_dict = [], {}
        # Delete all records
        self.env['stock_info.stock'].search([]).unlink()
        
        for row in range(1, sheet.nrows):
            product_name = sheet.cell(row, 0).value
            mir_stock = sheet.cell(row, 1).value
            sar_stock = sheet.cell(row, 2).value
            if product := self.env['product.product'].search(
                [('default_code', '=', product_name)]
                ):
                stock_dict = {
                    'product_id': product.id,
                    'mir_stock': mir_stock,
                    'sar_stock': sar_stock,
                }
                stock_list.append(stock_dict)

        self.env['stock_info.stock'].create(stock_list)

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
