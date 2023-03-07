{
    "name": "LMS",
    "description": """
      LMS stands for library management system.""",
    "depends": ["base", "hr"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/lms_views.xml",
        "reports/reports_test.xml",
    ],
    "installable": "True",
    "license": "LGPL-3",
}
