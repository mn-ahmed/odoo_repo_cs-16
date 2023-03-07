{
    "name": "OpenAcademy",
    "author": "Odoo S.a",
    "website": "odoo.com",
    "category": "Tools",
    "description": """
OpenAcademy
==============================
Training Course
Training Session
Training Attendee
    """,
    "depends": ["base", "sale", "mail"],
    "data": [
        "report/report_openacademy_template.xml",
        "wizard/openacademy_wizard_view.xml",
        "views/openacademy_views.xml",
        "views/res_partner_inherit_views.xml",
        "security/openacademy_security.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
