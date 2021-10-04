import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # ---------------------------------------------------------------------------------------------------------

    def test_stringLit_01(self):
        self.assertTrue(TestLexer.test(
                """\"What ''' are you doing?\"""",
                "What ''' are you doing?,<EOF>",
                101
            )
        )

    def test_stringLit_02(self):
        self.assertTrue(TestLexer.test(
                """\"What \\x are you doing?\"""",
                "Illegal Escape In String: What \\x",
                102
            )
        )

    def test_stringLit_03(self):
        self.assertTrue(TestLexer.test(
                """\"What \\n \\r \\t are you doing?\"""",
                "What \\n \\r \\t are you doing?,<EOF>",
                103
            )
        )

    def test_stringLit_04(self):
        self.assertTrue(TestLexer.test(
                """\"What are you doing?""",
                "Unclosed String: What are you doing?",
                104
            )
        )

    def test_stringLit_05(self):
        self.assertTrue(TestLexer.test(
                """\"Say: \\"What are you doing?\\" \"""",
                """Say: \\"What are you doing?\\" ,<EOF>""",
                105
            )
        )

    def test_stringLit_06(self):
        self.assertTrue(TestLexer.test(
                """\"What \n are you doing?\"""",
                """Unclosed String: What """,
                106
            )
        )

    def test_stringLit_07(self):
        self.assertTrue(TestLexer.test(
                """What are you doing?\"""",
                "What,are,you,doing,Error Token ?",
                107
            )
        )

    def test_stringLit_08(self):
        self.assertTrue(TestLexer.test(
                """What are you doing\"""",
                "What,are,you,doing,Unclosed String: ",
                108
            )
        )

    def test_stringLit_09(self):
        self.assertTrue(TestLexer.test(
                """\"What \\h \"""",
                """Illegal Escape In String: What \h""",
                109
            )
        )

    def test_stringLit_10(self):
        self.assertTrue(TestLexer.test(
                """\"abc\r\"""",
                """Unclosed String: abc""",
                110
            )
        )

    def test_stringLit_11(self):
        self.assertTrue(
            TestLexer.test(
                "\" abc \t \f \b abc \\f abc \"",
                " abc \t \f \b abc \\f abc ,<EOF>",
                111
            )
        )

    def test_stringLit_12(self):
        self.assertTrue(
            TestLexer.test(
                "\"abcd\!\"",
                "Illegal Escape In String: abcd\!",
                112
            )
        )

    def test_stringLit_13(self):
        self.assertTrue(
            TestLexer.test(
                "\"test /*comment*/ inside a string\"",
                "test /*comment*/ inside a string,<EOF>",
                113
            )
        )

    def test_stringLit_14(self):
        self.assertTrue(
            TestLexer.test(
                "\"test /*comment*/ /*inside \\n*/ a string\"",
                "test /*comment*/ /*inside \\n*/ a string,<EOF>",
                114
            )
        )

    def test_stringLit_15(self):
        self.assertTrue(
            TestLexer.test(
                "\"test #comment #inside a string\"",
                "test #comment #inside a string,<EOF>",
                115
            )
        )

    def test_stringLit_16(self):
        self.assertTrue(
            TestLexer.test(
                """\"\\"\\"\\"\"""",
                """\\"\\"\\",<EOF>""",
                116
            )
        )

    def test_stringLit_17(self):
        self.assertTrue(
            TestLexer.test(
                "\"this is a string\" and \"this is also a string\"",
                "this is a string,and,this is also a string,<EOF>",
                117
            )
        )

    def test_stringLit_18(self):
        self.assertTrue(
            TestLexer.test(
                "io.writeStr(\"Sorted array is:\");",
                "io,.,writeStr,(,Sorted array is:,),;,<EOF>",
                118
            )
        )

    def test_stringLit_19(self):
        self.assertTrue(
            TestLexer.test(
                "writeStrLn(\"Print somethings here\")",
                "writeStrLn,(,Print somethings here,),<EOF>",
                119
            )
        )

    def test_stringLit_20(self):
        self.assertTrue(
            TestLexer.test(
                "string a = \"string1\" ^ \"string2\"",
                "string,a,=,string1,^,string2,<EOF>",
                120
            )
        )
    # ---------------------------------------------------------------------------------------------------------

    def test_identifier_01(self):
        self.assertTrue(TestLexer.test(
                "abc12d a1bCd",
                "abc12d,a1bCd,<EOF>",
                131
            )
        )

    def test_identifier_02(self):
        self.assertTrue(TestLexer.test(
                "ab?cd",
                "ab,Error Token ?",
                132
            )
        )

    def test_identifier_03(self):
        self.assertTrue(TestLexer.test(
            "a12b_Dd",
            "a12b_Dd,<EOF>",
            133))

    def test_identifier_04(self):
        self.assertTrue(TestLexer.test(
            "12abc",
            "12,abc,<EOF>",
            134))

    def test_identifier_05(self):
        self.assertTrue(TestLexer.test(
            "12_Abc",
            "12,_Abc,<EOF>",
            135))

    def test_identifier_06(self):
        self.assertTrue(TestLexer.test(
            "abc 1A2",
            "abc,1,A2,<EOF>",
            136))

    def test_identifier_07(self):
        self.assertTrue(TestLexer.test(
            "class Triangle extends Shape {}",
            "class,Triangle,extends,Shape,{,},<EOF>",
            137))

    def test_identifier_08(self):
        self.assertTrue(TestLexer.test(
            "float length,width;",
            "float,length,,,width,;,<EOF>",
            138))

    def test_identifier_09(self):
        self.assertTrue(TestLexer.test(
            "int partition(int[6] arr; int low, high);",
            "int,partition,(,int,[,6,],arr,;,int,low,,,high,),;,<EOF>",
            139))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.test(
            "io.writeInt(anIntVar);",
            "io,.,writeInt,(,anIntVar,),;,<EOF>",
            140))

    # ---------------------------------------------------------------------------------------------------------

    def test_intLit_01(self):
        self.assertTrue(TestLexer.test(
            "1234 0982",
            "1234,0982,<EOF>",
            151))

    def test_intLit_02(self):
        self.assertTrue(TestLexer.test(
            "1234-0982",
            "1234,-,0982,<EOF>",
            152))

    def test_intLit_03(self):
        self.assertTrue(TestLexer.test(
            "1234 abcd 0982",
            "1234,abcd,0982,<EOF>",
            133))

    def test_intLit_04(self):
        self.assertTrue(TestLexer.test(
            "984753aBc_4s",
            "984753,aBc_4s,<EOF>",
            154))

    def test_intLit_05(self):
        self.assertTrue(TestLexer.test(
            "-----9877",
            "-,-,-,-,-,9877,<EOF>",
            155))

    def test_intLit_06(self):
        self.assertTrue(TestLexer.test(
            "5*1+3/2%f",
            "5,*,1,+,3,/,2,%,f,<EOF>",
            156))

    def test_intLit_07(self):
        self.assertTrue(TestLexer.test(
            ".5",
            ".,5,<EOF>",
            157))

    def test_intLit_08(self):
        self.assertTrue(TestLexer.test(
            "(1and.2)",
            "(,1,and,.,2,),<EOF>",
            158))

    def test_intLit_09(self):
        self.assertTrue(TestLexer.test(
            "1234:=abcd+0982",
            "1234,:=,abcd,+,0982,<EOF>",
            159))

    def test_intLit_10(self):
        self.assertTrue(TestLexer.test(
            "1234=0982",
            "1234,=,0982,<EOF>",
            160))

    # ---------------------------------------------------------------------------------------------------------

    def test_floatLit_01(self):
        self.assertTrue(TestLexer.test(
            "12.2342 12.",
            "12.2342,12.,<EOF>",
            121))

    def test_floatLit_02(self):
        self.assertTrue(TestLexer.test(
            "1e-0982 1E-0982 1e+0982 1E+0982",
            "1e-0982,1E-0982,1e+0982,1E+0982,<EOF>",
            122))

    def test_floatLit_03(self):
        self.assertTrue(TestLexer.test(
            "123.4E+5678 123.4e+5678 123.4E-5678 123.4e-5678",
            "123.4E+5678,123.4e+5678,123.4E-5678,123.4e-5678,<EOF>",
            123))

    def test_floatLit_04(self):
        self.assertTrue(TestLexer.test(
            "12.E+3 12.e+3 12.E-3 12.e-3",
            "12.E+3,12.e+3,12.E-3,12.e-3,<EOF>",
            124))

    def test_floatLit_05(self):
        self.assertTrue(TestLexer.test(
            ".4E+5678",
            ".,4E+5678,<EOF>",
            125))

    def test_floatLit_06(self):
        self.assertTrue(TestLexer.test(
            "1.E",
            "1.,E,<EOF>",
            126))

    def test_floatLit_07(self):
        self.assertTrue(TestLexer.test(
            "1.E+",
            "1.,E,+,<EOF>",
            127))

    def test_floatLit_08(self):
        self.assertTrue(TestLexer.test(
            "1234e-0982e+123",
            "1234e-0982,e,+,123,<EOF>",
            128))

    def test_floatLit_09(self):
        self.assertTrue(TestLexer.test(
            "1.e?3",
            "1.,e,Error Token ?",
            129))

    def test_floatLit_10(self):
        self.assertTrue(TestLexer.test(
            ".3e+3",
            ".,3e+3,<EOF>",
            130))

    # ---------------------------------------------------------------------------------------------------------

    def test_comment_01(self):
        input = \
            """
/* This is a block comment:
# line 
# line
*/
"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_comment_02(self):
        input = \
            """
/* This is a block comment:
line 
/* inside block */
line
*/"""
        expect = "line,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_comment_03(self):
        input = \
            """
/* This is a block comment:
line 
/* inside block
"""
        expect = "/,*,This,is,a,block,comment,Error Token :"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_comment_04(self):
        input = \
            """
# This is a line comment
"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_comment_05(self):
        input = \
            """
# This is a line comment /* block */
"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_comment_06(self):
        input = \
            """
# This is a line comment /* block
comment */
"""
        expect = "comment,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect,146))

    def test_comment_07(self):
        input = \
            """
## This is a line comment !@#!@!#@132_() \\t \t \f \\z # and 
"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_comment_08(self):
        input = \
            """
class Main {
    /*
    void main(){
        # Shape s = Shape();
    }
    */
}
"""
        expect = "class,Main,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_comment_09(self):
        input = \
            """
class Main {
    /*
    void main(){
        # Shape s = Shape();
    }
}
"""
        expect = "class,Main,{,/,*,void,main,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_comment_10(self):
        input = \
            """
class Main {
    /*
    void /* main() */{
        # Shape s = Shape();
    }
}
"""
        expect = "class,Main,{,{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))


# ---------------------------------------------------------------------------------------------------------


    def test_expression_01(self):
        self.assertTrue(TestLexer.test(
            "int a = 1, b = 2",
            "int,a,=,1,,,b,=,2,<EOF>", 
            161))

    def test_expression_02(self):
        self.assertTrue(TestLexer.test(
            "_a:=1.2\\5e-1",
            "_a,:=,1.2,\\,5e-1,<EOF>",
            162))

    def test_expression_03(self):
        self.assertTrue(TestLexer.test(
            "a[0]:=2*(a&&b||c)",
            "a,[,0,],:=,2,*,(,a,&&,b,||,c,),<EOF>",
            163))

    def test_expression_04(self):
        self.assertTrue(TestLexer.test(
            "int x = 1 + 2 * 3, y = functionA(this.n)",
            "int,x,=,1,+,2,*,3,,,y,=,functionA,(,this,.,n,),<EOF>", 
            164))

    def test_expression_05(self):
        self.assertTrue(TestLexer.test(
            r"int x = 3\ 1 + a[this.i] / b2cD % c",
            r"int,x,=,3,\,1,+,a,[,this,.,i,],/,b2cD,%,c,<EOF>",
            165))

    def test_expression_06(self):
        self.assertTrue(TestLexer.test(
            "int x = 1 + 2 * 3, y = functionA(this.n)",
            "int,x,=,1,+,2,*,3,,,y,=,functionA,(,this,.,n,),<EOF>",
            166))

    def test_expression_07(self):
        self.assertTrue(TestLexer.test(
            "boolean a = true == false && varA",
            "boolean,a,=,true,==,false,&&,varA,<EOF>", 
            167))

    def test_expression_08(self):
        self.assertTrue(TestLexer.test(
            "_a[3+x.foo(2)] := a==b!=c",
            "_a,[,3,+,x,.,foo,(,2,),],:=,a,==,b,!=,c,<EOF>",
            168))

    def test_expression_09(self):
        self.assertTrue(TestLexer.test(
            "_a[a&&b] := a>b<=c",
            "_a,[,a,&&,b,],:=,a,>,b,<=,c,<EOF>",
            169))

    def test_expression_10(self):
        self.assertTrue(TestLexer.test(
            "a[a>b<=c]:=a&&b||c",
            "a,[,a,>,b,<=,c,],:=,a,&&,b,||,c,<EOF>",
            170))

    def test_expression_11(self):
        self.assertTrue(TestLexer.test(
            "_a[x.foo(2)] := b[2] + new A().yo;",
            "_a,[,x,.,foo,(,2,),],:=,b,[,2,],+,new,A,(,),.,yo,;,<EOF>", 
            171))

    def test_expression_12(self):
        self.assertTrue(TestLexer.test(
            "_a.doo := (a>b)<=c;",
            "_a,.,doo,:=,(,a,>,b,),<=,c,;,<EOF>",
            172))

    def test_expression_13(self):
        self.assertTrue(TestLexer.test(
            "A _a = new A(1*4-2)",
            "A,_a,=,new,A,(,1,*,4,-,2,),<EOF>",
            173))

    def test_expression_14(self):
        self.assertTrue(TestLexer.test(
            "new A(true==false):= (a>b)<=c;",
            "new,A,(,true,==,false,),:=,(,a,>,b,),<=,c,;,<EOF>", 
            174))

    def test_expression_15(self):
        self.assertTrue(TestLexer.test(
            "new A(true==false).arr[new A(1*4-2)] := 1",
            "new,A,(,true,==,false,),.,arr,[,new,A,(,1,*,4,-,2,),],:=,1,<EOF>",
            175))

    def test_expression_16(self):
        self.assertTrue(TestLexer.test(
            "1e+120+new Ax(1,2,new Axx(arr[this.b]))",
            "1e+120,+,new,Ax,(,1,,,2,,,new,Axx,(,arr,[,this,.,b,],),),<EOF>",
            176))

    def test_expression_17(self):
        self.assertTrue(TestLexer.test(
            "this.a[i] := b[i]",
            "this,.,a,[,i,],:=,b,[,i,],<EOF>", 
            177))

    def test_expression_18(self):
        self.assertTrue(TestLexer.test(
            "int[2] a, b={1,2}",
            "int,[,2,],a,,,b,=,{,1,,,2,},<EOF>",
            178))

    def test_expression_19(self):
        self.assertTrue(TestLexer.test(
            "int i = ----------1 + 2 * ------3",
            "int,i,=,-,-,-,-,-,-,-,-,-,-,1,+,2,*,-,-,-,-,-,-,3,<EOF>",
            179))

    def test_expression_20(self):
        self.assertTrue(TestLexer.test(
            "boolean i = !!!!!!!!!!!false && true || !!!!!!!!a",
            "boolean,i,=,!,!,!,!,!,!,!,!,!,!,!,false,&&,true,||,!,!,!,!,!,!,!,!,a,<EOF>",
            180))

    def test_expression_21(self):
        self.assertTrue(TestLexer.test(
            "string a = \"false\"",
            "string,a,=,false,<EOF>", 
            181))

    def test_expression_22(self):
        self.assertTrue(TestLexer.test(
            "string i = a ^ \"true\" + a*b + new A(a);",
            "string,i,=,a,^,true,+,a,*,b,+,new,A,(,a,),;,<EOF>",
            182))

    def test_expression_23(self):
        self.assertTrue(TestLexer.test(
            "if a.a1==foo(true)[a*1.3e+5] then a",
            "if,a,.,a1,==,foo,(,true,),[,a,*,1.3e+5,],then,a,<EOF>",
            183))

    def test_expression_24(self):
        self.assertTrue(TestLexer.test(
            "return i ^ \"string\";",
            "return,i,^,string,;,<EOF>", 
            184))

    def test_expression_25(self):
        self.assertTrue(TestLexer.test(
            "string i = varX + a ^ \"true\";",
            "string,i,=,varX,+,a,^,true,;,<EOF>",
            185))

    def test_expression_26(self):
        self.assertTrue(TestLexer.test(
            "a := 1 + 5.4E-1 < 3 && True >= 2; ",
            "a,:=,1,+,5.4E-1,<,3,&&,True,>=,2,;,<EOF>",
            186))

    def test_expression_27(self):
        self.assertTrue(TestLexer.test(
            r"a := a ^ b + - c - new ClassD(d) % e && f < e",
            r"a,:=,a,^,b,+,-,c,-,new,ClassD,(,d,),%,e,&&,f,<,e,<EOF>", 
            187))

    def test_expression_28(self):
        self.assertTrue(TestLexer.test(
            "a := 1 + 5.4E-1 < 3 && !!2",
            "a,:=,1,+,5.4E-1,<,3,&&,!,!,2,<EOF>",
            188))

    def test_expression_29(self):
        self.assertTrue(TestLexer.test(
            "if a[0]==2 then if a+1==foo(true)[a*1.3e+5] then",
            "if,a,[,0,],==,2,then,if,a,+,1,==,foo,(,true,),[,a,*,1.3e+5,],then,<EOF>",
            189))

    def test_expression_30(self):
        self.assertTrue(TestLexer.test(
            "_a[3] := _a[new B(new C().a.aFunction().x + arr[this.c]) + new A().yo]",
            "_a,[,3,],:=,_a,[,new,B,(,new,C,(,),.,a,.,aFunction,(,),.,x,+,arr,[,this,.,c,],),+,new,A,(,),.,yo,],<EOF>",
            190))

# ---------------------------------------------------------------------------------------------------------

    def test_program_01(self):
        input = \
            """
Shape() {

}
"""
        expect = "Shape,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_program_02(self):
        input = \
            """
class Triangle extends Shape {
    float getArea(){
        return this.length*this.width / 2;
    }
}
"""
        expect = "class,Triangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_program_03(self):
        input = \
            """
class Main {
    void main(){
        Shape s = new Shape(); # Shape is a Class name
        Shape s = Shape(); # Shape is a function
    }
}
"""
        expect = "class,Main,{,void,main,(,),{,Shape,s,=,new,Shape,(,),;,Shape,s,=,Shape,(,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))


    def test_program_04(self):
        input = \
            """
class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}
"""
        expect = "class,Rectangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))


    def test_program_05(self):
        input = \
            """
class Main {
    void main(){
        Shape s = Shape();
    }
}
"""
        expect = "class,Main,{,void,main,(,),{,Shape,s,=,Shape,(,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))


    def test_program_06(self):
        input = \
            """
class Main {
    void main() {
        Shape s = nil;
    }
}
"""
        expect = "class,Main,{,void,main,(,),{,Shape,s,=,nil,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))


    def test_program_07(self):
        input = \
            """
class Main {
    void main() {
        arr[i+1] := arr[high];
        return (i+1);
    }
}
"""
        expect = "class,Main,{,void,main,(,),{,arr,[,i,+,1,],:=,arr,[,high,],;,return,(,i,+,1,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))


    def test_program_08(self):
        input = \
            """
class QuickSort {
    void quickSort(int[6] arr) {
        /*
        if len(arr) == 1 then
            return arr;
        */
        # this.quickSort(arr, low, pi-1);
        this.quickSort(arr, pi+1, high);
    }
}
"""
        expect = "class,QuickSort,{,void,quickSort,(,int,[,6,],arr,),{,this,.,quickSort,(,arr,,,pi,+,1,,,high,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))

    
    def test_program_09(self):
        input = \
            """
class QuickSort {
    void quickSort() {
        # this.quickSort(arr, low, pi-1);
        this.quickSort(arr, pi+1, high);
    }
}
"""
        expect = "class,QuickSort,{,void,quickSort,(,),{,this,.,quickSort,(,arr,,,pi,+,1,,,high,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))


    def test_program_10(self):
        input = \
            """
class Main {
    void main() {
        {
            {
                {{}}
                {}
            }
        }
    }
}
"""
        expect = "class,Main,{,void,main,(,),{,{,{,{,{,},},{,},},},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))