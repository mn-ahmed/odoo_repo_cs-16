# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    test = fields.Char(string="Test")
    ifsc_id = fields.Many2one("aipl.ifsc", string="IFSC")


class purchase(models.Model):
    # _name = 'aipl.purchase'
    _description = "aipl.purchase"
    _inherit = "res.partner"

    prac = fields.Char(string="Practice Name")
    nature_of_payment = fields.Char(string="Nature of Payment")
    pan = fields.Char(string="PAN")
    pan_type = fields.Char(string="PAN Type")
    session_ids = fields.Many2many(
        "res.partner",
        "aipl_session_partner_rel",
        "purchase_ids",
        "session_ids",
        string="session",
    )
    channel_ids = fields.Many2many(
        "res.partner",
        "channel_partner_rel",
        "purchase_ids",
        "channel_ids",
        string="channel",
    )
    sla_ids = fields.Many2many(
        "res.partner", "aipl_sla_partner_rel", "purchase_ids", "sla_ids", string="SLA"
    )
    gstin = fields.Char(string="GSTIN")
    gstin_state = fields.Char(string="GSTIN State")
    ifsc_id = fields.Many2one("aipl.ifsc", string="IFSC")
    bank_name = fields.Char(string="Bank Name")
    bank_branch = fields.Char(string="Bank Branch")

    @api.onchange("pan")
    def pan_type_change(self):
        pan_types = {
            "A": "Association of Persons (AoP)",
            "B": "Body of Individuals (BOI)",
            "C": "Company",
            "F": "Firm/Limited Liability Partnership",
            "G": "Government Agency",
            "H": "Hindu Undivided Family (HUF) ",
            "J": "Artificial Juridical Person",
            "L": "Local Authority",
            "P": "Individual ",
            "T": "Trust",
        }
        for record in self:
            if record.pan:
                pan_initials = record.pan[4].upper()
                record.pan_type = pan_types.get(pan_initials)
                if pan_initials == "C":
                    record.company_type = "company"
                else:
                    record.company_type = "person"

    @api.constrains("pan")
    def _check_pan(self):
        for record in self:
            if record.pan:
                if len(record.pan) != 10:
                    raise ValidationError("PAN should be 10 digits")
            else:
                raise ValidationError("Please enter Pan Number")

    @api.onchange("gstin")
    def _get_state(self):
        for record in self:
            # self.env.cr.execute("SELECT * FROM aipl_gstin_master where")
            # self.env.cr.fetchall()
            if record.gstin:
                dt = self.env["aipl.gstin_master"].search(
                    [("code", "=", record.gstin[0:2])]
                )
                print("*" * 1000)
                print(record.gstin[:2], dt.name)
                record.gstin_state = dt.name

    @api.onchange("ifsc_id")
    def _get_bank_name(self):
        for record in self:
            if record.ifsc_id:
                record.bank_name, record.bank_branch = (
                    record.ifsc_id.bank,
                    record.ifsc_id.branch,
                )


class gstin_state_master(models.Model):
    _name = "aipl.gstin_master"
    _description = "gstin.state.master"

    name = fields.Char(string="State Name")
    code = fields.Char(string="State Code")


class bank(models.Model):
    _inherit = "res.partner.bank"
    _description = "aipl.bank"

    ifsc_id = fields.Many2one("aipl.ifsc", string="IFSC")


class ifsc(models.Model):
    _name = "aipl.ifsc"
    _description = "aipl.ifsc"

    name = fields.Char(string="IFSC")
    bank = fields.Char(string="Bank")
    branch = fields.Char(string="Branch")
    address = fields.Char(string="Address")
    city1 = fields.Char(string="City")
    city2 = fields.Char(string="City2")
    state = fields.Char(string="State")
    std_code = fields.Char(string="STD Code")
    phone = fields.Char(string="Phone")
