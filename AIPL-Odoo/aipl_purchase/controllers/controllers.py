# -*- coding: utf-8 -*-
from odoo import http
import json


class aipl_purchase(http.Controller):
    @http.route("/aipl_purchase/", auth="public")
    def index(self, **kw):
        return http.request.render("aipl_purchase.form1")

    @http.route(
        "/aipl_purchase/form1_response",
        methods=["post"],
        type="http",
        auth="public",
        csrf=False,
    )
    def form1_response(self, **kw):
        # data = json.loads(http.request.form.get('data'))
        # file = http.request.files['file']
        if kw.get("json_file", False):
            name = kw.get("json_file").filename
            file = kw.get("json_file")
            fl = file.read().decode("utf8")
            # print(fl)

        # print(kw)

    # @http.route('/aipl_purchase/aipl_purchase/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('aipl_purchase.listing', {
    #         'root': '/aipl_purchase/aipl_purchase',
    #         'objects': http.request.env['aipl_purchase.aipl_purchase'].search([]),
    #     })

    # @http.route('/aipl_purchase/aipl_purchase/objects/<model("aipl_purchase.aipl_purchase"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('aipl_purchase.object', {
    #         'object': obj
    #     })
