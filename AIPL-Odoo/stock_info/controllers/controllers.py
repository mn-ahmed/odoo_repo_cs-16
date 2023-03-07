# -*- coding: utf-8 -*-
# from odoo import http


# class StockInfo(http.Controller):
#     @http.route('/stock_info/stock_info', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_info/stock_info/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_info.listing', {
#             'root': '/stock_info/stock_info',
#             'objects': http.request.env['stock_info.stock_info'].search([]),
#         })

#     @http.route('/stock_info/stock_info/objects/<model("stock_info.stock_info"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_info.object', {
#             'object': obj
#         })
