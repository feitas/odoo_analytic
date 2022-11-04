{
    'name': 'ODOO Analytic Advanced Extension',
    'version': '14.0',
    'author': '潍坊飞塔思信息科技有限公司',
    'website': 'https://www.wffeitas.com',
    'category': 'Accounting/Accounting',
    'depends': ['base', 'mail', 'analytic', 'account'],
    'description': """
Module for odoo analytic accounting cost.
===============================================

    """,
    'data': [
        'security/ir.model.access.csv',
        'views/account_analytic_default_view_ext.xml',
        'views/account_analytic_line_ext_view.xml',
        'views/analytic_account_group_views_ext.xml',
        'views/field_config_table_view.xml',
        'views/account_analytic_month_view.xml',
        'views/account_analytic_version_view.xml',
        'views/account_menuitem.xml',
    ],
    'demo': [
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
