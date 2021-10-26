import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_empty_class(self):
        """Simple program with 1 empty class """
        input = """class a {}"""
        expect = str(Program([ClassDecl(classname=Id("a"),memlist=[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_empty_class_with_parent_name(self):
        """Simple program with 1 class that has parentname"""
        input = """class a extends ABC{}"""
        expect = str(Program([ClassDecl(classname=Id("a"),memlist=[],parentname=Id("ABC"))]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_many_empty_class_with_parents_name(self):
        """Simple program with 3 class that has parentname"""
        input = """
        class Shape {}
        class Rectangle extends Shape {}
        class Square extends Shape{}
        """
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[]),ClassDecl(classname=Id("Rectangle"),memlist=[],parentname=Id("Shape")),ClassDecl(classname=Id("Square"),memlist=[],parentname=Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_program_class_with_memberlist(self):
        """Simple program with 1 class that has memberlist: method declaration and attribute declaration"""
        input = """class a {
        int a = 2,b = 3;
        int total(int a, b) {
            return a + b;
        }
        }"""
        expect = str(Program([ClassDecl(classname=Id("a"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("a"),varType=IntType(),varInit=IntLiteral(2))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("b"),varType=IntType(),varInit=IntLiteral(3))),MethodDecl(name=Id("total"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=IntType()),VarDecl(variable=Id("b"),varType=IntType())],returnType=IntType(),body=Block([],[Return(BinaryOp("+",left=Id("a"),right=Id("b")))]))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_class_with_attribute_declaration_list(self):
        """Simple program with 1 class that has memberlist: attribute declaration"""
        input = """class a {
        final int a = 2;
        static float b = 3.0;
        static final float pi = 3.14;
        }"""
        expect = str(Program([ClassDecl(classname=Id("a"),memlist=[AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("a"),constType=IntType(),value=IntLiteral(2))),AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("b"),varType=FloatType(),varInit=FloatLiteral(3.0))),AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("pi"),constType=FloatType(),value=FloatLiteral(3.14)))])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_class_with_constructor(self):
        """Simple program with 1 class that has memberlist: constructor"""
        input = """class Shape {
        Shape(float a, b) {
            this.a := a;
            this.b := b;
        }
        }"""
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=FloatType()),VarDecl(variable=Id("b"),varType=FloatType())],returnType=None,body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("a")),exp=Id("a")),Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("b")),exp=Id("b"))]))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_class_with_two_constructor(self):
        """Simple program with 1 class that has memberlist: 2 constructor"""
        input = """class Shape {
        Shape(){}
        Shape(float a, b) {
            this.a := a;
            this.b := b;
        }
        }"""
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[MethodDecl(name=Id("<init>"),kind=Instance(),param=[],body=Block([],[]),returnType=None),MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=FloatType()),VarDecl(variable=Id("b"),varType=FloatType())],returnType=None,body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("a")),exp=Id("a")),Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("b")),exp=Id("b"))]))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_many_class_with_parents_name(self):
        """Simple program with 3 class that has parentname"""
        input = """
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
                return this.length*this.width/2;
            }
        }
        """
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("length"),varType=FloatType())),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("width"),varType=FloatType())),MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("length"),varType=FloatType()),VarDecl(variable=Id("width"),varType=FloatType())],returnType=None,body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),exp=Id("length")),Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("width")),exp=Id("width"))]))]),ClassDecl(classname=Id("Rectangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))))]))]),ClassDecl(classname=Id("Triangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="/",left=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))),right=IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_class_with_three_member(self):
        """Simple program with 1 class that has memberlist: constructor, attribute declaration and method declaration """
        input = """class Shape {
        float area;
        final static string name = "hinh";
        Shape(float a, b) {
            this.a := a;
            this.b := b;
        }
        float getArea(){
            return a*b;
        }
        }"""
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("area"),varType=FloatType())),AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("name"),constType=StringType(),value=StringLiteral("hinh"))),MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=FloatType()),VarDecl(variable=Id("b"),varType=FloatType())],returnType=None,body=Block([],[Assign(FieldAccess(obj=SelfLiteral(),fieldname=Id("a")),exp=Id("a")),Assign(FieldAccess(obj=SelfLiteral(),fieldname=Id("b")),exp=Id("b"))])),MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(BinaryOp("*",left=Id("a"),right=Id("b")))]))])]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_all_valid_attribute_declaration(self):
        """Simple program with all kinds of attribute declaration"""
        input = """class attributedecl {
                    static final int numOfclass = 1;
                    final static float numOfclass2 = 1.0;
                    static string text = "abc";
                    final boolean a = true;
                    float[2] arr;
                    int[5] a = {1,2,3,4,5};
                }
                """
        expect = str(Program([ClassDecl(classname=Id("attributedecl"),memlist=[AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("numOfclass"),constType=IntType(),value=IntLiteral(1))),AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("numOfclass2"),constType=FloatType(),value=FloatLiteral(1.0))),AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("text"),varType=StringType(),varInit=StringLiteral("abc"))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("a"),constType=BoolType(),value=BooleanLiteral(True))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("arr"),varType=ArrayType(size=2,eleType=FloatType()))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("a"),varType=ArrayType(size=5,eleType=IntType()),varInit=ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])))])]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_mutable_int_attribute_declaration(self):
        """This class has some integer mutable attributes"""
        input = """
                class mutableintatt {
                    static int numOfclass = 1;
                    int numOfclass2 = 2;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("mutableintatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("numOfclass"),varType=IntType(),varInit=IntLiteral(1))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("numOfclass2"),varType=IntType(),varInit=IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_mutable_float_attribute_declaration(self):
        """This class has some float mutable attributes"""
        input = """
                class mutablefloatatt {
                    static float numOfclass = 1.0;
                    float numOfclass2 = 1.0e-12;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("mutablefloatatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("numOfclass"),varType=FloatType(),varInit=FloatLiteral(1.0))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("numOfclass2"),varType=FloatType(),varInit=FloatLiteral(1.0e-12)))])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_mutable_boolean_attribute_declaration(self):
        """This class has some boolean mutable attributes"""
        input = """
                class mutableboolatt {
                    static boolean a = true;
                    boolean b = false;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("mutableboolatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("a"),varType=BoolType(),varInit=BooleanLiteral(True))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("b"),varType=BoolType(),varInit=BooleanLiteral(False)))])]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_mutable_string_attribute_declaration(self):
        """This class has some boolean mutable attributes"""
        input = """
                class mutablestringatt {
                    static string text = "abc";
                    string text2 = "cde asd";
                }
                """
        expect = str(Program([ClassDecl(classname=Id("mutablestringatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("text"),varType=StringType(),varInit=StringLiteral("abc"))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("text2"),varType=StringType(),varInit=StringLiteral("cde asd")))])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_valid_immutable_int_attribute_declaration(self):
        """This class has some integer immutable attributes"""
        input = """
                class immutableintatt {
                    final static int numOfclass = 1;
                    int numOfclass2 = 2;
                    final int numOfclass3 = 3;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("immutableintatt"),memlist=[AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("numOfclass"),constType=IntType(),value=IntLiteral(1))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("numOfclass2"),varType=IntType(),varInit=IntLiteral(2))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("numOfclass3"),constType=IntType(),value=IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_valid_immutable_float_attribute_declaration(self):
        """This class has some float immutable attributes"""
        input = """
                class immutablefloatatt {
                    static float numOfclass = 1.0;
                    float numOfclass2 = 1.0e-12;
                    final float numOfclass3 = 3.;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("immutablefloatatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("numOfclass"),varType=FloatType(),varInit=FloatLiteral(1.0))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("numOfclass2"),varType=FloatType(),varInit=FloatLiteral(1e-12))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("numOfclass3"),constType=FloatType(),value=FloatLiteral(3.0)))])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_valid_immutable_boolean_attribute_declaration(self):
        """This class has some boolean immutable attributes"""
        input = """
                class immutableboolatt {
                    static boolean a = true;
                    boolean b = false;
                    final boolean numOfclass3 = true;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("immutableboolatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("a"),varType=BoolType(),varInit=BooleanLiteral(True))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("b"),varType=BoolType(),varInit=BooleanLiteral(False))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("numOfclass3"),constType=BoolType(),value=BooleanLiteral(True)))])]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_valid_immutable_string_attribute_declaration(self):
        """This class has some string immutable attributes"""
        input = """
                class immutablestringatt {
                    static string text = "abc";
                    string text2 = "cde asd";
                    final string text3 = "immutable attribute";
                }
                """
        expect = str(Program([ClassDecl(classname=Id("immutablestringatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("text"),varType=StringType(),varInit=StringLiteral("abc"))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("text2"),varType=StringType(),varInit=StringLiteral("cde asd"))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("text3"),constType=StringType(),value=StringLiteral("immutable attribute")))])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_valid_array_type_attribute_declaration(self):
        """This class has some array type immutable attributes"""
        input = """
                class immutablearraytypeatt {
                    static int[5] a = {1,2,3,4,5};
                    final static float[2] b = {1.0,2.2e-2};
                    final string[2] text = {"immutable attribute","mutable attribute"};
                    static final boolean[1] c = {true};
                    int[2] d ={1,6};
                }
                """
        expect = str(Program([ClassDecl(classname=Id("immutablearraytypeatt"),memlist=[AttributeDecl(kind=Static(),decl=VarDecl(variable=Id("a"),varType=ArrayType(size=5,eleType=IntType()),varInit=ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))),AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("b"),constType=ArrayType(size=2,eleType=FloatType()),value=ArrayLiteral([FloatLiteral(1.0),FloatLiteral(0.022)]))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("text"),constType=ArrayType(size=2,eleType=StringType()),value=ArrayLiteral([StringLiteral("immutable attribute"), StringLiteral("mutable attribute")]))),AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("c"),constType=ArrayType(size=1,eleType=BoolType()),value=ArrayLiteral([BooleanLiteral(True)]))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("d"),varType=ArrayType(size=2,eleType=IntType()),varInit=ArrayLiteral([IntLiteral(1),IntLiteral(6)])))])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_empty_method(self):
        """This class has 5 empty methods"""
        input = """
                class emptymethod1 {
                    int empty1(){}
                    float empty2(){}
                    boolean empty3(){}
                    string empty4(){}
                    void empty5(){}
                }
                """
        expect = str(Program([ClassDecl(classname=Id("emptymethod1"),memlist=[MethodDecl(name=Id("empty1"),kind=Instance(),param=[],returnType=IntType(),body=Block([],[])),MethodDecl(name=Id("empty2"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("empty3"),kind=Instance(),param=[],returnType=BoolType(),body=Block([],[])),MethodDecl(name=Id("empty4"),kind=Instance(),param=[],returnType=StringType(),body=Block([],[])),MethodDecl(name=Id("empty5"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_empty_static_method(self):
        """This class has 5 empty static methods"""
        input = """
                class emptymethod1 {
                    static int empty1(){}
                    static float empty2(){}
                    static boolean empty3(){}
                    static string empty4(){}
                    static void empty5(){}
                }
                """
        expect = str(Program([ClassDecl(classname=Id("emptymethod1"),memlist=[MethodDecl(name=Id("empty1"),kind=Static(),param=[],returnType=IntType(),body=Block([],[])),MethodDecl(name=Id("empty2"),kind=Static(),param=[],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("empty3"),kind=Static(),param=[],returnType=BoolType(),body=Block([],[])),MethodDecl(name=Id("empty4"),kind=Static(),param=[],returnType=StringType(),body=Block([],[])),MethodDecl(name=Id("empty5"),kind=Static(),param=[],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_static_method_with_one_parameter(self):
        """This class has 5 static methods that has 1 parameter"""
        input = """
                class staticmethodhas1parameter {
                    static int para(int parameter){}
                    static float para1(float parameter){}
                    static boolean para2(string parameter){}
                    static string para3(boolean parameter){}
                    static void para4(int[5] parameter){}
                }
                """
        expect = str(Program([ClassDecl(classname=Id("staticmethodhas1parameter"),memlist=[MethodDecl(name=Id("para"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=IntType())],returnType=IntType(),body=Block([],[])),MethodDecl(name=Id("para1"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=FloatType())],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("para2"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=StringType())],returnType=BoolType(),body=Block([],[])),MethodDecl(name=Id("para3"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=BoolType())],returnType=StringType(),body=Block([],[])),MethodDecl(name=Id("para4"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=ArrayType(size=5,eleType=IntType()))],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_static_method_with_many_parameters_in_same_type(self):
        """This class has 5 static methods that has many parameters in the same type"""
        input = """
                class staticmethodhas1parameter {
                    static int para(int parameter, parameter2){}
                    static float para1(float parameter, parameter2){}
                    static boolean para2(string parameter, parameter2){}
                    static string para3(boolean parameter, parameter2){}
                    static void para4(int[5] parameter, parameter2){}
                }
                """
        expect = str(Program([ClassDecl(classname=Id("staticmethodhas1parameter"),memlist=[MethodDecl(name=Id("para"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=IntType()),VarDecl(variable=Id("parameter2"),varType=IntType())],returnType=IntType(),body=Block([],[])),MethodDecl(name=Id("para1"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=FloatType()),VarDecl(variable=Id("parameter2"),varType=FloatType())],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("para2"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=StringType()),VarDecl(variable=Id("parameter2"),varType=StringType())],returnType=BoolType(),body=Block([],[])),MethodDecl(name=Id("para3"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=BoolType()),VarDecl(variable=Id("parameter2"),varType=BoolType())],returnType=StringType(),body=Block([],[])),MethodDecl(name=Id("para4"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=ArrayType(size=5,eleType=IntType())),VarDecl(variable=Id("parameter2"),varType=ArrayType(size=5,eleType=IntType()))],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_static_method_with_many_parameters_in_different_type(self):
        """This class has 5 static methods that has many parameters in different types"""
        input = """
                class staticmethodhasmanyparameter_differenttype {
                    static int para(int parameter, parameter2; float para3,para4){}
                    static float para1(float parameter, parameter2; string para5,para6){}
                    static boolean para2(string parameter, parameter2; int a,b,c){}
                    static string para3(boolean parameter, parameter2; int[2] arrays){}
                    static void para4(int[5] parameter, parameter2;int a,b;float c,d){}
                }
                """
        expect = str(Program([ClassDecl(classname=Id("staticmethodhasmanyparameter_differenttype"),memlist=[MethodDecl(name=Id("para"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=IntType()),VarDecl(variable=Id("parameter2"),varType=IntType()),VarDecl(variable=Id("para3"),varType=FloatType()),VarDecl(variable=Id("para4"),varType=FloatType())],returnType=IntType(),body=Block([],[])),MethodDecl(name=Id("para1"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=FloatType()),VarDecl(variable=Id("parameter2"),varType=FloatType()),VarDecl(variable=Id("para5"),varType=StringType()),VarDecl(variable=Id("para6"),varType=StringType())],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("para2"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=StringType()),VarDecl(variable=Id("parameter2"),varType=StringType()),VarDecl(variable=Id("a"),varType=IntType()),VarDecl(variable=Id("b"),varType=IntType()),VarDecl(variable=Id("c"),varType=IntType())],returnType=BoolType(),body=Block([],[])),MethodDecl(name=Id("para3"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=BoolType()),VarDecl(variable=Id("parameter2"),varType=BoolType()),VarDecl(variable=Id("arrays"),varType=ArrayType(size=2,eleType=IntType()))],returnType=StringType(),body=Block([],[])),MethodDecl(name=Id("para4"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=ArrayType(size=5,eleType=IntType())),VarDecl(variable=Id("parameter2"),varType=ArrayType(size=5,eleType=IntType())),VarDecl(variable=Id("a"),varType=IntType()),VarDecl(variable=Id("b"),varType=IntType()),VarDecl(variable=Id("c"),varType=FloatType()),VarDecl(variable=Id("d"),varType=FloatType())],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_empty_para_static_int_method_with_blockstmt(self):
        """This class has 1 static methods with blockstmt and no para"""
        input = """
                class emptymethod1 {
                    static int empty1(){
                        int a;
                        return a;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("emptymethod1"),memlist=[MethodDecl(name=Id("empty1"),kind=Static(),param=[],returnType=IntType(),body=Block([VarDecl(variable=Id("a"),varType=IntType())],[Return(expr=Id("a"))]))])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_empty_para_static_float_method_with_blockstmt(self):
        """This class has 1 static methods with blockstmt and no para"""
        input = """
                class emptymethod1 {
                    static float empty2(){
                        float b;
                        return b;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("emptymethod1"),memlist=[MethodDecl(name=Id("empty2"),kind=Static(),param=[],returnType=FloatType(),body=Block([VarDecl(variable=Id("b"),varType=FloatType())],[Return(expr=Id("b"))]))])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_empty_para_static_boolean_method_with_blockstmt(self):
        """This class has 1 static methods with blockstmt and no para"""
        input = """
                class emptymethod1 {
                    static boolean empty3(){
                        boolean abc = true;
                        return abc;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("emptymethod1"),memlist=[MethodDecl(name=Id("empty3"),kind=Static(),param=[],returnType=BoolType(),body=Block([VarDecl(variable=Id("abc"),varType=BoolType(),varInit=BooleanLiteral(True))],[Return(expr=Id("abc"))]))])]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_empty_para_static_string_method_with_blockstmt(self):
        """This class has 1 static methods with blockstmt and no para"""
        input = """
                class emptymethod1 {
                    static string empty4(){
                        string abc = "string lit";
                        return abc;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("emptymethod1"),memlist=[MethodDecl(name=Id("empty4"),kind=Static(),param=[],returnType=StringType(),body=Block([VarDecl(variable=Id("abc"),varType=StringType(),varInit=StringLiteral("string lit"))],[Return(expr=Id("abc"))]))])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_static_method_with_one_parameter_and_blockstmt(self):
        """This class has static methods that has 1 parameter and a blockstmt"""
        input = """
                class staticmethodhas1parameter {
                    static int para(int parameter){
                        parameter := 5 + 5;
                        return parameter;
                    }
                    static float para1(float parameter1){
                        return parameter - 1.0;
                    }
                    static boolean para2(boolean parameter2){
                        parameter2 := false;
                        return parameter || true;
                    }
                    static string para3(string parameter3){
                        parameter3 := "this is a string";
                        return parameter ^ "ABC";
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("staticmethodhas1parameter"),memlist=[MethodDecl(name=Id("para"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=IntType())],returnType=IntType(),body=Block([],[Assign(lhs=Id("parameter"),exp=BinaryOp(op="+",left=IntLiteral(5),right=IntLiteral(5))),Return(expr=Id("parameter"))])),MethodDecl(name=Id("para1"),kind=Static(),param=[VarDecl(variable=Id("parameter1"),varType=FloatType())],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="-",left=Id("parameter"),right=FloatLiteral(1.0)))])),MethodDecl(name=Id("para2"),kind=Static(),param=[VarDecl(variable=Id("parameter2"),varType=BoolType())],returnType=BoolType(),body=Block([],[Assign(lhs=Id("parameter2"),exp=BooleanLiteral(False)),Return(expr=BinaryOp(op="||",left=Id("parameter"),right=BooleanLiteral(True)))])),MethodDecl(name=Id("para3"),kind=Static(),param=[VarDecl(variable=Id("parameter3"),varType=StringType())],returnType=StringType(),body=Block([],[Assign(lhs=Id("parameter3"),exp=StringLiteral("this is a string")),Return(expr=BinaryOp(op="^",left=Id("parameter"),right=StringLiteral("ABC")))]))])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_static_method_with_many_parameters_and_a_blockstmt(self):
        """This class has static methods that has many parameters and a blockstmt"""
        input = """
                class staticmethodhasmanyparameter {
                    static int para(int parameter, parameter2){
                        int result =  parameter - parameter2;
                        return result;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("staticmethodhasmanyparameter"),memlist=[MethodDecl(name=Id("para"),kind=Static(),param=[VarDecl(variable=Id("parameter"),varType=IntType()),VarDecl(variable=Id("parameter2"),varType=IntType())],returnType=IntType(),body=Block([VarDecl(variable=Id("result"),varType=IntType(),varInit=BinaryOp(op="-",left=Id("parameter"),right=Id("parameter2")))],[Return(expr=Id("result"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_constructor(self):
        """This class has a constructor"""
        input = """
                class square {
                    square (float radius) {
                        this.radius := radius;
                    }
                    float area(float radius) {
                        return radius*3.14*radius;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("square"),memlist=[MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("radius"),varType=FloatType())],returnType=None,body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("radius")),exp=Id("radius"))])),MethodDecl(name=Id("area"),kind=Instance(),param=[VarDecl(variable=Id("radius"),varType=FloatType())],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="*",left=BinaryOp(op="*",left=Id("radius"),right=FloatLiteral(3.14)),right=Id("radius")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_complete_method(self):
        """This class has a complete method"""
        input = """
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
                """
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("length"),varType=FloatType())),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("width"),varType=FloatType())),MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("length"),varType=FloatType()),VarDecl(variable=Id("width"),varType=FloatType())],returnType=None,body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),exp=Id("length")),Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("width")),exp=Id("width"))]))]),ClassDecl(classname=Id("Rectangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))))]))]),ClassDecl(classname=Id("Triangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="/",left=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))),right=IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_valid_int_array_type(self):
        """This class has array type att and the method has array type parameter """
        input = """
                class example {
                    int[5] array_type_attribute;
                    float method(float a,b; int[2] c){}
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=5,eleType=IntType()))),MethodDecl(name=Id("method"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=FloatType()),VarDecl(variable=Id("b"),varType=FloatType()),VarDecl(variable=Id("c"),varType=ArrayType(size=2,eleType=IntType()))],returnType=FloatType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_valid_float_array_type(self):
        """This class has array type att"""
        input = """
                class example {
                    float[5] array_type_attribute;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=5,eleType=FloatType())))])]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_valid_boolean_array_type(self):
        """This class has array type att"""
        input = """
                class example {
                    boolean[5] array_type_attribute;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=5,eleType=BoolType())))])]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_valid_string_array_type(self):
        """This class has array type att"""
        input = """
                class example {
                    string[5] array_type_attribute;
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=5,eleType=StringType())))])]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_valid_int_array_type_with_varinit(self):
        """This class has array type att with varinit"""
        input = """
                class example {
                    int[2] array_type_attribute = {1,2};
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=2,eleType=IntType()),varInit=ArrayLiteral([IntLiteral(1),IntLiteral(2)])))])]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_valid_float_array_type_with_varinit(self):
        """This class has array type att with varinit"""
        input = """
                class example {
                    float[2] array_type_attribute = {1.0,2.0};
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=2,eleType=FloatType()),varInit=ArrayLiteral([FloatLiteral(1.0),FloatLiteral(2.0)])))])]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_valid_boolean_array_type_with_varinit(self):
        """This class has array type att with varinit"""
        input = """
                class example {
                    boolean[2] array_type_attribute = {true, false};
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=2,eleType=BoolType()),varInit=ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)])))])]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_valid_string_array_type_with_varinit(self):
        """This class has array type att with varinit"""
        input = """
                class example {
                    string[2] array_type_attribute = {"string 1", "string 2"};
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("array_type_attribute"),varType=ArrayType(size=2,eleType=StringType()),varInit=ArrayLiteral([StringLiteral("string 1"),StringLiteral("string 2")])))])]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_less_than_exp(self):
        """This class has valid Less than expression"""
        input = """
                class example{
                void main(){
                    if x < y then continue;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=BinaryOp(op="<",left=Id("x"),right=Id("y")),thenStmt=Continue())]))])]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_less_than_or_eq_exp(self):
        """This class has valid Less than or eq expression"""
        input = """
                class example{
                void main(){
                    if x <= y then continue;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=BinaryOp(op="<=",left=Id("x"),right=Id("y")),thenStmt=Continue())]))])]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_greater_than_exp(self):
        """This class has valid greater than expression"""
        input = """
                class example{
                void main(){
                    if x > y then continue;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=BinaryOp(op=">",left=Id("x"),right=Id("y")),thenStmt=Continue())]))])]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_greater_than_or_eq_exp(self):
        """This class has valid greater than or eq expression"""
        input = """
                class example{
                void main(){
                    if x >= y then continue;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=BinaryOp(op=">=",left=Id("x"),right=Id("y")),thenStmt=Continue())]))])]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_is_equal_exp(self):
        """This class has valid is equal expression"""
        input = """
                class example{
                void main(){
                    if x == y then continue;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=BinaryOp(op="==",left=Id("x"),right=Id("y")),thenStmt=Continue())]))])]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_not_equal_exp(self):
        """This class has valid not equal expression"""
        input = """
                class example{
                void main(){
                    if x != y then continue;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=BinaryOp(op="!=",left=Id("x"),right=Id("y")),thenStmt=Continue())]))])]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_binary_plus(self):
        """This class has valid plus exp"""
        input = """
                class example{
                void main(){
                    int a = a + 4;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BinaryOp(op="+",left=Id("a"),right=IntLiteral(4)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_binary_minus(self):
        """This class has valid minus exp"""
        input = """
                class example{
                void main(){
                    int a = a - 4;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BinaryOp(op="-",left=Id("a"),right=IntLiteral(4)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_binary_mul(self):
        """This class has valid mul exp"""
        input = """
                class example{
                void main(){
                    int a = a * 4;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BinaryOp(op="*",left=Id("a"),right=IntLiteral(4)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_binary_idiv(self):
        """This class has valid idiv exp"""
        input = """
                class example{
                void main(){
                    int a = a \\ 4;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BinaryOp(op="\\",left=Id("a"),right=IntLiteral(4)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_binary_fdiv(self):
        """This class has valid fdiv exp"""
        input = """
                class example{
                void main(){
                    int a = a / 4;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BinaryOp(op="/",left=Id("a"),right=IntLiteral(4)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_binary_mod(self):
        """This class has valid mod exp"""
        input = """
                class example{
                void main(){
                    int a = a % 4;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BinaryOp(op="%",left=Id("a"),right=IntLiteral(4)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_binary_concat(self):
        """This class has valid string concatenation expression"""
        input = """
                class example{
                void main(){
                    string x = "abc",y = "cde";
                    string result;
                    result := x ^ y;
                    return result;                    
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("x"),varType=StringType(),varInit=StringLiteral("abc")),VarDecl(variable=Id("y"),varType=StringType(),varInit=StringLiteral("cde")),VarDecl(variable=Id("result"),varType=StringType())],[Assign(lhs=Id("result"),exp=BinaryOp(op="^",left=Id("x"),right=Id("y"))),Return(expr=Id("result"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_unary_plus(self):
        """This class has valid unary add exp"""
        input = """
                class example{
                void main(){
                    int a = +3;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=UnaryOp(op="+",body=IntLiteral(3)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_unary_minus(self):
        """This class has valid unary minus exp"""
        input = """
                class example{
                void main(){
                    int a = -3;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=UnaryOp(op="-",body=IntLiteral(3)))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_not_exp(self):
        """This class has valid not exp"""
        input = """
                class example{
                void main(){
                    int a = !b;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=UnaryOp(op="!",body=Id("b")))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_complex_not_exp(self):
        """This class has valid not exp"""
        input = """
                class example{
                void main(){
                    int a = true;
                    int b = !a;
                    if b == a then return b;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BooleanLiteral(True)),VarDecl(variable=Id("b"),varType=IntType(),varInit=UnaryOp(op="!",body=Id("a")))],[If(expr=BinaryOp(op="==",left=Id("b"),right=Id("a")),thenStmt=Return(expr=Id("b")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_double_not(self):
        """This class has a double not exp"""
        input = """
                class example{
                void main(){
                    int a = true;
                    int b = !!a;
                    if b == a then return b;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=BooleanLiteral(True)),VarDecl(variable=Id("b"),varType=IntType(),varInit=UnaryOp(op="!", body=UnaryOp(op="!",body=Id("a"))))],[If(expr=BinaryOp(op="==",left=Id("b"),right=Id("a")),thenStmt=Return(expr=Id("b")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_all_indexop(self):
        """This class has valid index operator"""
        input = """
                class example{
                void main(){
                    a[3+x.foo(2)] := a[b[2]] +3;
                    x.b := x.m()[3];   
                    a[3] := b[2];
                    a[1] := 0;
                    a[2] := 5+5;  
                    a[1] := b[3] - b[2];          
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=ArrayCell(arr=Id("a"),idx=BinaryOp(op="+",left=IntLiteral(3),right=CallExpr(obj=Id("x"),method=Id("foo"),param=[IntLiteral(2)]))),exp=BinaryOp(op="+",left=ArrayCell(arr=Id("a"),idx=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),right=IntLiteral(3))),Assign(lhs=FieldAccess(obj=Id("x"),fieldname=Id("b")),exp=ArrayCell(arr=CallExpr(obj=Id("x"),method=Id("m"),param=[]),idx=IntLiteral(3))),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(3)),exp=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(1)),exp=IntLiteral(0)),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(2)),exp=BinaryOp(op="+",left=IntLiteral(5),right=IntLiteral(5))),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(1)),exp=BinaryOp(op="-",left=ArrayCell(arr=Id("b"),idx=IntLiteral(3)),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_simple_indexop(self):
        """This class has valid index operator"""
        input = """
                class example{
                void main(){
                    int[2] a;  
                    a[0] := 1;
                    a[1] := 2;
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=ArrayType(size=2,eleType=IntType()))],[Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(0)),exp=IntLiteral(1)),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(1)),exp=IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_complex_indexop(self):
        """This class has valid index operator"""
        input = """
                class example{
                void main(){
                    a[3+x.foo(2)] := a[b[2]] +3;
                    x.b := x.m()[3]; 
                }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=ArrayCell(arr=Id("a"),idx=BinaryOp(op="+",left=IntLiteral(3),right=CallExpr(obj=Id("x"),method=Id("foo"),param=[IntLiteral(2)]))),exp=BinaryOp(op="+",left=ArrayCell(arr=Id("a"),idx=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),right=IntLiteral(3))),Assign(lhs=FieldAccess(obj=Id("x"),fieldname=Id("b")),exp=ArrayCell(arr=CallExpr(obj=Id("x"),method=Id("m"),param=[]),idx=IntLiteral(3)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_simple_indexop_with_plus(self):
        """This class has valid index operator with plus binary op"""
        input = """
                class example{
                    void main(){
                        a+b[2] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=BinaryOp(op="+",left=Id("a"),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_simple_indexop_with_minus(self):
        """This class has valid index operator with minus binary op"""
        input = """
                class example{
                    void main(){
                        a-b[2] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=BinaryOp(op="-",left=Id("a"),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_simple_indexop_with_mul(self):
        """This class has valid index operator with mul binary op"""
        input = """
                class example{
                    void main(){
                        a*b[2] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=BinaryOp(op="*",left=Id("a"),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_simple_indexop_with_fdiv(self):
        """This class has valid index operator with float div binary op"""
        input = """
                class example{
                    void main(){
                        a/b[2] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=BinaryOp(op="/",left=Id("a"),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_simple_indexop_with_idiv(self):
        """This class has valid index operator with integer div binary op"""
        input = """
                class example{
                    void main(){
                        a\\b[2] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=BinaryOp(op="\\",left=Id("a"),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_simple_indexop_with_mod(self):
        """This class has valid index operator with mod binary op"""
        input = """
                class example{
                    void main(){
                        a%b[2] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=BinaryOp(op="%",left=Id("a"),right=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_double_indexop(self):
        """This class has valid index operator"""
        input = """
                class example{
                    void main(){
                        a[b[2]] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=ArrayCell(arr=Id("a"),idx=ArrayCell(arr=Id("b"),idx=IntLiteral(2))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_triple_indexop(self):
        """This class has valid index operator"""
        input = """
                class example{
                    void main(){
                        a[b[c[2]]] := 3;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=ArrayCell(arr=Id("a"),idx=ArrayCell(arr=Id("b"),idx=ArrayCell(arr=Id("c"),idx=IntLiteral(2)))),exp=IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_valid_instance_attribute_access(self):
        """This class has valid instance attribute access"""
        input = """
                class example{
                    void main(){
                        this.foo := b;    
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("foo")),exp=Id("b"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_valid_static_attribute_access(self):
        """This class has valid static attribute access"""
        input = """
                class example{
                    void main(){
                        x.foo := a.b;       
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=FieldAccess(obj=Id("x"),fieldname=Id("foo")),exp=FieldAccess(obj=Id("a"),fieldname=Id("b")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_valid_instance_method_invocation(self):
        """This class has valid instance method invocation"""
        input = """
                class example{
                    void main(){
                        this.foo();        
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[CallStmt(obj=SelfLiteral(),method=Id("foo"),param=[])]))])]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_valid_static_method_invocation(self):
        """This class has valid static method invocation"""
        input = """
                class example{
                void main(){
                    x.foo() := a.b();  
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("example"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=CallExpr(obj=Id("x"),method=Id("foo"),param=[]),exp=CallExpr(obj=Id("a"),method=Id("b"),param=[]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_complex_member_access(self):
        """This class has valid member acceess"""
        input = """
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
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("s"),varType=ClassType(classname=Id("Shape")))],[Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Rectangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])]),Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Triangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_one_object_create(self):
        """This class has valid object create"""
        input = """
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("s"),varType=ClassType(classname=Id("Shape")))],[Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Rectangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_new_exp(self):
        """This class has valid object create"""
        input = """
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
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("s"),varType=ClassType(classname=Id("Shape")))],[Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Rectangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])]),Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Triangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_exp_callstmt(self):
        """This class has a callstatement"""
        input = """
        class main {
            int total(int a, b){
                main a;
                a.total(4,5);
            }
        }
        """
        expect = str(Program([ClassDecl(classname=Id("main"),memlist=[MethodDecl(name=Id("total"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=IntType()),VarDecl(variable=Id("b"),varType=IntType())],returnType=IntType(),body=Block([VarDecl(variable=Id("a"),varType=ClassType(classname=Id("main")))],[CallStmt(obj=Id("a"),method=Id("total"),param=[IntLiteral(4),IntLiteral(5)])]))])]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_exp_callexpr_as_varinit(self):
        """This class has callexpr as a varinit"""
        input = """
        class main {
            int total(int a, b){
                main a;
                int c = a.total(4,5);
            }
        }
        """
        expect = str(Program([ClassDecl(classname=Id("main"),memlist=[MethodDecl(name=Id("total"),kind=Instance(),param=[VarDecl(variable=Id("a"),varType=IntType()),VarDecl(variable=Id("b"),varType=IntType())],returnType=IntType(),body=Block([VarDecl(variable=Id("a"),varType=ClassType(classname=Id("main"))),VarDecl(variable=Id("c"),varType=IntType(),varInit=CallExpr(obj=Id("a"),method=Id("total"),param=[IntLiteral(4),IntLiteral(5)]))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_valid_empty_block_statement(self):
        """This class has empty block statement"""
        input = """
                class empty {
                    void emptyblock(){
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("empty"),memlist=[MethodDecl(name=Id("emptyblock"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_valid_block_statement_with_only_vardecllist(self):
        """This class has valid block statement declaration: with only variables"""
        input = """
                class Example2 {
                    void main(){
                        float r,s;
                        int[5] a,b;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("r"),varType=FloatType()),VarDecl(variable=Id("s"),varType=FloatType()),VarDecl(variable=Id("a"),varType=ArrayType(size=5,eleType=IntType())),VarDecl(variable=Id("b"),varType=ArrayType(size=5,eleType=IntType()))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_valid_block_statement_with_only_stmt(self):
        """This class has valid block statement declaration: with only stmts"""
        input = """
                class Example2 {
                    void main(){
                        r:=2.0;
                        continue;
                        return none;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=Id("r"),exp=FloatLiteral(2.0)),Continue(),Return(expr=Id("none"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_valid_method_block_stmt(self):
        """The method in this class has valid block statement"""
        input = """
                class Example2 {
                    void main(){
                        float r,s;
                        int[5] a,b;
                        r:=2.0;
                        s:=r*r*this.myPI;
                        a[0]:= s;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("r"),varType=FloatType()),VarDecl(variable=Id("s"),varType=FloatType()),VarDecl(variable=Id("a"),varType=ArrayType(size=5,eleType=IntType())),VarDecl(variable=Id("b"),varType=ArrayType(size=5,eleType=IntType()))],[Assign(lhs=Id("r"),exp=FloatLiteral(2.0)),Assign(lhs=Id("s"),exp=BinaryOp(op="*",left=BinaryOp(op="*",left=Id("r"),right=Id("r")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("myPI")))),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(0)),exp=Id("s"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_valid_method_block_stmt_with_comment(self):
        """The method in this class has valid block statement with comment inside of it"""
        input = """
                class Example2 {
                    void main(){
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
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("r"),varType=FloatType()),VarDecl(variable=Id("s"),varType=FloatType()),VarDecl(variable=Id("a"),varType=ArrayType(size=5,eleType=IntType())),VarDecl(variable=Id("b"),varType=ArrayType(size=5,eleType=IntType()))],[Assign(lhs=Id("r"),exp=FloatLiteral(2.0)),Assign(lhs=Id("s"),exp=BinaryOp(op="*",left=BinaryOp(op="*",left=Id("r"),right=Id("r")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("myPI")))),Assign(lhs=ArrayCell(arr=Id("a"),idx=IntLiteral(0)),exp=Id("s"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_asmstmt(self):
        """Test assignment statement"""
        input = """
                class Example2 {
                    void assignmentSTMT(){
                        this.aPI := 3.14;
                        value := x.foo(5);
                        l[3] := value * 2;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("assignmentSTMT"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("aPI")),exp=FloatLiteral(3.14)),Assign(lhs=Id("value"),exp=CallExpr(obj=Id("x"),method=Id("foo"),param=[IntLiteral(5)])),Assign(lhs=ArrayCell(arr=Id("l"),idx=IntLiteral(3)),exp=BinaryOp(op="*",left=Id("value"),right=IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_if_stmt(self):
        """Test if statement"""
        input = """
                class Example2 {
                    void ifelsestmt(){
                        if flag then
                            io.writeStrLn("Expression is true");
                        else
                            io.writeStrLn ("Expression is false");
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("ifelsestmt"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=Id("flag"),thenStmt=CallStmt(obj=Id("io"),method=Id("writeStrLn"),param=[StringLiteral("Expression is true")]),elseStmt=CallStmt(obj=Id("io"),method=Id("writeStrLn"),param=[StringLiteral("Expression is false")]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_if_stmt_without_else(self):
        """Test if statement without else part"""
        input = """
                 class Example2 {
                    void ifstmt(){
                        if flag then
                            io.writeStrLn("Expression is true");
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("ifstmt"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[If(expr=Id("flag"),thenStmt=CallStmt(obj=Id("io"),method=Id("writeStrLn"),param=[StringLiteral("Expression is true")]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_for_to_stmt(self):
        """Test for to statement"""
        input = """
                class Example2 {
                    void forto(){
                        for i := 1 to 100 do {
                            io.writeIntLn(i);
                            Intarray[i] := i + 1;
                        }
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("forto"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[For(id=Id("i"),expr1=IntLiteral(1),expr2=IntLiteral(100),up=True,loop=Block([],[CallStmt(obj=Id("io"),method=Id("writeIntLn"),param=[Id("i")]),Assign(ArrayCell(arr=Id("Intarray"),idx=Id("i")),exp=BinaryOp(op="+",left=Id("i"),right=IntLiteral(1)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_for_downto_stmt(self):
        """Test for downto statement"""
        input = """
                class Example2 {
                    void fordownto(){
                        for x := 5 downto 2 do
                            io.writeIntLn(x);
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("fordownto"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[For(id=Id("x"),expr1=IntLiteral(5),expr2=IntLiteral(2),up=False,loop=CallStmt(obj=Id("io"),method=Id("writeIntLn"),param=[Id("x")]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_for_downto_stmt_with_block_stmt(self):
        """Test for downto statement with block statement"""
        input = """
                class Example2 {
                    void fordownto(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            return x;
                        }
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("fordownto"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[For(id=Id("x"),expr1=IntLiteral(5),expr2=IntLiteral(2),up=False,loop=Block([],[CallStmt(obj=Id("io"),method=Id("writeIntLn"),param=[Id("x")]),Return(expr=Id("x"))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_for_to_stmt_with_block_stmt(self):
        """Test for to statement with block statement"""
        input = """
                class Example2 {
                    void forto(){
                        for x := 5 to 2 do {
                            io.writeIntLn(x);
                            return x;
                        }
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("forto"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[For(id=Id("x"),expr1=IntLiteral(5),expr2=IntLiteral(2),up=True,loop=Block([],[CallStmt(obj=Id("io"),method=Id("writeIntLn"),param=[Id("x")]),Return(expr=Id("x"))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_break_stmt(self):
        """Test break statement"""
        input = """
                class Example2 {
                    void breakstmt(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            if x == 3 then break;
                        }
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("breakstmt"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[For(id=Id("x"),expr1=IntLiteral(5),expr2=IntLiteral(2),up=False,loop=Block([],[CallStmt(obj=Id("io"),method=Id("writeIntLn"),param=[Id("x")]),If(expr=BinaryOp(op="==",left=Id("x"),right=IntLiteral(3)),thenStmt=Break())]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_continue_stmt(self):
        """Test continue statement"""
        input = """
                class Example2 {
                    void continuestmt(){
                        for x := 5 downto 2 do {
                            if x == 3 then continue;
                        }
                    }
                }
                """
        expect= str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("continuestmt"),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[For(id=Id("x"),expr1=IntLiteral(5),expr2=IntLiteral(2),up=False,loop=Block([],[If(expr=BinaryOp(op="==",left=Id("x"),right=IntLiteral(3)),thenStmt=Continue())]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_return_stmt(self):
        """Test return statement"""
        input = """
                class Example2 {
                    void returnstmt(){
                        int a = 5;
                        if a != 0 then return a; else return 0;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("returnstmt"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("a"),varType=IntType(),varInit=IntLiteral(5))],[If(expr=BinaryOp(op="!=",left=Id("a"),right=IntLiteral(0)),thenStmt=Return(expr=Id("a")),elseStmt=Return(expr=IntLiteral(0)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_method_invocation_stmt(self):
        """Test method invocation statement"""
        input = """
                class Shape {
                    static int getNumOfShape(){}
                }
                class Example2 {
                    void getSum(){
                        Shape s;
                        s.getNumOfShape();
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[MethodDecl(name=Id("getNumOfShape"),kind=Static(),param=[],returnType=IntType(),body=Block([],[]))]),ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("getSum"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("s"),varType=ClassType(classname=Id("Shape")))],[CallStmt(obj=Id("s"),method=Id("getNumOfShape"),param=[])]))])]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_object_create_stmt(self):
        """Test object create statement"""
        input = """
                class Shape {
                    static int getNumOfShape(){}
                }
                class Bob {
                }
                class Example2 {
                    void getSum(){
                        Shape s;
                        Bob a;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[MethodDecl(name=Id("getNumOfShape"),kind=Static(),param=[],returnType=IntType(),body=Block([],[]))]),ClassDecl(classname=Id("Bob"),memlist=[]),ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("getSum"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("s"),varType=ClassType(classname=Id("Shape"))),VarDecl(variable=Id("a"),varType=ClassType(classname=Id("Bob")))],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_valid_simple_program_one_class(self):
        """Simple program with 1 class"""
        input = """class simple1 {}"""
        expect = str(Program([ClassDecl(classname=Id("simple1"),memlist=[])]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_valid_simple_program_many_classes(self):
        """Simple program with many classes"""
        input = """class simple1 {}
                class simple2 {}
                class simple3 {}
                """
        expect = str(Program([ClassDecl(classname=Id("simple1"),memlist=[]),ClassDecl(classname=Id("simple2"),memlist=[]),ClassDecl(classname=Id("simple3"),memlist=[])]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_valid_program_rule_example_in_part_9_1(self):
        """Example program in part 9.1"""
        input = """
                class Example1 {
                    int factorial(int n){
                        if n == 0 then return 1; else return n * this.factorial(n - 1);
                    }
                    void main(){
                        int x;
                        x := io.readInt();
                        io.writeIntLn(this.factorial(x));
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Example1"),memlist=[MethodDecl(name=Id("factorial"),kind=Instance(),param=[VarDecl(variable=Id("n"),varType=IntType())],returnType=IntType(),body=Block([],[If(expr=BinaryOp(op="==",left=Id("n"),right=IntLiteral(0)),thenStmt=Return(IntLiteral(1)),elseStmt=Return(expr=BinaryOp(op="*",left=Id("n"),right=CallExpr(obj=SelfLiteral(),method=Id("factorial"),param=[BinaryOp(op="-",left=Id("n"),right=IntLiteral(1))]))))])),MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("x"),varType=IntType())],[Assign(lhs=Id("x"),exp=CallExpr(obj=Id("io"),method=Id("readInt"),param=[])),CallStmt(obj=Id("io"),method=Id("writeIntLn"),param=[CallExpr(obj=SelfLiteral(),method=Id("factorial"),param=[Id("x")])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_valid_program_rule_example_in_part_9_2(self):
        """Example program in part 9.2"""
        input = """
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
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("length"),varType=FloatType())),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("width"),varType=FloatType())),MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[])),MethodDecl(name=Id("<init>"),kind=Instance(),param=[VarDecl(variable=Id("length"),varType=FloatType()),VarDecl(variable=Id("width"),varType=FloatType())],returnType=None,body=Block([],[Assign(lhs=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),exp=Id("length")),Assign(FieldAccess(obj=SelfLiteral(),fieldname=Id("width")),exp=Id("width"))]))]),ClassDecl(classname=Id("Rectangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))))]))]),ClassDecl(classname=Id("Triangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="/",left=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))),right=IntLiteral(2)))]))]),ClassDecl(classname=Id("Example2"),memlist=[MethodDecl(name=Id("main"),kind=Instance(),param=[],returnType=VoidType(),body=Block([VarDecl(variable=Id("s"),varType=ClassType(classname=Id("Shape")))],[Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Rectangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])]),Assign(lhs=Id("s"),exp=NewExpr(classname=Id("Triangle"),param=[IntLiteral(3),IntLiteral(4)])),CallStmt(obj=Id("io"),method=Id("writeFloatLn"),param=[CallExpr(obj=Id("s"),method=Id("getArea"),param=[])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_program_rule_with_example_in_part_2_1(self):
        """Test program rule with the example in part 2.1"""
        input = """class Shape {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                float length,width;
                static int getNumOfShape() {
                    return numOfShape;
                    }
                }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                """
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[AttributeDecl(kind=Static(),decl=ConstDecl(constant=Id("numOfShape"),constType=IntType(),value=IntLiteral(0))),AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("immuAttribute"),constType=IntType(),value=IntLiteral(0))),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("length"),varType=FloatType())),AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id("width"),varType=FloatType())),MethodDecl(name=Id("getNumOfShape"),kind=Static(),param=[],returnType=IntType(),body=Block([],[Return(expr=Id("numOfShape"))]))]),ClassDecl(classname=Id("Rectangle"),parentname=Id("Shape"),memlist=[MethodDecl(name=Id("getArea"),kind=Instance(),param=[],returnType=FloatType(),body=Block([],[Return(expr=BinaryOp(op="*",left=FieldAccess(obj=SelfLiteral(),fieldname=Id("length")),right=FieldAccess(obj=SelfLiteral(),fieldname=Id("width"))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 399))
