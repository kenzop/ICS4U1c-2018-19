import unittest
import stringlib


class Test_lengths(unittest.TestCase):
    def test_strLength_general1(self):
        self.assertEquals(5, stringlib.strLength("hello"))

    def test_strLength_general2(self):
        self.assertEquals(11, stringlib.strLength("Sub 2 Pewds"))
