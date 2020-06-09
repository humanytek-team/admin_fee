# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    admin_fee_percentage = fields.Float(
        string='Admin Fee %',
    )
