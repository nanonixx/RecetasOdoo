# -*- coding: utf-8 -*-
{
    'name': "recetas",

    'summary': """
        Módulo para gestionar recetingas""",

    'description': """
        Aquí está toda la información sobre recetas de cocina y cosingas relacionadas con esta. Se pueden hacer cosas con estas cosingas
    """,

    'author': "Naomi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
     # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
