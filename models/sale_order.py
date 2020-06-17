# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    admin_fee_percentage = fields.Float(
        string='Admin Fee %',
        compute='_get_admin_fee_percentage',
        store=True,
        readonly=False,
    )
    admin_fee = fields.Monetary(
        compute='_get_admin_fee',
        store=True,
    )
    amount_with_admin_fee = fields.Monetary(
        compute='_get_admin_fee',
        store=True,
    )

    @api.depends('partner_id')
    def _get_admin_fee_percentage(self):
        for order in self:
            if not order.admin_fee_percentage:
                order.admin_fee_percentage = order.partner_id.admin_fee_percentage

    @api.depends('admin_fee_percentage', 'amount_total')
    def _get_admin_fee(self):
        for order in self:
            order.admin_fee = order.admin_fee_percentage / 100 * order.amount_total
            order.amount_with_admin_fee = order.amount_total + order.admin_fee
