# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import models, fields, api


class vidhansabha_voter(models.Model):
    _name = "vidhansabha.voter"
    _description = "vidhansabha voter data"
    _inherits = {"res.partner": "partner_id"}

    name = fields.Char(related="partner_id.name", inherited=True, readonly=False)
    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.user.company_id)

    eng_fullname = fields.Char()
    guj_fullname = fields.Char()
    fname = fields.Char()
    mname = fields.Char()
    surname = fields.Char()
    eng_fname = fields.Char()
    eng_mname = fields.Char()
    eng_surname = fields.Char()
    birthdate = fields.Date()
    phone_no = fields.Char()
    contact_no = fields.Char()
    ward = fields.Many2one('vidhansabha.ward')
    ward_name = fields.Char(related="ward.name")
    booth = fields.Many2one('vidhansabha.booth')
    booth_name = fields.Char(related="booth.name")
    eng_booth = fields.Char()
    booth_no = fields.Integer()
    address = fields.Char()
    soc_no = fields.Char()
    sex = fields.Char()
    age = fields.Integer()
    icard = fields.Char()
    eng_address = fields.Char()
    scode = fields.Char()
    ac_no = fields.Char()
    booth_no = fields.Char()
    serialno = fields.Char()
    mathak_no = fields.Char()
    district = fields.Char()
    vibhag_no = fields.Char()
    house_no = fields.Char()
    house_no_e = fields.Char()
    rln_fm_name = fields.Char()
    rln_m_name = fields.Char()
    rln_lastname = fields.Char()
    rln_fm_name_e = fields.Char()
    rln_eng_m_name = fields.Char()
    rln_lastname_e = fields.Char()
    rln_type = fields.Char()
    statustype = fields.Char()
    rollno = fields.Char()
    mrollno = fields.Char()
    ecast = fields.Char()

    partner_id = fields.Many2one("res.partner", ondelete="cascade", required=True)

    def create_company(self):
        return super().create_company()

    def _compute_name(self):
        for record in self:
            record.name = f"{record.fname} {record.mname} {record.surname}"

    def _message_get_suggested_recipients(self):
        recipients = super(vidhansabha_voter, self)._message_get_suggested_recipients()


    def action_view_partner_invoices(self):
        return super().action_view_partner_invoices()

    def action_open_employees(self):
        return super().action_open_employees()

    def phone_action_blacklist_remove(self):
        return super().phone_action_blacklist_remove()

    def mail_action_blacklist_remove(self):
        return super().mail_action_blacklist_remove()

    def open_commercial_entity(self):
        return super().open_commercial_entity()

    def action_view_sale_order(self):
        return super().action_view_sale_order()

    def action_view_certifications(self):
        return super().action_view_certifications()

    def action_update_full_name(self):
        for record in self:
            # record.eng_fullname = f"{record.eng_fname or ''} {record.eng_mname or ''} {record.eng_surname or ''}"
            record.name = record.eng_fullname
            # record.guj_fullname = f"{record.fname or ''} {record.mname or ''} {record.surname or ''}"


# class vidhansabha_page_samiti(models.Model):
#     _name = "vidhansabha.page.samiti"
#     _description = "page samiti data"
#     _inherits = {"vidhansabha.voter": "voter_id"}

#     voter_id = fields.Many2one("vidhansabha.voter", ondelete="cascade", required=True)
#     page_no = fields.Integer()
#     booth_no = fields.Integer()
#     name = fields.Char()
#     address = fields.Char()
#     contact_no = fields.Char()
#     designation = fields.Char()


class booth_personnel(models.Model):
    _inherit = "res.partner"

    booth_name = fields.Char()
    booth_incharge = fields.Char()
    booth_head = fields.Char(string="Booth Head")
    mobile_no = fields.Char()
    member_warning = fields.Char()


class vidhansabha_chairman_secretary(models.Model):
    _name = "vidhansabha.chairman.secretary"
    _description = "vidhansabha chairman secretary data"
    _inherits = {"vidhansabha.voter": "voter_id"}

    shaktikendra_name = fields.Char()
    booth_no = fields.Char()
    society_name = fields.Char()
    total_voters = fields.Char()
    chairman_name = fields.Char()
    mobile_no = fields.Integer()
    secretary_name = fields.Char()
    voter_id = fields.Many2one("vidhansabha.voter", ondelete="cascade", required=True)


class vidhansabha_booth(models.Model):
    _name = "vidhansabha.booth"
    _description = "vidhansabha booth data"
    _inherits = {"crm.team": "crm_team_id"}
    _rec_name = "booth_no"

    scode = fields.Char()
    ac_no = fields.Char()
    booth_no = fields.Char()
    mathak_no = fields.Char()
    mathak_locn_no = fields.Char()
    mathak_name = fields.Char()
    mathak_name_e = fields.Char()
    district = fields.Char()
    matdan_location = fields.Char()
    matdan_location_e = fields.Char()
    mathak_area = fields.Char()
    mathak_area_e = fields.Char()
    blo = fields.Char()
    blo_contact = fields.Char()
    taluka = fields.Char()
    locn_dtl = fields.Char()
    eng_locn_dtl = fields.Char()
    fvtm_no = fields.Char()
    fvtm_type = fields.Char()
    ac_no_11 = fields.Char()
    part_no_11 = fields.Char()
    ac_no_14 = fields.Char()
    part_no_14 = fields.Char()
    ac_no_13 = fields.Char()
    part_no_13= fields.Char()	
    ac_no_15	= fields.Char()
    part_no_15	= fields.Char()
    ac_no_16	= fields.Char()
    part_no_16	= fields.Char()
    ac_no_17	= fields.Char()
    part_no_17	= fields.Char()
    incharge	= fields.Char()
    inchargecontact = fields.Char()	
    agent1	 = fields.Char()
    agent1contact	 = fields.Char()
    agent2	= fields.Char()
    agent2contact= fields.Char()
    booth_id = fields.Many2one('vidhansabha.booth.list')
    crm_team_id = fields.Many2one("crm.team", ondelete="cascade", required=True)
    # tag_id = fields.Many2one("vidhansabha.voter", ondelete="cascade", required=True)


class vidhansabha_ward(models.Model):
    _name = "vidhansabha.ward"
    _description = "vidhansabha ward data"
    _inherits = {"vidhansabha.voter": "voter_id"}

    name = fields.Char()
    guj_name = fields.Char()
    voter_id = fields.Many2one("vidhansabha.voter", ondelete="cascade", required=True)
    # booth_id = fields.Many2one("vidhansabha.booth", "Booth", ondelete="cascade", required=False)


class booth_list(models.Model):
    _name = 'vidhansabha.booth.list'
    _description = "Booth List"

    name= fields.Char()
    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.user.company_id)
    booth_ids = fields.One2many("vidhansabha.booth", 'booth_id')


class vidhansabha_vibhag(models.Model):
    _name = "vidhansabha.vibhag"
    _description = "Vibhag"
    _rec_name = "society"

    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.user.company_id)
    scode = fields.Char() 
    district = fields.Char()
    ac_no = fields.Char()
    booth = fields.Many2one('vidhansabha.booth')
    booth_name = fields.Char(related="booth.name")
    mathak_no = fields.Char()
    vibhag_no = fields.Char()
    society = fields.Char()
    society_e = fields.Char()
    area1 = fields.Char()
    area_e = fields.Char()
    pincode = fields.Char()

class vidhansabha_karyakarta(models.Model):
    _name = "vidhansabha.karyakarta"
    _description = "Vidhansabha Karyakarta"
    _inherits = {"res.partner":"partner_id"}

    ward = fields.Char()
    name = fields.Char(related="partner_id.name", inherited=True, readonly=False)
    responsibility_1 = fields.Char() 
    responsibility_2 = fields.Char()
    responsibility_3 = fields.Char()
    location = fields.Char()
    mobile = fields.Char()
    booth  = fields.Char()
    partner_id = fields.Many2one("res.partner", ondelete="cascade", required=True)

