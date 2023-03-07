# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ReportOpenacademYSession(models.AbstractModel):
    _name = "report.openacademy.report_openacademy_session"
    _description = "Get OpenAcademy session Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["openacademy.session"].browse(docids)
        email = docs.mapped("instructor_id.email")
        return {
            "doc_ids": docids,
            "doc_model": "openacademy.session",
            "docs": docs,
            "email": email,
        }
