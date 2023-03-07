from odoo import api, fields, models


class ReportAiplPurchase(models.AbstractModel):
    _name = "report.aipl_purchase.report_aipl_purchase_template"
    _description = "Aipl Purchase Report"

    @api.model
    def _sample_report(self, docsids, data=None):
        docs = self.env["aipl_purchase.res_partner"].browse(docsids)
        return {
            "doc_ids": docsids,
            "doc_model": "aipl_purchase.res_partner",
            "docs": docs,
        }
