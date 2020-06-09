# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase


class SaleOrder(TransactionCase):

    def prepare_order(self, admin_fee_percentage, total):
        partner_id = self.env['res.partner'].search([], limit=1)
        product_id = self.env['product.product'].search([], limit=1)
        order_id = self.env['sale.order'].create({
            'partner_id': partner_id.id,
        })
        order_id.admin_fee_percentage = admin_fee_percentage
        self.env['sale.order.line'].create({
            'product_id': product_id.id,
            'price_unit': total,
            'product_uom_qty': 1,
            'order_id': order_id.id,
        })
        return order_id

    def _get_admin_fee_target(self, admin_fee_percentage, total):
        return admin_fee_percentage / 100 * total

    def _get_amount_with_admin_fee_target(self, admin_fee_target, total):
        return total + admin_fee_target

    def test_admin_fee(self):
        admin_fee_percentage = 25
        total = 300
        order_id = self.prepare_order(admin_fee_percentage, total)
        admin_fee_target = self._get_admin_fee_target(admin_fee_percentage, total)
        amount_with_admin_fee_target = self._get_amount_with_admin_fee_target(admin_fee_target, total)
        self.assertEqual(order_id.admin_fee, admin_fee_target)
        self.assertEqual(order_id.amount_with_admin_fee, amount_with_admin_fee_target)
