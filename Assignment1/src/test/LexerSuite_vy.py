import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    """WhitespaceTest"""
    def test_ws1(self):
        self.assertTrue(TestLexer.test("Blank space here   .All of", "Blank,space,here,.,All,of,<EOF>", 101))

    def test_ws2(self):
        self.assertTrue(TestLexer.test("this \t will", "this,will,<EOF>", 102))

    def test_ws3(self):
        self.assertTrue(TestLexer.test("be \f skipped", "be,skipped,<EOF>", 103))

    def test_ws4(self):
        self.assertTrue(TestLexer.test("also \r this", "also,this,<EOF>", 104))

    def test_ws5(self):
        self.assertTrue(TestLexer.test("and \n this", "and,this,<EOF>", 105))

    """test comment"""
    def test_block_comment(self):
        self.assertTrue(TestLexer.test("""/* This is a block comment, 
        that may span in many lines*/""", "<EOF>", 106))

    def test_line_comment(self):
        self.assertTrue(TestLexer.test("#This is a line comment", "<EOF>", 107))

    def test_line_comment_with_statement(self):
        self.assertTrue(TestLexer.test("a := 5;#this is a line comment", "a,:=,5,;,<EOF>", 108))

    def test_nested_block_comment(self):
        self.assertTrue(TestLexer.test("/* This is a block comment so # has no meaning here */", "<EOF>", 109))

    def test_nested_line_comment(self):
        self.assertTrue(TestLexer.test("#This is a line comment so /* has no meaning here", "<EOF>", 110))

    def test_two_line_comment_in_a_single_line(self):
        self.assertTrue(TestLexer.test("#This is a comment #This is another comment", "<EOF>", 111))

    """test id"""
    def test_one_letter_id(self):
        self.assertTrue(TestLexer.test("a", "a,<EOF>", 112))

    def test_one_underscore_id(self):
        self.assertTrue(TestLexer.test("_", "_,<EOF>", 113))

    def test_lowercase_id(self):
        self.assertTrue(TestLexer.test("lowercase", "lowercase,<EOF>", 114))

    def test_uppercase_id(self):
        self.assertTrue(TestLexer.test("UPPERCASE", "UPPERCASE,<EOF>", 115))

    def test_valid_id_start_with_underscore(self):
        self.assertTrue(TestLexer.test("_This_Is_Valid_ID_0123", "_This_Is_Valid_ID_0123,<EOF>", 116))

    def test_valid_id_start_with_a_letter(self):
        self.assertTrue(TestLexer.test("this_Is_Valid_ID_0123___", "this_Is_Valid_ID_0123___,<EOF>", 117))

    def test_wrong_id_token(self):
        self.assertTrue(TestLexer.test("aA123?sVN", "aA123,Error Token ?", 118))

    """test keyword"""
    def test_all_keyword(self):
        self.assertTrue(TestLexer.test(
            "boolean break class continue do else extends float if int new string then for return true false void nil "
            "this final static to downto",
            "boolean,break,class,continue,do,else,extends,float,if,int,new,string,then,for,return,true,false,void,"
            "nil,this,final,static,to,downto,<EOF>",
            119))

    """test operator"""
    def test_operator_add_sub(self):
        self.assertTrue(TestLexer.test("x+34-y", "x,+,34,-,y,<EOF>", 120))

    def test_operator_mul(self):
        self.assertTrue(TestLexer.test("99x*11y", "99,x,*,11,y,<EOF>", 121))

    def test_operator_fdiv_idiv_mod(self):
        self.assertTrue(TestLexer.test("a/b\\c%d", "a,/,b,\\,c,%,d,<EOF>", 122))

    def test_operator_noe(self):
        self.assertTrue(TestLexer.test("4!=5 ", "4,!=,5,<EOF>", 123))

    def test_operator_eq(self):
        self.assertTrue(TestLexer.test("a == b", "a,==,b,<EOF>", 124))

    def test_operator_less(self):
        self.assertTrue(TestLexer.test("x < x + 1", "x,<,x,+,1,<EOF>", 125))

    def test_operator_greater(self):
        self.assertTrue(TestLexer.test("x > 2", "x,>,2,<EOF>", 126))

    def test_operator_lessoe(self):
        self.assertTrue(TestLexer.test("x<= x+y", "x,<=,x,+,y,<EOF>", 127))

    def test_operator_greateroe(self):
        self.assertTrue(TestLexer.test("a>=b+c", "a,>=,b,+,c,<EOF>", 128))

    def test_operator_or_and(self):
        self.assertTrue(TestLexer.test("true || false && true", "true,||,false,&&,true,<EOF>", 129))

    def test_operator_concat(self):
        self.assertTrue(TestLexer.test("string1 ^ string2", "string1,^,string2,<EOF>", 130))

    def test_operator_not(self):
        self.assertTrue(TestLexer.test("!true = false", "!,true,=,false,<EOF>", 131))

    """test separator"""
    def test_all_separator(self):
        self.assertTrue(
            TestLexer.test("{[(a-2)*b]/c;e:d,f,g}", "{,[,(,a,-,2,),*,b,],/,c,;,e,:,d,,,f,,,g,},<EOF>", 132))

    """test literal"""
    """test integer"""
    def test_integer_with_id(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 133))

    def test_integer_without_id(self):
        self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 134))

    def test_integer_with_comment(self):
        self.assertTrue(TestLexer.test("123#this is a comment", "123,<EOF>", 135))

    def test_integer_with_block_comment(self):
        self.assertTrue(TestLexer.test("456/*skip this part*/", "456,<EOF>", 136))

    def test_integer_with_operator(self):
        self.assertTrue(TestLexer.test("123-3=240/2", "123,-,3,=,240,/,2,<EOF>", 137))

    def test_integer_with_separator(self):
        self.assertTrue(TestLexer.test("{[(4-2)*12]/9;12:3,5,7}",
                                       "{,[,(,4,-,2,),*,12,],/,9,;,12,:,3,,,5,,,7,},<EOF>", 138))

    """test float"""
    def test_float_with_decimal_part(self):
        self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 139))

    def test_float_without_decimal_part(self):
        self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 140))

    def test_float_with_exponent_part(self):
        self.assertTrue(TestLexer.test("123e-8", "123e-8,<EOF>", 141))

    def test_valid_float_with_e_without_dot_and_sub(self):
        self.assertTrue(TestLexer.test("123e8", "123e8,<EOF>", 142))

    def test_valid_float_with_e_and_dot_and_sub(self):
        self.assertTrue(TestLexer.test("1.2e-2", "1.2e-2,<EOF>", 143))

    def test_valid_float_with_e_and_dot_and_plus(self):
        self.assertTrue(TestLexer.test("2.1e+2", "2.1e+2,<EOF>", 144))

    def test_valid_float_both_side_number_with_E_without_dot_and_sub(self):
        self.assertTrue(TestLexer.test("1E2", "1E2,<EOF>", 145))

    def test_valid_float_both_side_number_with_E_and_dot_and_sub(self):
        self.assertTrue(TestLexer.test("1.2E-2", "1.2E-2,<EOF>", 146))

    def test_valid_float_only_left_side_number_with_E_and_plus(self):
        self.assertTrue(TestLexer.test("1.1E+2", "1.1E+2,<EOF>", 147))

    def test_valid_float_next_to_an_identifier(self):
        self.assertTrue(TestLexer.test("1.12e12 _thisisID", "1.12e12,_thisisID,<EOF>", 148))

    def test_many_float(self):
        self.assertTrue(TestLexer.test("9.0 12e8 1. 0.33E-3 128e+42", "9.0,12e8,1.,0.33E-3,128e+42,<EOF>", 149))

    def test_invalid_float(self):
        self.assertTrue(TestLexer.test(".12143e", ".,12143,e,<EOF>", 150))

    """test boolean"""
    def test_booleanlit(self):
        self.assertTrue(TestLexer.test("true and false", "true,and,false,<EOF>", 151))

    """test string"""
    def test_valid_string(self):
        self.assertTrue(TestLexer.test(""" "This is a valid string 123456" """,
                                       """This is a valid string 123456,<EOF>""", 152))

    def test_string_with_only_letter(self):
        self.assertTrue(TestLexer.test(""" "Valid string without numbers" """,
                                       """Valid string without numbers,<EOF>""", 153))

    def test_string_with_only_number(self):
        self.assertTrue(TestLexer.test(""" "1234567890" """, """1234567890,<EOF>""", 154))

    def test_string_with_special_char(self):
        self.assertTrue(TestLexer.test(""" "Valid string with special characters !@#!@#!$@#$" """,
                                       """Valid string with special characters !@#!@#!$@#$,<EOF>""", 155))

    def test_string_with_whitespace(self):
        self.assertTrue(TestLexer.test(""" "    " """, """    ,<EOF>""", 156))

    def test_empty_string(self):
        self.assertTrue(TestLexer.test(""" "" """, """,<EOF>""", 157))

    def test_valid_string_with_tab(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t in it" """,
                                       """This is a string containing tab \\t in it,<EOF>""", 158))

    def test_example_valid_string(self):
        self.assertTrue(TestLexer.test(""" "He asked me: "Where is John?"" """,
                                       """He asked me: "Where is John?",<EOF>""", 159))

    def test_middle_illegal_esc_string(self):
        self.assertTrue(TestLexer.test(""" "String with ill_esc in middle \\a like this" """,
                                       """Illegal Escape In String: String with ill_esc in middle \\a""", 160))

    def test_beginning_illegal_esc_string(self):
        self.assertTrue(TestLexer.test(""" "\\string with ill_esc at beginning" """,
                                       """Illegal Escape In String: \\s""", 161))

    def test_end_illegal_esc_string(self):
        self.assertTrue(TestLexer.test(""" "This string ends with an ill_esc \\z" """,
                                       """Illegal Escape In String: This string ends with an ill_esc \\z""", 162))

    def test_unclosed_string_without_end_quote(self):
        self.assertTrue(TestLexer.test(""" "123a123abc """, """Unclosed String: 123a123abc """, 163))

    def test_unclose_string_with_newline(self):
        self.assertTrue(TestLexer.test(""" "123a\\n123 """, """Unclosed String: 123a\\n123 """, 164))

    def test_valid_string_with_a_slash(self):
        self.assertTrue(TestLexer.test(""" "alo__ "a\\t123"" """, """alo__ "a\\t123",<EOF>""", 165))

    def test_double_slash(self):
        self.assertTrue(TestLexer.test(""" 123 "123a\\\\123" """, """123,123a\\\\123,<EOF>""", 166))

    """test array literal"""
    def test_integer_arraylit(self):
        self.assertTrue(TestLexer.test("{1, 2, 3}", "{,1,,,2,,,3,},<EOF>", 167))

    def test_float_arraylit(self):
        self.assertTrue(TestLexer.test("{2.3, 4.2, 102e3}", "{,2.3,,,4.2,,,102e3,},<EOF>", 168))

    def test_bool_arraylit(self):
        self.assertTrue(TestLexer.test("{true, false}", "{,true,,,false,},<EOF>", 169))

    def test_string_arraylit(self):
        self.assertTrue(TestLexer.test("{""""string"""", """"array""""}", "{,string,,,array,},<EOF>", 170))

    """test datatype"""
    def test_primitive_data_type(self):
        self.assertTrue(TestLexer.test("int float boolean string", "int,float,boolean,string,<EOF>", 171))

    def test_int_data_type(self):
        self.assertTrue(TestLexer.test("int", "int,<EOF>", 172))

    def test_float_data_type(self):
        self.assertTrue(TestLexer.test("float", "float,<EOF>", 173))

    def test_boolean_data_type(self):
        self.assertTrue(TestLexer.test("boolean", "boolean,<EOF>", 174))

    def test_string_data_type(self):
        self.assertTrue(TestLexer.test("string", "string,<EOF>", 175))

    def test_void_data_type(self):
        self.assertTrue(TestLexer.test("void", "void,<EOF>", 176))

    def test_array_int_data_type(self):
        self.assertTrue(TestLexer.test("int[5] a", "int[5],a,<EOF>", 177))

    def test_array_float_data_type(self):
        self.assertTrue(TestLexer.test("float[1] a", "float[1],a,<EOF>", 178))

    def test_array_boolean_data_type(self):
        self.assertTrue(TestLexer.test("boolean[2] a", "boolean[2],a,<EOF>", 179))

    def test_array_string_data_type(self):
        self.assertTrue(TestLexer.test("string[3] a", "string[3],a,<EOF>", 180))

    """test stmt"""
    def test_assignment_sign(self):
        self.assertTrue(TestLexer.test("a=b", "a,=,b,<EOF>", 181))

    def test_other_assignment_sign(self):
        self.assertTrue(TestLexer.test("a:=b", "a,:=,b,<EOF>", 182))

    def test_if_else_then_token(self):
        self.assertTrue(TestLexer.test("if a then b else c", "if,a,then,b,else,c,<EOF>", 183))

    def test_for_to_token(self):
        self.assertTrue(TestLexer.test("for a := 1 to 5 do b", "for,a,:=,1,to,5,do,b,<EOF>", 184))

    def test_for_downto_token(self):
        self.assertTrue(TestLexer.test("for a := 1 downto 5 do b", "for,a,:=,1,downto,5,do,b,<EOF>", 185))

    def test_break_token(self):
        self.assertTrue(TestLexer.test("break;", "break,;,<EOF>", 186))

    def test_continue_token(self):
        self.assertTrue(TestLexer.test("continue;", "continue,;,<EOF>", 187))

    def test_return_token(self):
        self.assertTrue(TestLexer.test("return;", "return,;,<EOF>", 188))

    def test_dot_token(self):
        self.assertTrue(TestLexer.test("io.writeIntLn(x)", "io,.,writeIntLn,(,x,),<EOF>", 189))

    """test other token separately"""
    def test_class_token(self):
        self.assertTrue(TestLexer.test("class", "class,<EOF>", 190))

    def test_do_token(self):
        self.assertTrue(TestLexer.test("do", "do,<EOF>", 191))

    def test_else_token(self):
        self.assertTrue(TestLexer.test("else", "else,<EOF>", 192))

    def test_extends_token(self):
        self.assertTrue(TestLexer.test("extends", "extends,<EOF>", 193))

    def test_new_token(self):
        self.assertTrue(TestLexer.test("new", "new,<EOF>", 194))

    def test_then_token(self):
        self.assertTrue(TestLexer.test("then", "then,<EOF>", 195))

    def test_true_token(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 196))

    def test_false_token(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 197))

    def test_nil_token(self):
        self.assertTrue(TestLexer.test("nil", "nil,<EOF>", 198))

    def test_static_token(self):
        self.assertTrue(TestLexer.test("static", "static,<EOF>", 199))

    def test_final_token(self):
        self.assertTrue(TestLexer.test("final", "final,<EOF>", 200))
