# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError


class OpenacademyCourse(models.Model):
    _name = "openacademy.course"
    _description = "Training Course"
    _inherit = "mail.thread"

    name = fields.Char("Name", required=True, translate=True)
    description = fields.Text("Description")
    active = fields.Boolean(default=True)
    resonsible_id = fields.Many2one(
        "res.users", string="Responsible", ondelete="restrict"
    )
    session_ids = fields.One2many("openacademy.session", "course_id", string="Session")

    _sql_constraints = [("name_unique", "unique(name)", "Name must be unique")]

    @api.constrains("name", "description")
    def _check_name_description(self):
        for record in self:
            if record.name == record.description:
                raise ValidationError("name and description should not be same!!")


class OpenacademySession(models.Model):
    _name = "openacademy.session"
    _description = "Training session"

    @api.depends("partner_ids")
    def _get_attendee_count(self):
        for record in self:
            record.attendee_count = len(record.partner_ids)

    name = fields.Char("Session")
    instructor_id = fields.Many2one(
        "res.partner", string="Instructor", domain=[("instructor", "=", True)]
    )
    seats = fields.Integer("Seats")
    start_date = fields.Date("Start Date", default=fields.Date.today())
    duration = fields.Float("Duration")
    course_id = fields.Many2one("openacademy.course", string="Course")
    partner_ids = fields.Many2many(
        "res.partner",
        "session_partner_rel",
        "session_id",
        "partner_id",
        string="Attendees",
    )
    attendee_count = fields.Integer(
        compute="_get_attendee_count", string="No.of Attendees", store=True
    )
    email = fields.Char("Email", related="instructor_id.email")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirm", "Confirm"),
            ("delay", "Delay"),
            ("cancel", "Cancel"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
    )

    @api.constrains("instructor_id", "partner_ids")
    def _check_instructor_attendee(self):
        for record in self:
            if record.instructor_id and record.instructor_id in record.partner_ids:
                raise ValidationError("Instructor cannot be attendee!!")

    def action_confirm(self):
        print("Context", self.env.context)
        self.write({"state": "confirm"})

    def action_delay(self):
        self.write({"state": "delay"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancel"})


class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean()
    session_ids = fields.Many2many(
        "openacademy.session",
        "session_partner_rel",
        "partner_id",
        "session_id",
        string="Session",
    )
