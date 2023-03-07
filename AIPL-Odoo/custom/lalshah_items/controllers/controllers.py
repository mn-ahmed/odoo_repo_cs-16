# -*- coding: utf-8 -*-
# from odoo import http


# class LalshahItems(http.Controller):
#     @http.route('/lalshah_items/lalshah_items/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lalshah_items/lalshah_items/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lalshah_items.listing', {
#             'root': '/lalshah_items/lalshah_items',
#             'objects': http.request.env['lalshah_items.lalshah_items'].search([]),
#         })

#     @http.route('/lalshah_items/lalshah_items/objects/<model("lalshah_items.lalshah_items"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lalshah_items.object', {
#             'object': obj
#         })
