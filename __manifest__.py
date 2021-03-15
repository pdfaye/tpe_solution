# -*- coding: utf-8 -*-
{
    'name': "TPE SOLUTION",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'crm',
                'website',
                'website_sale',
                'website_mail',
                'website_profile',
                'website_rating',
                'mail',
                'mail_preview_base',
                "web_drop_target",
                "http_routing",
                'sale',
                'stock',
                'purchase',
                'digest',
                'hr',
                'account',
                'l10n_syscohada',
                'contacts',
                'mass_mailing',
                'mass_mailing_sms',
                'project',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        # 'views/tpe_achat.xml',
        # 'views/tpe_vente.xml',
        # 'views/tpe_comptabilite.xml',
        # 'views/tpe_crm.xml',
        # 'views/tpe_ecommerce.xml',
        # 'views/tpe_employe.xml',
        # 'views/tpe_marketting.xml',
        # 'views/tpe_paie.xml',
        # 'views/tpe_rh.xml',
        # 'views/tpe_stock.xml',
        'views/configuration.xml',
        'views/tp_accueil.xml',

        ],
    'demo': [
         'demo/demo.xml',
        ],
    'qweb': [
        'static/src/xml/attachment_action.xml',
        ],
    'installable': True,
    'application': True,
    'auto_install': False
}
