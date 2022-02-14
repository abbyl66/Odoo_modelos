# -*- coding: utf-8 -*-
{
    'name': "odoo51y",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
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
        'security/odoo51y_security.xml',
        'security/ir.model.access.csv',
        'report/odoo51y_modelo51y_report.xml',
        'report/odoo51y_autores51y_report.xml',
        'report/odoo51y_editoriales51y_report.xml',
        'report/odoo51y_generos_report.xml',
        'report/odoo51y_librosgratis_report.xml',
        'report/odoo51y_librospago_report.xml',
        'report/odoo51y_librospremiados_report.xml',
        'report/odoo51y_librosvendidos_report.xml',
        'report/odoo51y_sagas_report.xml',
        'report/odoo51y_trilogias_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
