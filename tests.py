from unittest import TestCase
from katabank import ocrMachine


class TestKataBank(TestCase):
    def test_foo(self):
        self.assertTrue(True)

    def test_digit1(self):
        digitOne = "   \n  |\n  |\n   "
        self.assertEquals(ocrMachine(digitOne),1)

    def test_digit2(self):
        digit_two = " _ \n _|\n|_ \n   "
        self.assertEqual(ocrMachine(digit_two), 2)

    def test_digit3(self):
        digit_three = " _ \n _|\n _|\n   "
        self.assertEquals(ocrMachine(digit_three), 3)


    def test_digits12(self):
        digits_12 = "    _ \n  | _|\n  ||_ \n      "
        self.assertEquals(ocrMachine(digits_12), 12)

    def test_wholestring(self):
        s = "    _  _     _  _  _  _  _ \n" \
          + "  | _| _||_||_ |_   ||_||_|\n" \
          + "  ||_  _|  | _||_|  ||_| _|\n" \
          + "                           "
        self.assertEquals(ocrMachine(s), 123456789)
