# -*- coding: utf-8 -*-
from odoo import http
import requests
from odoo.http import request
from psycopg2.errors import IntegrityError
from dateutil import parser
import traceback


class Sg(http.Controller):
    @http.route("/sg/sg", auth="public")
    def index(self, **kw):
        return "Hello, world"

    @http.route("/sg/delete", auth="public")
    def delete(self, **kw):
        record_set = request.env["sg.attendance"].search([])
        record_set.unlink()
        return "delete"

    @http.route("/sg/sg/objects", auth="public")
    def list(self, **kw):
        try:
            if len(request.env["sg.attendance"].search([])) == 1:
                r = requests.get(
                    "http://13.235.113.114/aipl/attendance/data/api",
                    params={
                        "date": request.env["sg.attendance"].search([])[-1].timestamp
                    },
                )
            else:
                r = requests.get("http://13.235.113.114/aipl/attendance/data/api")

            for x in r.json():
                try:
                    result = request.env["sg.organisation"].search(
                        [("b_no", "=", x.get("b_no"))]
                    )
                    if result:
                        x["b_no"] = result["id"]
                        x["timestamp"] = parser.parse(x["timestamp"])
                        request.env["sg.attendance"].sudo().create(x)
                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            return """
            ================================================
            Traceback: {}
            ================================================
            Error: {}
            """.format(
                traceback.format_exc(), e
            )
        return "dta"

    @http.route('/sg/sg/objects/<model("sg.sg"):obj>', auth="public")
    def object(self, obj, **kw):
        return http.request.render("sg.object", {"object": obj})
