from odoo import models, fields


class author(models.Model):
    _name = "book.author"
    _description = "Author"

    name = fields.Char()
    address = fields.Char()


class bookCategory(models.Model):
    _name = "book.category"
    _description = "Book Category"

    name = fields.Char(string="Book Name")


class bookDepartment(models.Model):
    _name = "book.department"
    _description = "Book Department"

    name = fields.Char(string="Book Department Name")


class bookPublisher(models.Model):
    _name = "book.publisher"
    _description = "Book Publisher"

    name = fields.Char(string="Book Publisher Name")


class rack(models.Model):
    _name = "book.rack"
    _description = "Rack"

    name = fields.Char(string="Rack Name")
    shelf_ids = fields.One2many("book.shelf", "rack_id", string="Shelf")


class Shelf(models.Model):
    _name = "book.shelf"
    _description = "Shelf"

    name = fields.Char(string="Shelf Name")
    rack_id = fields.Many2one("book.rack")


class books(models.Model):
    _name = "book.books"
    _description = "Books Table"
    _sql_constraints = [("isbn_unique", "unique(isbn)", "ISBN must be unique.")]

    price = fields.Float()
    author_ids = fields.Many2many("book.author")
    category_ids = fields.Many2one("book.category")
    department = fields.Many2one("book.department")
    barcode = fields.Char()
    publisher_id = fields.Many2one("book.publisher")
    edition = fields.Char()
    date = fields.Date()
    shelf_id = fields.Many2one("book.shelf")
    isbn = fields.Integer()
