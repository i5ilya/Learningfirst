from unittest import TestCase, main
from calc_for_tests import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('4-1'), 3)

    def test_mult(self):
        self.assertEqual(calculator('5*20'), 100)

    def test_div(self):
        self.assertEqual(calculator('100/2'), 50)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотябы один знак +-/*', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*6')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*6/3')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.0+3.2')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a/b')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])


if __name__ == '__main__':
    main()
