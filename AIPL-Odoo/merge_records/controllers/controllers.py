# -*- coding: utf-8 -*-
# from odoo import http


# class MergeRecords(http.Controller):
#     @http.route('/merge_records/merge_records', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/merge_records/merge_records/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('merge_records.listing', {
#             'root': '/merge_records/merge_records',
#             'objects': http.request.env['merge_records.merge_records'].search([]),
#         })

#     @http.route('/merge_records/merge_records/objects/<model("merge_records.merge_records"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('merge_records.object', {
#             'object': obj
#         })
