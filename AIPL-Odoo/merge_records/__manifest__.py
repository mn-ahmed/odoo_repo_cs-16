# -*- coding: utf-8 -*-
{
    'name': "Merge Records",

    'summary': """
        Merge Records:
        Can Be used to merge records in Sales App.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "APP INfoweb Pvt Ltd",
    'website': "https://www.appinfoweb.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
