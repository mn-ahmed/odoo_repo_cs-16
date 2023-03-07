# -*- coding: utf-8 -*-
# from odoo import http


# class CsSplitAccounting(http.Controller):
#     @http.route('/cs_split_accounting/cs_split_accounting', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cs_split_accounting/cs_split_accounting/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cs_split_accounting.listing', {
#             'root': '/cs_split_accounting/cs_split_accounting',
#             'objects': http.request.env['cs_split_accounting.cs_split_accounting'].search([]),
#         })

#     @http.route('/cs_split_accounting/cs_split_accounting/objects/<model("cs_split_accounting.cs_split_accounting"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cs_split_accounting.object', {
#             'object': obj
#         })
