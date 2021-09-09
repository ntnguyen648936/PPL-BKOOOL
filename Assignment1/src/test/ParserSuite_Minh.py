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
        int x = 3\\1 + a[this.i] / b2cD % c;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2123))

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

    def test_expression_04(self):
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

    def test_expression_05(self):
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

    def test_expression_05(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2]] + ;
    }
}
"""
        expect = "Error on line 4 col 37: ;"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_expression_06(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
            
    }
}
""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_expression_07(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + 2];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_expression_08(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + 2;
    }
}
"""
        expect = "Error on line 4 col 37: ;"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_expression_06(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2) := _a[b[2] + 2];
    }
}
"""
        expect = "Error on line 4 col 22: :="
        self.assertTrue(TestParser.test(input,expect,216))

    def test_expression_07(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + new A().yo];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_expression_08(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + new A(.yo];
    }
}
"""
        expect = "Error on line 4 col 42: ."
        self.assertTrue(TestParser.test(input,expect,218))

    def test_expression_09(self):
        input = \
r"""
class ABC extends XYZ { 
    static int foo() { 
        _a[3+x.foo(2)] := _a[b[2] + new A).yo];
    }
}
"""
        expect = "Error on line 4 col 41: )"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_expression_10(self):
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
        self.assertTrue(TestParser.test(input,expect,220))

    def test_expression_11(self):
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
        self.assertTrue(TestParser.test(input,expect,221))

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
        self.assertTrue(TestParser.test(input,expect,241))


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
        self.assertTrue(TestParser.test(input,expect,271))


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