from odoo import models, fields, api
from odoo.exceptions import ValidationError


class lmsbooks(models.Model):
    _name = "lms.books"
    _description = "Book Master"

    name = fields.Char("Book Name")
    genre_id = fields.One2many("lms.genres", "genre_id", string="Genre")
    author_id = fields.Many2one("lms.authors", string="Author")
    isbn = fields.Char(string="ISBN")
    isbn_com = fields.Float(string="ISBN-com", compute="_inc10")

    def _inc10(self):
        # pass
        for record in self:
            record.isbn_com = str(int(record.isbn) * 100)


class authors(models.Model):
    _name = "lms.authors"
    _description = "Author Master"

    name = fields.Char("Author Name")
    address = fields.Char("Address")
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    # books_id = fields.One2many('books', 'author_id', string="Books")


class genres(models.Model):
    _name = "lms.genres"
    _description = "Genre"

    name = fields.Char("Genre")
    genre_id = fields.Many2one("lms.books", string="Book")


class users(models.Model):
    _name = "lms.users"
    _description = "User"

    name = fields.Char("Users Name")
    email = fields.Char("Email")


class library_employees(models.Model):
    _name = "lms.library_employees"
    _inherit = "hr.employee"
    _description = "Employee"

    hobbies = fields.Selection(
        [
            ("cricket", "Cricket"),
            ("football", "Football"),
            ("hockey", "Hockey"),
            ("chess", "Chess"),
            ("reading", "Reading"),
            ("swimming", "Swimming"),
            ("others", "Others"),
        ],
        string="Hobbies",
    )

    category_ids = fields.Many2many(
        "hr.employee.category", "library_rel", "emp_id", "category_id", string="Tags"
    )


class library_employees_inherit(models.Model):
    _inherit = "hr.employee"
    _description = "Employee Inherit"

    car_color = fields.Char(string="Car Color")
