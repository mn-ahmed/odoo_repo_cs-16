from odoo import models, fields, api
from odoo.exceptions import UserError, Warning


class Test(models.Model):
    _name = "test"
    _description = "Test"

    data = fields.Char(string="Data")
    pincode = fields.Integer(string="Pincode")

    def name_get(self):
        return [(r.id, r.data) for r in self]


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _order = "price desc"

    price = fields.Float(string="Price")
    status = fields.Selection([("available", "Available"), ("refused", "Refused")])
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")

    def action_refuse(self):
        for record in self:
            record.status = "refused"

    def action_accept(self):
        for record in self:
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type"

    name = fields.Char(string="Name")
    property_ids = fields.One2many("estate.property", "property_type_id")


class estatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag"

    name = fields.Char(string="Name")
    color = fields.Integer()


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = "id desc"

    name = fields.Char(string="Title", default="Unknown", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availibiliaty = fields.Date(
        default=lambda self: fields.Datetime.now(), copy=False
    )
    expected_price = fields.Float()
    selling_price = fields.Float(copy=False)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [("north", "North"), ("east", "East"), ("south", "South"), ("west", "West")]
    )
    active = fields.Boolean(default=True)
    image = fields.Image()
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.users", string="Salesman")
    buyer_id = fields.Many2one("res.partner", string="partner")
    test_id = fields.Many2one("test")
    property_tag_id = fields.Many2many("estate.property.tag", string="Property Tag")
    property_offer_ids = fields.One2many(
        "estate.property.offer", "property_id", string="Property Offer"
    )
    total_area = fields.Integer(compute="_compute_area", inverse="_inverse_area")
    best_price = fields.Float(compute="_compute_best_price", store=True)
    state = fields.Selection(
        [("new", "New"), ("sold", "Sold"), ("cancelled", "Cancelled")], default="new"
    )

    @api.depends("living_area", "garden_area")
    def _compute_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("property_offer_ids")
    def _compute_best_price(self):
        for record in self:
            max_price = 0
            for offer in record.property_offer_ids:
                if offer.price > max_price:
                    max_price = offer.price
            record.best_price = max_price

    def _inverse_area(self):
        for record in self:
            record.living_area = record.garden_area = record.total_area / 2

    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_orientation = None
                record.garden_area = 0

    def action_sold(self):
        print("  ACTION SOLD.  ")
        for record in self:
            if record.state == "cancel":
                raise UserError("Cancel Property cannot be sold.")
            record.state = "sold"

    def action_cancel(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Sold Property cannot be cancelled.")
            record.state = "cancelled"
