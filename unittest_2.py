from unittest import TestCase, main

from fib import fib


class TestFibonacci(TestCase):
    def test_simple(self):
        for param, result in [(0, 0), (1, 1), (3, 2), (10, 55)]:
            self.assertEqual(fib(param), result)

    def test_stress(self):
        self.assertEqual(fib(29), (fib(27) + fib(28)))
        with self.assertRaises(ValueError):
            fib(30)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-100)

    def test_wrong_param_type(self):
        with self.assertRaises(TypeError):
            fib("Hello")
        with self.assertRaises(TypeError):
            fib(2.5)


if __name__ == "__main__":
    main()
