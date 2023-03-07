# -*- coding: utf-8 -*-
# from odoo import http


# class CsCustomReport(http.Controller):
#     @http.route('/cs_custom_report/cs_custom_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cs_custom_report/cs_custom_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cs_custom_report.listing', {
#             'root': '/cs_custom_report/cs_custom_report',
#             'objects': http.request.env['cs_custom_report.cs_custom_report'].search([]),
#         })

#     @http.route('/cs_custom_report/cs_custom_report/objects/<model("cs_custom_report.cs_custom_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cs_custom_report.object', {
#             'object': obj
#         })
