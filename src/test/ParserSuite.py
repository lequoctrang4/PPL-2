import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """
                main: function void() {
                        if ((a == true) || (b)) {}
                        return 0;
}
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
