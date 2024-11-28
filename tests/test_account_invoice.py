# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase


class AccountMove(TransactionCase):
    def prepare_invoice(self, admin_fee_percentage, total):
        partner_id = self.env["res.partner"].search([], limit=1)
        # Cambiando account.invoice por account.move
        invoice_id = self.env["account.move"].create(
            {
                "partner_id": partner_id.id,
                "move_type": "out_invoice",  # Aseguramos que es una factura de cliente
            }
        )
        invoice_id.admin_fee_percentage = admin_fee_percentage
        invoice_id.amount_total = total
        return invoice_id

    def _get_admin_fee_target(self, admin_fee_percentage, total):
        return admin_fee_percentage / 100 * total

    def _get_amount_with_admin_fee_target(self, admin_fee_target, total):
        return total + admin_fee_target

    def test_admin_fee(self):
        admin_fee_percentage = 25
        total = 300
        invoice_id = self.prepare_invoice(admin_fee_percentage, total)
        admin_fee_target = self._get_admin_fee_target(admin_fee_percentage, total)
        amount_with_admin_fee_target = self._get_amount_with_admin_fee_target(
            admin_fee_target, total
        )
        self.assertEqual(invoice_id.admin_fee, admin_fee_target)
        self.assertEqual(invoice_id.amount_with_admin_fee, amount_with_admin_fee_target)
