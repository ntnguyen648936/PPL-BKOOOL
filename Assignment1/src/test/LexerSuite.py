import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # ---------------------------------------------------------------------------------------------------------
    
    def test_stringLit_01(self):
        self.assertTrue(TestLexer.test("""\"What are you doing?\"""","\"What are you doing?\",<EOF>",101))

    def test_stringLit_02(self):
            self.assertTrue(TestLexer.test("""\"What \\x are you doing?\"""","Illegal escape in string: What \\x",102))

    def test_stringLit_03(self):
        self.assertTrue(TestLexer.test("""\"What \\n \\r \\t are you doing?\"""","\"What \\n \\r \\t are you doing?\",<EOF>",103))

    def test_stringLit_04(self):
        self.assertTrue(TestLexer.test("""\"What are you doing?""","Unclosed String: What are you doing?",104))

    def test_stringLit_05(self):
        self.assertTrue(TestLexer.test("""\"Say: \\"What are you doing?\\" \"""","""\"Say: \\"What are you doing?\\" \",<EOF>""",105))

    def test_stringLit_06(self):
        self.assertTrue(TestLexer.test("""\"What \n are you doing?\"""","Unclosed String: What ",106))

    def test_stringLit_07(self):
        self.assertTrue(TestLexer.test("""What are you doing?\"""","What,are,you,doing,ErrorToken ?",107))

    def test_stringLit_08(self):
        self.assertTrue(TestLexer.test("""What are you doing\"""","What,are,you,doing,Unclosed String: ",108))

    # ---------------------------------------------------------------------------------------------------------

    def test_identifier_01(self):
        self.assertTrue(TestLexer.test("abc12d a1bCd","abc12d,a1bCd,<EOF>",131))   
        
    def test_identifier_02(self):
        self.assertTrue(TestLexer.test("ab?cd","ab,ErrorToken ?",132))    

    def test_identifier_03(self):
        self.assertTrue(TestLexer.test("a12b_Dd","a12b_Dd,<EOF>",133))   
    
    def test_identifier_04(self):
        self.assertTrue(TestLexer.test("12abc","12,abc,<EOF>",134))    

    def test_identifier_04(self):
        self.assertTrue(TestLexer.test("12_Abc","12,_Abc,<EOF>",134))    

    # ---------------------------------------------------------------------------------------------------------

    def test_intLit_01(self):
        self.assertTrue(TestLexer.test("1234 0982","1234,0982,<EOF>",111))

    def test_intLit_02(self):
        self.assertTrue(TestLexer.test("1234-0982","1234,-,0982,<EOF>",112))

    def test_intLit_03(self):
        self.assertTrue(TestLexer.test("1234 abcd 0982","1234,abcd,0982,<EOF>",113))
    
    # ---------------------------------------------------------------------------------------------------------

    def test_floatLit_01(self):
        self.assertTrue(TestLexer.test("12.2342 12.","12.2342,12.,<EOF>",121))

    def test_floatLit_02(self):
        self.assertTrue(TestLexer.test("1e-0982 1E-0982 1e+0982 1E+0982","1e-0982,1E-0982,1e+0982,1E+0982,<EOF>",122))

    def test_floatLit_03(self):
        self.assertTrue(TestLexer.test("123.4E+5678 123.4e+5678 123.4E-5678 123.4e-5678","123.4E+5678,123.4e+5678,123.4E-5678,123.4e-5678,<EOF>",123))
    
    def test_floatLit_04(self):
        self.assertTrue(TestLexer.test("12.E+3 12.e+3 12.E-3 12.e-3","12.E+3,12.e+3,12.E-3,12.e-3,<EOF>",124))

    def test_floatLit_05(self):
        self.assertTrue(TestLexer.test(".4E+5678",".,4E+5678,<EOF>",125))

    def test_floatLit_06(self):
        self.assertTrue(TestLexer.test("1.E","1.,E,<EOF>",126))

    def test_floatLit_07(self):
        self.assertTrue(TestLexer.test("1.E+","1.,E,+,<EOF>",127))

    def test_floatLit_08(self):
        self.assertTrue(TestLexer.test("1.e+e","1.,e,+,e,<EOF>",128))

    def test_floatLit_09(self):
        self.assertTrue(TestLexer.test("1.e?3","1.,e,ErrorToken ?",129))

    # ---------------------------------------------------------------------------------------------------------

    def test_comment_01(self):
        self.assertTrue(TestLexer.test(
"""
/* This is a block comment:
# line 
# line
*/
"""
    ,"<EOF>",141))

    def test_comment_02(self):
        self.assertTrue(TestLexer.test(
"""
/* This is a block comment:
line 
/* inside block */
line
*/"""
    ,"line,*,/,<EOF>",142))

    def test_comment_03(self):
        self.assertTrue(TestLexer.test(
"""
/* This is a block comment:
line 
/* inside block
"""
    ,"/,*,This,is,a,block,comment,ErrorToken :",143))

    def test_comment_04(self):
        self.assertTrue(TestLexer.test(
"""
# This is a line comment
"""
    ,"<EOF>",144))

    def test_comment_05(self):
        self.assertTrue(TestLexer.test(
"""
# This is a line comment /* block */
"""
    ,"<EOF>",145))

    def test_comment_06(self):
        self.assertTrue(TestLexer.test(
"""
# This is a line comment /* block
comment */
"""
    ,"comment,*,/,<EOF>",146))

    def test_comment_07(self):
        self.assertTrue(TestLexer.test(
"""
## This is a line comment !@#!@!#@132_() \\t \t \f \\z # and 
"""
    ,"<EOF>",147))



    def test_expression_01(self):
        self.assertTrue(TestLexer.test("int a = 1, b = 2","int,a,=,1,,,b,=,2,<EOF>",151))

    def test_expression_02(self):
        self.assertTrue(TestLexer.test("_a:=1.2\\5e-1","_a,:=,1.2,\\,5e-1,<EOF>",152))