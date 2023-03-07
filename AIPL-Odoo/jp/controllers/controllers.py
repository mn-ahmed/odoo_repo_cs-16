# -*- coding: utf-8 -*-
# from odoo import http


# class Jp(http.Controller):
#     @http.route('/jp/jp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jp/jp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jp.listing', {
#             'root': '/jp/jp',
#             'objects': http.request.env['jp.jp'].search([]),
#         })

#     @http.route('/jp/jp/objects/<model("jp.jp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jp.object', {
#             'object': obj
#         })
