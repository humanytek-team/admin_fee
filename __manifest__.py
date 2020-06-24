# -*- coding: utf-8 -*-
{
    'name': 'Admin Fee',
    'version': '1.2.2',
    'author': 'Humanytek',
    'website': 'https://github.com/humanytek-team/admin_fee',
    'depends': [
        'account',
        'sale',
    ],
    'data': [
        # security
        # data
        # reports
        'reports/account_invoice.xml',
        'reports/sale_order.xml',
        # views
        'views/account_invoice.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
}
