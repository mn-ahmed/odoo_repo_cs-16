from odoo import models, api, fields
import json
from collections import defaultdict
# from odoo.tools import (
#     formatLang,
# )

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange(
        'invoice_line_ids.currency_rate',
        'invoice_line_ids.tax_base_amount',
        'invoice_line_ids.tax_line_id',
        'invoice_line_ids.price_total',
        'invoice_line_ids.price_subtotal',
        'invoice_line_ids',
        'invoice_payment_term_id',
        'partner_id',
        'currency_id',
    )
    def on_change_line_id(self):
        # fatchData = self.env['account.move.line'].browse(self.journal_id)
        # print(fatchData)
        # print(self.journal_id.journal_group_ids.excluded_journal_ids)
        # print(self.tax_totals.amount_total)

        # print(self.tax_totals['groups_by_subtotal'])
        # data = self.tax_totals['groups_by_subtotal']
        # self.tax_totals.am
        # print(json.dump(dict, data))
        # journal = self._search_default_journal()
        # print(self.line_ids[0])
        journal_vals = {
                "move_id": self._origin.id,
                "account_id": 171,
                'name': 'Reverse Deducted',
                # 'type': 'purchase',
                'debit': 100,
                'credit': 0
            }

        # self.line_ids.update(journal_vals)
        data = self.line_ids[1].copy(default={'move_id': self._origin.id})
        print(data)
        # data = self.line_ids[0].copy(default={'move_id': self._origin.id})
        # data.debit = 100
        # print(data)
        # for data in self.invoice_line_ids.tax_ids:
        #     print(data.id)
            # if self.invoice_line_ids.tax_ids.id == 510:
            # self.copy(default={'id': data.id})
            # if data.is_split_account is True and journal is not None and (journal.type in ['purchase']):
            #     print('Require Split Account')
            #     # data.amount = abs(data.amount)
            #     # data.real_amount = abs(data.real_amount)
            #     print(data.amount)
            #     print(data.real_amount)
            #     journal_vals = {
            #         "move_id": self._origin.id,
            #         "account_id": 1,
            #         'name': 'Reverse Deducted',
            #         # 'type': 'purchase',
            #         'debit': 100,
            #         'credit': 0
            #     }
            #
            #     new_journal = self.env['account.move.line'].create(journal_vals)
            #     print(new_journal)
                # self.env['account.journal'].crea
        # self.tax_totals['amount_total'] = 50000
        # print(self.tax_totals)
        # for m in self:
        #     journal_type = m.invoice_filter_type_domain or 'general'
        #     company_id = m.company_id.id or self.env.company.id
        #     domain = [('company_id', '=', company_id), ('type', '=', journal_type)]
        #     m.suitable_journal_ids = self.env['account.journal'].search(domain)

    # @api.model_create_multi
    # def _compute_tax_totals(self):
    #     res = super(AccountMove, self)._compute_tax_totals()
    #     return res

