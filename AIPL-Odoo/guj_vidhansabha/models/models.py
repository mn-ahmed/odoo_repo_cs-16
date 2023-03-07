# -*- coding: utf-8 -*-

from odoo import models, fields, api

class guj_vidhansabha_voter(models.Model):
    _name = "guj_vidhansabha.voter"
    _description = "guj_vidhansabha voter data"
    _inherits = {"res.partner": "partner_id"}

    name = fields.Char(related="partner_id.name", inherited=True, readonly=False,compute="_compute_name")
    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.user.company_id)

    eng_fullname = fields.Char()
    guj_fullname = fields.Char()
    booth_id = fields.Many2one("guj_vidhansabha.booth")
    booth_name = fields.Char(related="booth_id.mathak_name_e")
    ward_name = fields.Char(related="booth_id.booth_no.name")
    vibhag = fields.Many2one("crm.team")
    vibhag_address = fields.Char(related="vibhag.society_e")
    fname = fields.Char()
    mname = fields.Char()
    surname = fields.Char()
    eng_fname = fields.Char()
    eng_mname = fields.Char()
    eng_surname = fields.Char()
    birthdate = fields.Date()
    phone_no = fields.Char()
    contact_no = fields.Char()
    # ward_name = fields.Char(related="booth.booth_no.name")
    # booth = fields.Many2one('guj_vidhansabha.booth')
    # booth_name = fields.Char(related="booth.name")
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

    # def _message_get_suggested_recipients(self):
    #     return super()._message_get_suggested_recipients()


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
    
    def get_booth(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Booth',
            'view_mode': 'tree',
            'res_model': 'guj_vidhansabha.booth',
            'domain': [('booth_no', '=', self.booth_id)],
            'context': "{'create': False}"
        }

class guj_vidhansabha_ward(models.Model):
    _name = "guj_vidhansabha.ward"
    _description = "guj_vidhansabha ward data"
    _rec_name = "booth"

    name = fields.Char()
    guj_name = fields.Char()
    ward_no = fields.Integer()
    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.user.company_id)
    booth = fields.Integer()
    # booth_count = fields.Integer(compute="_booth_count", string="count")

    # def _booth_count(self):
    #     for record in self:
    #         record.booth_count = len(record.booth)

class guj_vidhansabha_mathak(models.Model):
    _name="guj_vidhansabha.mathak"
    _description = "Mathak"

    booth_id = fields.Many2one('guj_vidhansabha.booth')
    # booth_ids = fields.One2many(related="ward_id.booth")

class guj_vidhansabha_booth(models.Model):
    _name = "guj_vidhansabha.booth"
    _description = "guj_vidhansabha booth data"
    _rec_name = "booth_no"

    scode = fields.Char()
    ac_no = fields.Char()
    booth_no = fields.Many2one('guj_vidhansabha.ward')
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


class guj_vidhansabha_vibhag(models.Model):
    _description = "Vibhag"
    _inherit = "crm.team"
    _rec_name = "vibhag_no"

    scode = fields.Char() 
    district = fields.Char()
    ac_no = fields.Char()
    booth_id = fields.Many2one('guj_vidhansabha.booth')
    users_ids = fields.Many2many('res.users')
    # booth_name = fields.Char(related="booth_id.name")
    mathak_no = fields.Char()
    vibhag_no = fields.Char()
    society = fields.Char()
    society_e = fields.Char()
    area1 = fields.Char()
    area_e = fields.Char()
    pincode = fields.Char()

    def write(self, vals_list):
        records = super().write(vals_list)
        users = self.env['res.users'].browse(self.users_ids.ids)
        if users.ids:
            self.message_subscribe(partner_ids=users.partner_id.ids)
        print(set(users.partner_id.ids) - set(vals_list['users_ids'][0][-1]))
        return records