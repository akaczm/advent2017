import unittest
from day1.day1 import solve_captcha

class Day1TestCase(unittest.TestCase):

    def test_captcha_part1(self):
        assert solve_captcha(1122) == 3
        assert solve_captcha(1111) == 4
        assert solve_captcha(1234) == 0
        assert solve_captcha(91212129) == 9

    def test_captcha_part2(self):
        assert solve_captcha(1212, "mids") == 6
        assert solve_captcha(1122, "mids") == 0
        assert solve_captcha(123425, "mids") == 4
        assert solve_captcha(123123, "mids") == 12
        assert solve_captcha(12131415, "mids") == 4