# -*- coding: utf-8 -*-

from odoo import models, fields, api

class account_move_line(models.Model):
    _inherit = 'account.move.line'


class print_contacts(models.Model):
    inherit = 'res.partner'

    def print_checkin(self):
        return self.env.ref('print_contacts.action_report_checkin').report_action(self)