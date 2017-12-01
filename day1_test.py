import unittest
from day1.day1 import solve_captcha

class Day1TestCase(unittest.TestCase):

    def test_captcha(self):
        assert solve_captcha(1122) == 3
        assert solve_captcha(1111) == 4
        assert solve_captcha(1234) == 0
        assert solve_captcha(91212129) == 9
