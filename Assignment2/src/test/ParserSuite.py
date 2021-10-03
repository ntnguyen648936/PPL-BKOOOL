import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = r"""
        class main {
            final static boolean[3] a = {true,false,true};
            int[2] b = {1,2};
            final string[1] c = {"hello"}, d = {"world"};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_simple_program_02(self):
        input = r"""
        class main {
            float a = b * ((c \ d) / e) % f;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_simple_program_03(self):
        input = r"""
        class main {
            int a = !--new A(10.0E-1++new B());
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
