# -*- coding: utf-8 -*-
{
    "name": "Admin Fee",
    "version": "17.0.1.3.2",
    "author": "Humanytek",
    "website": "https://github.com/humanytek-team/admin_fee",
    "depends": [
        "account_accountant",
        "sale_management",
    ],
    "data": [
        # security
        # data
        # reports
        "reports/account_move.xml",
        "reports/sale_order.xml",
        # views
        "views/account_move.xml",
        "views/res_partner.xml",
        "views/sale_order.xml",
    ],
    "installable": True,
    "application": False,
}
