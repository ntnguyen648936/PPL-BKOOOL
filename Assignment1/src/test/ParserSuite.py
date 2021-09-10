import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_01(self):
        input = \
r"""
class ABC { }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_simple_program_02(self):
        input = \
r"""
class ABC extends XYZ { }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_simple_program_03(self):
        input = \
r"""
class ABC extends XYZ { 
    int foo() { 

    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program_04(self):
        input = \
r"""
class ABC extends XYZ { 
    static foo() { 

    }
}
"""
        expect = "Error on line 3 col 14: ("
        self.assertTrue(TestParser.test(input,expect,204))

    def test_simple_program_05(self):
        input = \
r"""
ABC extends XYZ { 
    void foo() { 

    }
}
"""
        expect = "Error on line 2 col 0: ABC"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_simple_program_06(self):
        input = \
r"""
Class ABC extends XYZ { 
    void foo() { 

    }
}
"""
        expect = "Error on line 2 col 0: Class"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_simple_program_07(self):
        input = \
r"""
class ABC extends { 
    void foo() { 

    }
}
"""
        expect = "Error on line 2 col 18: {"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_simple_program_08(self):
        input = \
r"""
class ABC Extends { 
    void foo() { 

    }
}
"""
        expect = "Error on line 2 col 10: Extends"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_simple_program_09(self):
        input = \
r"""
class ABC extends ABCD
    void foo() { 

    }
}
"""
        expect = "Error on line 3 col 4: void"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_simple_program_10(self):
        input = \
r"""
class ABC extends ABCD { 
    void foo() { 

    }

"""
        expect = "Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,210))

    # ---------------------------------------------------------------------------------------------------------


    def test_expression_01(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
            int x = 1 + 2 * 3;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_expression_02(self):
        input = \
r"""
class ABC extends XYZ { 
    int x = 1 + _x * 3;
    static int foo() { 

    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_expression_03(self):
        input = \
r"""
class ABC extends XYZ { 
    int i = 1 + 2 * 3;
    static int foo() { 
        int x = 3\ 1 + a[this.i] / b2cD % c;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_expression_04(self):
        input = \
r"""
class ABC extends XYZ { 
    float n;
    static int foo() { 
            int x = 1 + 2 * 3, y = functionA(this.n);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_expression_05(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2]] + 3;   
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_expression_06(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[c[d[2]]] + 1 + 2 + 3] + 3;   
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_expression_07(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2]] + ;
    }
}
"""
        expect = "Error on line 4 col 37: ;"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_expression_08(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
            
    }
}
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_expression_09(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + 2];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_expression_10(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + 2;
    }
}
"""
        expect = "Error on line 4 col 37: ;"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_expression_11(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2) := _a[b[2] + 2];
    }
}
"""
        expect = "Error on line 4 col 22: :="
        self.assertTrue(TestParser.test(input,expect,221))

    def test_expression_12(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + new A().yo];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_expression_13(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + new A(.yo];
    }
}
"""
        expect = "Error on line 4 col 42: ."
        self.assertTrue(TestParser.test(input,expect,223))

    def test_expression_14(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + new A).yo];
    }
}
"""
        expect = "Error on line 4 col 41: )"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_expression_15(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := a==b==c;
    }
}
"""
        expect = "Error on line 4 col 30: =="
        self.assertTrue(TestParser.test(input,expect,225))

    def test_expression_16(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := a==b!=c;
    }
}
"""
        expect = "Error on line 4 col 30: !="
        self.assertTrue(TestParser.test(input,expect,226))


    def test_expression_17(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := a==b<=c;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))


    def test_expression_18(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := a>b<=c;
    }
}
"""
        expect = "Error on line 4 col 29: <="
        self.assertTrue(TestParser.test(input,expect,228))

    def test_expression_19(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := (a>b)<=c;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_expression_20(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        A _a = new A(1*4-2);
        _a.doo := (a>b)<=c;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_expression_21(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        A _a = new A(1*4-2);
        _a.doo():= (a>b)<=c;
    }
}
"""
        expect = "Error on line 5 col 16: :="
        self.assertTrue(TestParser.test(input,expect,231))


    def test_expression_22(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        A _a = new A(1*4-2);
        _a.doo()[3]:= (a>b)<=c;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_expression_23(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        A _a = new A(1*4-2);
        new A(true==false):= (a>b)<=c;
    }
}
"""
        expect = "Error on line 5 col 26: :="
        self.assertTrue(TestParser.test(input,expect,233))

    def test_expression_24(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        A _a = new A(1*4-2);
        new A(true==false);
    }
}
"""
        expect = "Error on line 5 col 26: ;"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_expression_25(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        new A(true==false).arr[new A(1*4-2)] := 1;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_expression_26(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        new A(true==false).arr[2].doo := 1e+120;
    }
}
"""
        expect = "Error on line 4 col 33: ."
        self.assertTrue(TestParser.test(input,expect,236))

    def test_expression_27(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        a := new A(true==false)[2];
    }
}
"""
        expect = "Error on line 4 col 31: ["
        self.assertTrue(TestParser.test(input,expect,237))


    def test_expression_28(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        new A(true==false).doo := 1e+120+new Ax(1,2,new Axx(arr[this.b]));
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_expression_29(self):
        input = \
r"""
class ABC extends XYZ { 
    int[2]  a, b={1,2};
    static int foo() { 
        int i=1;
        this.a[i] := b[i];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_expression_30(self):
        input = \
r"""
class ABC extends XYZ { 
    int[2]  a, b={{1,2}};
    static int foo() { 
        int i=1;
        this.a[i] := b[i];
    }
}
"""
        expect = "Error on line 3 col 18: {"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_expression_31(self):
        input = \
r"""
class ABC extends XYZ { 
    int[2][3]  a, b={1,2};
    static int foo() { 
    }
}
"""
        expect = "Error on line 3 col 10: ["
        self.assertTrue(TestParser.test(input,expect,241))

    def test_expression_32(self):
        input = \
r"""
class ABC extends XYZ { 
    int i = ----------1 + 2 * ------3;
    static int foo() { 
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_expression_33(self):
        input = \
r"""
class ABC extends XYZ { 
    boolean a = false;
    boolean i = !!!!!!!!!!!false && true || !!!!!!!!a;
    static int foo() { 
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_expression_34(self):
        input = \
r"""
class ABC extends XYZ { 
    static final string a = "false";
    string i = a ^ "true";
    static int foo() { 
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_expression_35(self):
        input = \
r"""
class ABC extends XYZ { 
    static final string a = "false";
    string i = a ^ "true" + a*b + new A(a);
    static int foo() { 
        return i ^ "string";
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_expression_36(self):
        input = \
r"""
class ABC extends XYZ {
    int c = 1;
    static int foo() { 
        a := a ^ b + - c - new ClassD(d) % e && f < e; 
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_expression_37(self):
        input = \
r"""
class ABC extends XYZ {
    int c = 1;
    static int foo() { 
        a := 1 + 5.4E-1 < 3 && True >= 2; 
    }
}
"""
        expect = "Error on line 5 col 36: >="
        self.assertTrue(TestParser.test(input,expect,247))  

    def test_expression_38(self):
        input = \
r"""
class ABC extends XYZ {
    int c = 1;
    static int foo() { 
        a := 1 + 5.4E-1 < 3 && !!2
    }
}
"""
        expect = "Error on line 6 col 4: }"
        self.assertTrue(TestParser.test(input,expect,248))  

    def test_expression_39(self):
        input = \
r"""
class ABC extends XYZ {
    int c = 1;
    static int foo() { 
        _a[3+x.foo(2)] := _a[new B(new C().a.aFunction().x + arr[this.c]) + new A().yo];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_expression_40(self):
        input = \
r"""
class ABC extends XYZ {
    int c = 1;
    static int foo() { 
        _a[3+x.foo(2)] := _a[new B(new C().a.aFunction().x + arr[this.c]) + new A().yo];
        io.writeInt(_a[x==1+x.foo(2)]);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    # ---------------------------------------------------------------------------------------------------------


    def test_statement_01(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        if a[0]==2 then if a+1==foo(true)[a*1.3e+5] then if a then a:=1; else a:=1; else
            
    }
}
"""
        expect = "Error on line 6 col 4: }"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_statement_02(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then if a+1==foo(true)[a*1.3e+5] then if a then a:=1; else a:=1; else a:=1;
            
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_statement_03(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 if a+1==foo(true)[a*1.3e+5] then if a then a:=1; else a:=1; else a:=1;
            
    }
}
"""
        expect = "Error on line 5 col 19: if"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_statement_04(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then a+1==foo(true)[a*1.3e+5] then if a then a:=1; else a:=1; else a:=1;
            
    }
}
"""
        expect = "Error on line 5 col 25: +"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_statement_05(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then a.1==foo(true)[a*1.3e+5] then if a then a:=1; else a:=1; else a:=1;
            
    }
}
"""
        expect = "Error on line 5 col 26: 1"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_statement_06(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then if a.a1==foo(true)[a*1.3e+5] then a==1 then a:=1; else a:=1; else a:=1;
            
    }
}
"""
        expect = "Error on line 5 col 59: =="
        self.assertTrue(TestParser.test(input,expect,256))

    def test_statement_07(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then if a.a1==foo(true)[a*1.3e+5] then a then a:=1; else a:=1; else a:=1;
            
    }
}
"""
        expect = "Error on line 5 col 60: then"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_statement_08(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then if a==1 then if a then a:=1 else a:=1; else a:=1;
            
    }
}
"""
        expect = "Error on line 5 col 52: else"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_statement_09(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then {
            if (a&&b||c) then {

            } else
                a := 1;
            }
        }
            
    }
}
"""
        expect = "Error on line 14 col 0: }"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_statement_10(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then {
            if (a&&b||c) then {

            } else
                a := 1
            }
        }
            
    }
}
"""
        expect = "Error on line 10 col 12: }"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_statement_11(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        for i:=2 to 10 do
        if a[0]==2 then {
            if (a&&b||c) then {
                io.writeIntLn("Hello");
            } else
                a := 1;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_statement_12(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        if a then if b then b:=1; else if c then d:=1; else if e==1 then if f==2 then g:=2; else {}
        }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_statement_13(self):
        input = \
r"""
class ABC extends XYZ { 
    break;
    static int foo() {
        
    }
}
"""
        expect = "Error on line 3 col 4: break"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_statement_14(self):
        input = \
r"""
class ABC extends XYZ { 
    continue;
    static int foo() {
        
    }
}
"""
        expect = "Error on line 3 col 4: continue"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_statement_15(self):
        input = \
r"""
class ABC extends XYZ { 
    return foo().a[2+x];
    static int foo() {
        
    }
}
"""
        expect = "Error on line 3 col 4: return"
        self.assertTrue(TestParser.test(input,expect,265))


    def test_statement_16(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        return;
    }
}
"""
        expect = "Error on line 5 col 14: ;"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_statement_17(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        return a:=5;
    }
}
"""
        expect = "Error on line 5 col 16: :="
        self.assertTrue(TestParser.test(input,expect,267))

    def test_statement_18(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        return True&&False==varA;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_statement_19(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        Shape.getNumOfShape();
        break;
        continue;
        this.a := 1 ^ s;
        return True&&False==varA;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))


    def test_statement_20(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        for i:=2 to 10 do for j:=0 downto -1 do for k:=1 to this.a+20e+1 do if a==b then for x:=1 to xxx do {}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_statement_21(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        for i:=2 to a==1 if a==b then for x:=1 to xxx do {}
    }
}
"""
        expect = "Error on line 5 col 25: if"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_statement_22(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        for i:=2 to 10 do {
            if a==b then for x:=1 to 1000 do {
                break;
            }
            else continue;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_statement_23(self):
        input = \
r"""
class ABC extends XYZ { 
    
    static int foo() {
        for i:=2 to 10 do {
            if a==b then for x:=1 to 33 do {
                break;
            }
            else continue
        }
    }
}
"""
        expect = "Error on line 10 col 8: }"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_statement_24(self):
        input = \
r"""
class ABC extends XYZ { 

    for i:=2 to 10 do {
        5.i := 1;
    }
}
"""
        expect = "Error on line 4 col 4: for"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_statement_25(self):
        input = \
r"""
class ABC extends XYZ { 
    int[2] a = {x, y};
    static int foo() {
            /*
            # line comment 1
            # line comment 2
            */
        }
    }
}
"""
        expect = "Error on line 3 col 16: x"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_statement_26(self):
        input = \
r"""
class abc {
    void getArea(string a, b, c, d){
        {
            # body
        }
    }
}
"""
        expect = "Error on line 4 col 8: {"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_statement_27(self):
        input = \
r"""
class abc {
    void getArea(string a, b, c, d){
        for a[1]:=1 to 10 do {}
    }
}
"""
        expect = "Error on line 4 col 13: ["
        self.assertTrue(TestParser.test(input,expect,277))

    def test_statement_28(self):
        input = \
r"""
class abc {
    void getArea(string a, b, c, d){
        for a.1:=1 to 10 do {}
    }
}
"""
        expect = "Error on line 4 col 14: 1"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_statement_29(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        #start of declaration part
        float r,s;
        int[5] a,b;
        #list of statements
        r:=2.0;
        s:=r*r*this.myPI;
        a[0]:= s;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_statement_30(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() {
        #start of declaration part
        float r,s,float;
    }
}
"""
        expect = "Error on line 5 col 18: float"
        self.assertTrue(TestParser.test(input,expect,280))

    # ---------------------------------------------------------------------------------------------------------


    def test_complex_program_01(self):
        input = \
r"""
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        return numOfShape;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))


    def test_complex_program_02(self):
        input = \
r"""
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        return numOfShape;
    }

class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}

"""
        expect = "Error on line 10 col 0: class"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_complex_program_03(self):
        input = \
r"""
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    final int getNumOfShape() {
        return numOfShape;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}

"""
        expect = "Error on line 6 col 27: ("
        self.assertTrue(TestParser.test(input,expect,283))

    def test_complex_program_04(self):
        input = \
r"""
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        numOfShape;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}

"""
        expect = "Error on line 7 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_complex_program_05(self):
        input = \
r"""
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        numOfShape;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}

"""
        expect = "Error on line 7 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_complex_program_06(self):
        input = \
r"""
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    
    Shape() {

    }

    static int getNumOfShape() {
        numOfShape;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length;
    }
}

class Angel extends Shape {

}

class Main {

    void main(){
        Shape s = Shape();
    }
}

"""
        expect = "Error on line 12 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,286))

    # ---------------------------------------------------------------------------------------------------------


    def test_most_complex_program_01(self):
        input = \
r"""
class Shape {
    float length,width;
    float getArea() {}
    Shape(float length,width){
        this.length := length;
        this.width := width;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
class Triangle extends Shape {
    float getArea(){
        return this.length*this.width / 2;
    }
}
class Example2 {
    void main(){
        Shape s;
        s := new Rectangle(3,4);
        io.writeFloatLn(s.getArea());
        s := new Triangle(3,4);
        io.writeFloatLn(s.getArea());
    }
}

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))


    def test_most_complex_program_02(self):
        input = \
r"""
class QuickSort {
    
    int partition(int[6] arr; int low, high)
    {
        int i = (low-1), pivot = arr[high];    
    
        for j :=low to high do
            if arr[j] <= pivot then
            { 
                i := i+1;
                arr[i] := arr[j];
                arr[j] :=arr[i];
            }
    
        arr[i+1] := arr[high];
        arr[high] := arr[i+1];
        return (i+1);
    }
    
    void quickSort(int[6] arr; int low, high) {
        if len(arr) == 1 then
            return arr;
        if low < high then
            pi := partition(arr, low, high);

        this.quickSort(arr, low, pi-1);
        this.quickSort(arr, pi+1, high);
    }
    
    void main() {
        int[6] arr = {10, 7, 8, 9, 1, 5};
        int n = 6;
        this.quickSort(arr, 0, n-1);
        io.writeStr("Sorted array is:");
        for i := 0 to n do
            io.writeInt(arr[i]);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))