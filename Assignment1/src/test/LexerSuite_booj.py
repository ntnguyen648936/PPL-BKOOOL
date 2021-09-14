# import unittest
# from TestUtils import TestLexer
#
# class LexerSuite(unittest.TestCase):
#
#     def test_lowercase_identifier(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
#     def test_lower_upper_id(self):
#         self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
#     # def test_mixed_id(self):
#     #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
#     # def test_integer(self):
#     #     """test integers"""
#     #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))
#     def test_empty_program_with_tab(self):
#         input = "\t\t\t\t\t\t   \t\t\t"
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(input, expect, 105))
#     def test_new_line(self):
#         input = "\n\n"
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(input, expect, 106))
#     def test_new_line_with_string(self):
#         input = "a\n"
#         expect = "a,<EOF>"
#         self.assertTrue(TestLexer.test(input, expect, 107))
#     def test_empty_program(self):
#         input = r""" "" """
#         expect = """,<EOF>"""
#         self.assertTrue(TestLexer.test(input, expect, 108))
#
#     def test_only_whitespace_program(self):
#         input = r""" " " """
#         expect = """ ,<EOF>"""
#         self.assertTrue(TestLexer.test(input, expect, 109))
#
#     def test_skip_space_and_only_extract_defined_tokens(self):
#         input = "Var: \n x;"
#         expect = "Var,:,x,;,<EOF>"
#         self.assertTrue(TestLexer.test(input, expect, 110))
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        self.assertTrue(
            TestLexer.test(
                r""" a b c """,
                r"""a,b,c,<EOF>""",
                101
            )
        )

    def test_2(self):
        self.assertTrue(
            TestLexer.test(
                r""" "a\n" """,
                r"""a\n,<EOF>""",
                102
            )
        )

    def test_103(self):
        self.assertTrue(
            TestLexer.test(
                "testString#",
                "testString,<EOF>",
                103
            )
        )

    def test_104(self):
        self.assertTrue(
            TestLexer.test(
                "/*/**A*",
                "/,*,/,*,*,A,*,<EOF>",
                104
            )
        )

    def test_105(self):
        self.assertTrue(
            TestLexer.test(
                "1_String",
                "1,_String,<EOF>",
                105
            )
        )

    def test_106(self):
        self.assertTrue(
            TestLexer.test(
                "**",
                "*,*,<EOF>",
                106
            )
        )

    def test_107(self):
        self.assertTrue(
            TestLexer.test(
                "#/*abc*/\nabc",
                "abc,<EOF>",
                107
            )
        )

    def test_108(self):
        self.assertTrue(
            TestLexer.test(
                "/*/**a/",
                "/,*,/,*,*,a,/,<EOF>",
                108
            )
        )

    def test_109(self):
        self.assertTrue(
            TestLexer.test(
                "/*/**/A*/",
                "A,*,/,<EOF>",
                109
            )
        )

    def test_110(self):
        self.assertTrue(
            TestLexer.test(
                "aBc AA________#",
                "aBc,AA________,<EOF>",
                110
            )
        )

    def test_111(self):
        self.assertTrue(
            TestLexer.test(
                "1230X123",
                "1230,X123,<EOF>",
                111
            )
        )

    def test_112(self):
        self.assertTrue(
            TestLexer.test(
                "0123456789",
                "0,123456789,<EOF>",
                112
            )
        )

    def test_113(self):
        self.assertTrue(
            TestLexer.test(
                "1e+20",
                "1e+20,<EOF>",
                113
            )
        )

    def test_114(self):
        self.assertTrue(
            TestLexer.test(
                "1.",
                "1.,<EOF>",
                114
            )
        )

    def test_115(self):
        self.assertTrue(
            TestLexer.test(
                "-1.3e-123",
                "-,1.3e-123,<EOF>",
                115
            )
        )

    def test_116(self):
        self.assertTrue(
            TestLexer.test(
                ".123e-1",
                ".,123e-1,<EOF>",
                116
            )
        )

    def test_117(self):
        self.assertTrue(
            TestLexer.test(
                "0O7 0O8",
                "0,O7,0,O8,<EOF>",
                117
            )
        )


    def test_118(self):
        self.assertTrue(
            TestLexer.test(
                "12.",
                "12.,<EOF>",
                118
            )
        )

    def test_119(self):
        self.assertTrue(
            TestLexer.test(
                "0.25e3",
                "0.25e3,<EOF>",
                119
            )
        )

    def test_120(self):
        self.assertTrue(
            TestLexer.test(
                "12..56",
                "12.,.,56,<EOF>",
                120
            )
        )

    def test_121(self):
        self.assertTrue(
            TestLexer.test(
                "12e.03",
                "12,e,.,0,3,<EOF>",
                121
            )
        )

    def test_122(self):
        self.assertTrue(
            TestLexer.test(
                "0.e-123",
                "0.e-123,<EOF>",
                122
            )
        )

    def test_123(self):
        self.assertTrue(
            TestLexer.test(
                "1e-1.123",
                "1e-1,.,123,<EOF>",
                123
            )
        )

    def test_124(self):
        self.assertTrue(
            TestLexer.test(
                "12.04e-1",
                "12.04e-1,<EOF>",
                124
            )
        )

    def test_125(self):
        self.assertTrue(
            TestLexer.test(
                "true",
                "true,<EOF>",
                125
            )
        )

    def test_126(self):
        self.assertTrue(
            TestLexer.test(
                "trueabc",
                "trueabc,<EOF>",
                126
            )
        )

    def test_127(self):
        self.assertTrue(
            TestLexer.test(
                "true_1",
                "true_1,<EOF>",
                127
            )
        )

    def test_128(self):
        self.assertTrue(
            TestLexer.test(
                "falseabc_",
                "falseabc_,<EOF>",
                128
            )
        )

    def test_129(self):
        self.assertTrue(
            TestLexer.test(
                "TrueFalsefalsetrue",
                "TrueFalsefalsetrue,<EOF>",
                129
            )
        )

    def test_130(self):
        self.assertTrue(
            TestLexer.test(
                "truefalseFalseTrue",
                "truefalseFalseTrue,<EOF>",
                130
            )
        )

    def test_131(self):
        self.assertTrue(
            TestLexer.test(
                "While",
                "While,<EOF>",
                131
            )
        )

    def test_132(self):
        self.assertTrue(
            TestLexer.test(
                "breakclasscontinuedoelseextendsifthenforreturn",
                "breakclasscontinuedoelseextendsifthenforreturn,<EOF>",
                132
            )
        )

    def test_133(self):
        self.assertTrue(
            TestLexer.test(
                "**#**/*",
                "*,*,<EOF>",
                133
            )
        )

    # def test_134(self):
    #     self.assertTrue(
    #         TestLexer.test(
    #             "a[3+x.foo(2)] := a[b[2]] +3;",
    #             "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>",
    #             134
    #         )
    #     )

    def test_135(self):
        self.assertTrue(
            TestLexer.test(
                "WhileDoingEndDo",
                "WhileDoingEndDo,<EOF>",
                135
            )
        )

    def test_136(self):
        self.assertTrue(
            TestLexer.test(
                "+-*\\",
                "+,-,*,\\,<EOF>",
                136
            )
        )

    def test_137(self):
        self.assertTrue(
            TestLexer.test(
                "====:=/:=!=",
                "==,==,:=,/,:=,!=,<EOF>",
                137
            )
        )

    def test_138(self):
        self.assertTrue(
            TestLexer.test(
                "======/:=!=",
                "==,==,==,/,:=,!=,<EOF>",
                138
            )
        )

    def test_139(self):
        self.assertTrue(
            TestLexer.test(
                "~",
                "Error Token ~",
                139
            )
        )

    def test_140(self):
        self.assertTrue(
            TestLexer.test(
                "+.-.*.\\.",
                "+,.,-,.,*,.,\\,.,<EOF>",
                140
            )
        )

    def test_141(self):
        self.assertTrue(
            TestLexer.test(
                ">.<.==<=<=.>=>=.:=",
                ">,.,<,.,==,<=,<=,.,>=,>=,.,:=,<EOF>",
                141
            )
        )

    def test_142(self):
        self.assertTrue(
            TestLexer.test(
                "{1.05,1,\"huhihihu\"}",
                "{,1.05,,,1,,,huhihihu,},<EOF>",
                142
            )
        )

    def test_143(self):
        self.assertTrue(
            TestLexer.test(
                "{1,   3,5    }",
                "{,1,,,3,,,5,},<EOF>",
                143
            )
        )

    def test_144(self):
        self.assertTrue(
            TestLexer.test(
                "{{    },{            } }",
                "{,{,},,,{,},},<EOF>",
                144
            )
        )

    def test_145(self):
        self.assertTrue(
            TestLexer.test(
                "{ {1,2,3},{4,5,6}}",
                "{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},<EOF>",
                145
            )
        )

    def test_146(self):
        self.assertTrue(
            TestLexer.test(
                "{\"abc\",\"xyz\"}",
                "{,abc,,,xyz,},<EOF>",
                146
            )
        )

    def test_147(self):
        self.assertTrue(
            TestLexer.test(
                "{True,False,False,True}",
                "{,True,,,False,,,False,,,True,},<EOF>",
                147
            )
        )

    def test_148(self):
        self.assertTrue(
            TestLexer.test(
                "{{1,2,3},{4,5,6,{7,8,9}}}",
                "{,{,1,,,2,,,3,},,,{,4,,,5,,,6,,,{,7,,,8,,,9,},},},<EOF>",
                148
            )
        )

    def test_149(self):
        self.assertTrue(
            TestLexer.test(
                "{{1,2,3},{4,5,6,{7,8,9},   {10,11,12}}}",
                "{,{,1,,,2,,,3,},,,{,4,,,5,,,6,,,{,7,,,8,,,9,},,,{,10,,,11,,,12,},},},<EOF>",
                149
            )
        )

    def test_150(self):
        self.assertTrue(
            TestLexer.test(
                "/*##/**/",
                "<EOF>",
                150
            )
        )

    def test_151(self):
        self.assertTrue(
            TestLexer.test(
                "{12e4,4.,0.}",
                "{,12e4,,,4.,,,0.,},<EOF>",
                151
            )
        )

    def test_152(self):
        self.assertTrue(
            TestLexer.test(
                "{1,2 /*haha*/*   }",
                "{,1,,,2,*,},<EOF>",
                152
            )
        )

    def test_153(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc 123\"",
                "abc 123,<EOF>",
                153
            )
        )

    def test_154(self):
        self.assertTrue(
            TestLexer.test(
                "\"/*#####\"",
                "/*#####,<EOF>",
                154
            )
        )

    def test_155(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc \t abc \\f abc\"",
                "abc \t abc \\f abc,<EOF>",
                155
            )
        )

    def test_156(self):
        self.assertTrue(
            TestLexer.test(
                r""" "abc\r def" """,
                "abc\\r def,<EOF>",
                156
            )
        )

    def test_157(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc \\n\"",
                "abc \\n,<EOF>",
                157
            )
        )

    def test_158(self):
        self.assertTrue(
            TestLexer.test(
                "\"~~~\"",
                "~~~,<EOF>",
                158
            )
        )

    def test_159(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc\\\" ok\\\"\"",
                "abc\\\" ok\\\",<EOF>",
                159
            )
        )

    def test_160(self):
        self.assertTrue(
            TestLexer.test(
                r""" "More esc \n \t \k" """,
                "Illegal Escape In String: More esc \\n \\t \\k",
                160
            )
        )

    def test_161(self):
        self.assertTrue(
            TestLexer.test(
                "\"This is an unclose string '",
                "Unclosed String: This is an unclose string '",
                161
            )
        )

    def test_162(self):
        self.assertTrue(
            TestLexer.test(
                """ "He said: '\\\"Hello'\\\"" """,
                "He said: '\\\"Hello'\\\",<EOF>", 162
            )
        )

    def test_163(self):
        self.assertTrue(
            TestLexer.test(
                "\"He said: \\\"Hello \\n hello \\\"\"",
                "He said: \\\"Hello \\n hello \\\",<EOF>",
                163
            )
        )

    def test_164(self):
        self.assertTrue(
            TestLexer.test(
                "/*one\n*two\n*three\n*/",
                "<EOF>",
                164
            )
        )

    def test_165(self):
        self.assertTrue(
            TestLexer.test(
                "*##one\t \\k \b *#$#%@^^^**",
                "*,<EOF>",
                165
            )
        )

    def test_166(self):
        self.assertTrue(
            TestLexer.test(
                "/*one\t \\k",
                "/,*,one,\\,k,<EOF>",
                166
            )
        )

    def test_167(self):
        self.assertTrue(
            TestLexer.test(
                "/*one\t \\k \b */$#%@^^^**",
                "Error Token $",
                167
            )
        )

    def test_168(self):
        self.assertTrue(
            TestLexer.test(
                "/**/*?",
                "*,Error Token ?",
                168
            )
        )

    def test_169(self):
        self.assertTrue(
            TestLexer.test(
                "\"I said: \\\"<EOF> \p\\\"\"",
                "Illegal Escape In String: I said: \\\"<EOF> \p",
                169
            )
        )

    def test_170(self):
        self.assertTrue(
            TestLexer.test(
                "Var: a,a,f:={1,2};",
                "Var,:,a,,,a,,,f,:=,{,1,,,2,},;,<EOF>",
                170
            )
        )

    def test_171(self):
        self.assertTrue(
            TestLexer.test(
                "var: a,b,c,d;",
                "var,:,a,,,b,,,c,,,d,;,<EOF>",
                171
            )
        )

    def test_172(self):
        self.assertTrue(
            TestLexer.test(
                "v:=4+.3*.5-2:=6.e4",
                "v,:=,4,+,.,3,*,.,5,-,2,:=,6.e4,<EOF>",
                172
            )
        )

    def test_173(self):
        self.assertTrue(
            TestLexer.test(
                "if(!a && b != c) then z:={1,5e99}",
                "if,(,!,a,&&,b,!=,c,),then,z,:=,{,1,,,5e99,},<EOF>",
                173
            )
        )

    def test_174(self):
        self.assertTrue(
            TestLexer.test(
                "a[3+foo(i)] <= b +. {1.2}",
                "a,[,3,+,foo,(,i,),],<=,b,+,.,{,1.2,},<EOF>",
                174
            )
        )

    def test_175(self):
        self.assertTrue(
            TestLexer.test(
                "a[0xAFF][3] != {{1,2,3},{4,5,6}}",
                "a,[,0,xAFF,],[,3,],!=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},<EOF>",
                175
            )
        )

    def test_176(self):
        self.assertTrue(
            TestLexer.test(
                "for(i:=9;i<11;i:=i+1)",
                "for,(,i,:=,9,;,i,<,11,;,i,:=,i,+,1,),<EOF>",
                176
            )
        )

    def test_177(self):
        self.assertTrue(
            TestLexer.test(
                "If \"string\" == True Then a := b",
                "If,string,==,True,Then,a,:=,b,<EOF>",
                177
            )
        )

    def test_178(self):
        self.assertTrue(
            TestLexer.test(
                "If \"string\" ? True Then a = b",
                "If,string,Error Token ?",
                178
            )
        )

    def test_179(self):
        self.assertTrue(
            TestLexer.test(
                "if \"string\" != true then a / b := 5;",
                "if,string,!=,true,then,a,/,b,:=,5,;,<EOF>",
                179
            )
        )

    def test_180(self):
        self.assertTrue(
            TestLexer.test(
                "if \"string\" != true then a \ b := 5;",
                "if,string,!=,true,then,a,\,b,:=,5,;,<EOF>",
                180
            )
        )

    def test_181(self):
        self.assertTrue(
            TestLexer.test(
                "if \"string \\\"abc\\\"\" != true then a \\. b := 5;",
                "if,string \\\"abc\\\",!=,true,then,a,\\,.,b,:=,5,;,<EOF>",
                181
            )
        )

    def test_182(self):
        self.assertTrue(
            TestLexer.test(
                "if \"string\" != true */abc# then a \\ b = 5;",
                "if,string,!=,true,*,/,abc,<EOF>",
                182
            )
        )

    def test_183(self):
        self.assertTrue(
            TestLexer.test(
                "/*If \"string\" != True*/  Then a \\ b := 5;",
                "Then,a,\\,b,:=,5,;,<EOF>",
                183
            )
        )

    def test_184(self):
        self.assertTrue(
            TestLexer.test(
                "If \"string\\' != True  Then a + b := 5;",
                "If,Unclosed String: string\\' != True  Then a + b := 5;",
                184
            )
        )

    def test_185(self):
        self.assertTrue(
            TestLexer.test(
                "\"Hello \\a \"",
                "Illegal Escape In String: Hello \\a",
                185
            )
        )

    def test_186(self):
        self.assertTrue(
            TestLexer.test(
                "\"Illegal with the \z escape abcxyz \"",
                "Illegal Escape In String: Illegal with the \z",
                186
            )
        )

    def test_187(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc\n\n\"",
                "Unclosed String: abc",
                187
            )
        )

    def test_188(self):
        self.assertTrue(
            TestLexer.test(
                " \n \t \f \r",
                "<EOF>",
                188
            )
        )

    def test_189(self):
        self.assertTrue(
            TestLexer.test(
                "\"Some illegals \" \\nabc \\k \"",
                "Some illegals ,\\,nabc,\\,k,Unclosed String: ",
                189
            )
        )

    def test_190(self):
        self.assertTrue(
            TestLexer.test(
                "\"Hello world**notcomment**",
                "Unclosed String: Hello world**notcomment**",
                190
            )
        )

    def test_191(self):
        self.assertTrue(
            TestLexer.test(
                "\"Hello world \\n '",
                "Unclosed String: Hello world \\n \'",
                191
            )
        )

    def test_192(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc\",\"xyz\"",
                "abc,,,xyz,<EOF>",
                192
            )
        )

    def test_193(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc\",\"xyz",
                "abc,,,Unclosed String: xyz",
                193
            )
        )

    def test_194(self):
        self.assertTrue(
            TestLexer.test(
                "not_errorChar,Error",
                "not_errorChar,,,Error,<EOF>",
                194
            )
        )

    def test_195(self):
        self.assertTrue(
            TestLexer.test(
                "0Char^",
                "0,Char,^,<EOF>",
                195
            )
        )

    def test_196(self):
        self.assertTrue(
            TestLexer.test(
                "\"error char in string $##!@\"",
                "error char in string $##!@,<EOF>",
                196
            )
        )

    def test_197(self):
        self.assertTrue(
            TestLexer.test(
                "-3,-4,5,-0xFFFF,0",
                "-,3,,,-,4,,,5,,,-,0,xFFFF,,,0,<EOF>",
                197
            )
        )

    def test_198(self):
        self.assertTrue(
            TestLexer.test(
                "\"abc\m\"",
                "Illegal Escape In String: abc\m",
                198
            )
        )

    def test_199(self):
        self.assertTrue(
            TestLexer.test(
                r""" /*bbbjhgjh**/ """,
                "<EOF>",
                199
            )
        )

    def test_200(self):
        self.assertTrue(
            TestLexer.test(
                "/*#abc*/",
                "<EOF>",
                200
            )
        )
