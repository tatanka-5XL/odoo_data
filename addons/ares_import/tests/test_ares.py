from odoo.tests.common import TransactionCase

class TestAresImport(TransactionCase):

    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Test Firma',
            'vat': 'CZ06635482',
        })

    def test_action_fetch_ares_data(self):
        self.partner.action_fetch_ares_data()
        # assert company name is updated
        self.assertNotEqual(self.partner.name, 'Test Firma')
        self.assertTrue(len(self.partner.name) > 0)
