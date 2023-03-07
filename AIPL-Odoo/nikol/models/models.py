# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nikol(models.Model):
    _name = "nikol.matdar.yaadi"
    _description = "nikol.matdar.yaadi"

    vidhansabha = fields.Integer()
    booth_no = fields.Integer()
    kram = fields.Integer()
    dist = fields.Integer()
    fname = fields.Char()
    mname = fields.Char()
    surname = fields.Char()
    eng_fname = fields.Char()
    eng_mname = fields.Char()
    eng_surname = fields.Char()
    icard = fields.Char()
    sex = fields.Char()
    relation = fields.Char()
    age = fields.Integer()
    birthdate = fields.Date()
    phone_no = fields.Char()
    contact_no = fields.Char()
    soc_no = fields.Integer()
    address = fields.Char()
    eng_address = fields.Char()
    booth = fields.Char()
    eng_booth = fields.Char()
    assigned_user_id = fields.Many2one("res.users", string="Assigned User")



class nikol_chairman_secretary(models.Model):
    _name = "nikol.chairman.secretary"
    _description = "nikol.chairman.secretary"

    shaktikendra_name = fields.Char()
    booth_no = fields.Integer()
    booth_area = fields.Integer()
    nof_voters = fields.Integer()
    chairman_name = fields.Char()
    chairman_mobile = fields.Char()
    secretary_name = fields.Char()
    secretary_mobile = fields.Char()
    total_voters = fields.Integer()
    ward = fields.Char()
    nof_booth = fields.Integer()
    nof_shaktikendra = fields.Integer()
    assembly = fields.Char()



class res_partner(models.Model):
    _name = "nikol.res.partner"
    _inherits = {"res.partner": "partner_id"}
    _description = "nikol res partner"

    kram = fields.Integer()
    vidhansabha = fields.Integer()
    booth_no = fields.Integer()
    kram = fields.Integer()
    dist = fields.Integer()
    fname = fields.Char()
    mname = fields.Char()
    surname = fields.Char()
    eng_fname = fields.Char()
    eng_mname = fields.Char()
    eng_surname = fields.Char()
    icard = fields.Char()
    sex = fields.Char()
    relation = fields.Char()
    age = fields.Integer()
    birthdate = fields.Date()
    phone_no = fields.Char()
    contact_no = fields.Char()
    soc_no = fields.Integer()
    address = fields.Char()
    eng_address = fields.Char()
    booth = fields.Char()
    eng_booth = fields.Char()

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        ondelete="cascade",
        string="Related Partner",
        help="Partner-related data of the user",
    )


    def create_company(self):
        return super().create_company()


class viratnagar_general_body(models.Model):
    _name = "viratnagar.general_body"
    _description = "viratnagar general body"

    designation = fields.Char()
    name = fields.Char()
    contact_no = fields.Char()
    full_address = fields.Char()
    eng_designation = fields.Char()
    eng_name = fields.Char()
    eng_contact_no = fields.Char()
    eng_full_address = fields.Char()


class viratnagar_page_samiti(models.Model):
    _name = "viratnagar.page_samiti"
    _description = "viratnagar page samiti"

    page_no = fields.Integer()
    booth_no = fields.Integer()
    name = fields.Char()
    surname = fields.Char()
    contact_us = fields.Integer()
    designation = fields.Char()
    vishansabha = fields.Char()
    ward = fields.Char()
    shaktikendra = fields.Char()
    shaktikendra_mobile = fields.Char()
    incharge = fields.Char()
    incharge_mobile = fields.Integer()


class amraiwadi_page_samiti(models.Model):
    _name = "amraiwadi.page.samiti"
    _description = "amraiwadi page samiti"

    ward_number = fields.Integer()
    ward_name = fields.Char()
    booth_no = fields.Integer()
    new_si_no = fields.Integer()
    address = fields.Char()
    full_name = fields.Char()
    mobile = fields.Char()
    designation = fields.Char()

