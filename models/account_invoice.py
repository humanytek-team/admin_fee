# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    admin_fee_percentage = fields.Float(
        string='Admin Fee %',
        compute='_get_admin_fee_percentage',
        store=True,
        readonly=False,
    )

    @api.onchange('partner_id')
    def _get_admin_fee_percentage(self):
        for order in self:
            order.admin_fee_percentage = order.partner_id.admin_fee_percentage
