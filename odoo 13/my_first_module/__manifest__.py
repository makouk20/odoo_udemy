# -*- coding: utf-8 -*-
{
    'name': "my_first_module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Turki Maki",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/car.xml',
        'views/parking.xml',
        'views/sequence.xml',
        'views/security.xml',
        'views/rules.xml',
        #  'views/res_partner_inherit_form_view.xml',
    ],
    # only loaded in demonstration mode

}
