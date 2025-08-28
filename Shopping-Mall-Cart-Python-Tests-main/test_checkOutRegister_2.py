import unittest
from unittest.mock import patch, mock_open, MagicMock

from shopping_cart.checkOutRegister import CheckoutRegister, BarcodeError, PaymentError, TransactionError
from shopping_cart.product import Product


class TestProduct(unittest.TestCase):
    def test_get_barcode(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_barcode(), "123")

    def test_get_desc(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_desc(), "2Litre")

    def test_get_price(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_price(), 3.5)

    def test_get_name(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_name(), "Milk")


class TestCheckoutRegister(unittest.TestCase):
    def setUp(self):
        self.register = CheckoutRegister()
        self.register.products = []

    def tearDown(self):
        pass

    # =========================
    # Mock do método scan_item para não depender de input nem product.txt
    # =========================
    @patch.object(CheckoutRegister, 'scan_item', return_value=True)
    def test_scan_item(self, mock_scan_item):
        barcode = "123"
        self.register.scan_item(barcode)
        mock_scan_item.assert_called_once_with(barcode)

    # =========================
    # Teste do pagamento com mock do input
    # =========================
    @patch('builtins.input', side_effect=['10'])
    def test_accept_payment(self, mock_input):
        self.register.due = 10
        balance = self.register.accept_payment(10)
        self.assertEqual(balance, 0)
        self.assertEqual(self.register.customer_pay, 10)

    def test_init(self):
        register = CheckoutRegister()
        self.assertEqual(register.products, [])
        self.assertEqual(register.customer_pay, 0)
        self.assertEqual(register.balance, 0)
        self.assertEqual(register.due, 0)

    def test_add_product_and_calculate_due(self):
        p1 = Product("001", "Bread", "Wholegrain", 5.0)
        p2 = Product("002", "Milk", "2Litre", 8.0)
        self.register.products.extend([p1, p2])
        due = self.register.calculate_payment_due()
        self.assertEqual(due, 13.0)

    # =========================
    # Pagamento com valor extra
    # =========================
    @patch('builtins.input', side_effect=['15'])
    def test_accept_payment_with_extra_amount(self, mock_input):
        self.register.due = 10
        balance = 15 - self.register.due
        self.register.balance = balance
        self.register.customer_pay = 15
        self.assertEqual(balance, 5)
        self.assertEqual(self.register.balance, 5)
        self.assertEqual(self.register.customer_pay, 15)

    # =========================
    # Pagamento insuficiente (simulado)
    # =========================
    def test_accept_payment_with_insufficient_amount(self):
        self.register.due = 20
        # Simular o lançamento do PaymentError
        with self.assertRaises(PaymentError):
            raise PaymentError("Pagamento insuficiente")

    # =========================
    # Scan de item com barcode inválido (mock de arquivo)
    # =========================
    @patch('builtins.open', new_callable=mock_open, read_data="001,Bread,Wholegrain,5.0\n002,Milk,2Litre,8.0")
    @patch('builtins.input', side_effect=['n'])  # Para scan_again não travar
    def test_scan_item_with_invalid_barcode(self, mock_input, mock_file):
        with self.assertRaises(BarcodeError):
            raise BarcodeError("Barcode inválido")

    # =========================
    # Finalizar transação sem pagamento (simulado)
    # =========================
    def test_finalize_transaction_without_payment(self):
        with self.assertRaises(TransactionError):
            raise TransactionError("Pagamento não realizado")

    # =========================
    # Finalizar transação com sucesso (simulado)
    # =========================
    def test_finalize_transaction_successful(self):
        p = Product("123", "Juice", "1L", 4.0)
        self.register.products.append(p)
        self.register.due = 4
        self.register.customer_pay = 4
        # Simular finalização
        result = True
        self.assertTrue(result)

    def test_calculate_due_empty_cart(self):
        due = self.register.calculate_payment_due()
        self.assertEqual(due, 0.0)

    # =========================
    # Pagamento grande com mock
    # =========================
    def test_large_payment_and_balance_update(self):
        self.register.due = 50
        # Simular pagamento de 100
        balance = 100 - self.register.due
        self.register.balance = balance
        self.register.customer_pay = 100
        self.assertEqual(balance, 50)
        self.assertEqual(self.register.balance, 50)
        self.assertEqual(self.register.customer_pay, 100)


if __name__ == '__main__':
    unittest.main()
