from typing import Callable
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program_01(self):
        input = r"""
        class Child {}
        """
        expect = str(Program([ClassDecl(Id("Child"), [])]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_simple_program_02(self):
        input = r"""
        class Child extends Parent { }
        """
        expect = str(Program([ClassDecl(Id("Child"), [], Id("Parent"))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program_03(self):
        input = r"""
        class Child extends Parent { 
            int foo() { }
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Child"),
                parentname=Id("Parent"),
                memlist=[MethodDecl(
                    kind=Instance(),
                    name=Id("foo"),
                    param=[],
                    body=Block([], []),
                    returnType=IntType()
                )],
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_simple_program_04(self):
        input = r"""
        class Abc {}
        class Child extends Parent { }
        """
        expect = str(Program([
            ClassDecl(Id("Abc"), []),
            ClassDecl(Id("Child"), [], Id("Parent"))
        ]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_simple_program_05(self):
        input = r"""
        class Parent {}
        class Child extends Parent { }
        class main extends Child {}
        """
        expect = str(Program([
            ClassDecl(Id("Parent"), []),
            ClassDecl(Id("Child"), [], Id("Parent")),
            ClassDecl(Id("main"), [], Id("Child"))
        ]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_simple_program_06(self):
        input = r"""
        class Child extends Parent { 
            void main() {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Child"),
                parentname=Id("Parent"),
                memlist=[MethodDecl(
                    kind=Static(),
                    name=Id("main"),
                    param=[],
                    body=Block([], []),
                    returnType=VoidType()
                )],
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simple_program_07(self):
        input = r"""
        class Abc {
            Abc() {}
        }
        class Child extends Parent { 
            Child() {
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Abc"),
                memlist=[MethodDecl(
                    kind=Instance(),
                    name=Id("<init>"),
                    param=[],
                    body=Block([], []),
                    returnType=None
                )],
            ),
            ClassDecl(
                classname=Id("Child"),
                parentname=Id("Parent"),
                memlist=[MethodDecl(
                    kind=Instance(),
                    name=Id("<init>"),
                    param=[],
                    body=Block([], []),
                    returnType=None
                )],
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_simple_program_08(self):
        input = r"""
        class Child extends Parent { 
            Child(int a, b) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Child"),
                parentname=Id("Parent"),
                memlist=[MethodDecl(
                    kind=Instance(),
                    name=Id("<init>"),
                    param=[
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ],
                    body=Block([], []),
                    returnType=None
                )])
        ]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_simple_program_09(self):
        input = r"""
        class Child extends Parent { 
            Child(int a; boolean c) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Child"),
                parentname=Id("Parent"),
                memlist=[MethodDecl(
                    kind=Instance(),
                    name=Id("<init>"),
                    param=[
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("c"), BoolType())
                    ],
                    body=Block([], []),
                    returnType=None
                )])
        ]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_simple_program_10(self):
        input = r"""
        class Child extends Parent { 
            Child(int a, b; float c,d) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Child"),
                parentname=Id("Parent"),
                memlist=[MethodDecl(
                    kind=Instance(),
                    name=Id("<init>"),
                    param=[
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                        VarDecl(Id("c"), FloatType()),
                        VarDecl(Id("d"), FloatType())
                    ],
                    body=Block([], []),
                    returnType=None
                )])
        ]))
        self.assertTrue(TestAST.test(input, expect, 310))

    # -------------------------------------------------------------------------

    def test_declaration_01(self):
        input = r"""
        class main {
            int a;
        }
        """
        expect = str(Program(
            [ClassDecl(Id("main"), [AttributeDecl(
                Instance(), VarDecl(Id("a"), IntType()))])]
        ))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_declaration_02(self):
        input = r"""
        class main {
            int a;
            final int b;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                AttributeDecl(Instance(), ConstDecl(
                    Id("b"), IntType(), None))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_declaration_03(self):
        input = r"""
        class main {
            int a,b;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                AttributeDecl(Instance(), VarDecl(Id("b"), IntType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_declaration_04(self):
        input = r"""
        class main {
            float a,b;
            boolean c;
            string d;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(Instance(), VarDecl(Id("a"), FloatType())),
                AttributeDecl(Instance(), VarDecl(Id("b"), FloatType())),
                AttributeDecl(Instance(), VarDecl(Id("c"), BoolType())),
                AttributeDecl(Instance(), VarDecl(Id("d"), StringType())),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_declaration_05(self):
        input = r"""
        class main {
            float a,b;
            static boolean c;
            final string d="hello";
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(Instance(), VarDecl(Id("a"), FloatType())),
                AttributeDecl(Instance(), VarDecl(Id("b"), FloatType())),
                AttributeDecl(Static(), VarDecl(Id("c"), BoolType())),
                AttributeDecl(Instance(), ConstDecl(
                    Id("d"), StringType(), StringLiteral("hello"))),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_declaration_06(self):
        input = r"""
        class main {
            static final float a=1.1,b=2e-1,c=1.3E+1;
            static boolean d,e;
            final string f="hello";
            final static int h=3;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(Static(), ConstDecl(
                    Id("a"), FloatType(), FloatLiteral(1.1))),
                AttributeDecl(Static(), ConstDecl(
                    Id("b"), FloatType(), FloatLiteral(0.2))),
                AttributeDecl(Static(), ConstDecl(
                    Id("c"), FloatType(), FloatLiteral(13.0))),
                AttributeDecl(Static(), VarDecl(Id("d"), BoolType())),
                AttributeDecl(Static(), VarDecl(Id("e"), BoolType())),
                AttributeDecl(Instance(), ConstDecl(
                    Id("f"), StringType(), StringLiteral("hello"))),
                AttributeDecl(Static(), ConstDecl(
                    Id("h"), IntType(), IntLiteral(3)))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_declaration_07(self):
        input = r"""
        class main {
            int[5] a;
        }
        """
        expect = str(Program(
            [
                ClassDecl(
                    classname=Id("main"),
                    memlist=[AttributeDecl(Instance(), VarDecl(
                        Id("a"), ArrayType(5, IntType())))],
                    parentname=None
                )
            ]
        ))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_declaration_08(self):
        input = r"""
        class main {
            static boolean[5] a;
            float[50] b;
        }
        """
        expect = str(Program(
            [
                ClassDecl(
                    classname=Id("main"),
                    memlist=[
                        AttributeDecl(Static(), VarDecl(
                            Id("a"), ArrayType(5, BoolType()))),
                        AttributeDecl(Instance(), VarDecl(
                            Id("b"), ArrayType(50, FloatType())))
                    ],
                    parentname=None
                )
            ]
        ))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_declaration_08(self):
        input = r"""
        class main {
            final static boolean[3] a = {true,false,true};
            int[2] b = {1,2};
            final string[1] c = {"hello"}, d = {"world"};
        }
        """
        expect = str(Program(
            [
                ClassDecl(
                    classname=Id("main"),
                    memlist=[
                        AttributeDecl(
                            Static(),
                            ConstDecl(
                                constant=Id("a"),
                                constType=ArrayType(
                                    size=3,
                                    eleType=BoolType()
                                ),
                                value=ArrayLiteral([
                                    BooleanLiteral(True),
                                    BooleanLiteral(False),
                                    BooleanLiteral(True)
                                ])
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                variable=Id("b"),
                                varType=ArrayType(2, IntType()),
                                varInit=ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                constant=Id("c"),
                                constType=ArrayType(1, StringType()),
                                value=ArrayLiteral([StringLiteral("hello")])
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                constant=Id("d"),
                                constType=ArrayType(1, StringType()),
                                value=ArrayLiteral([StringLiteral("world")])
                            )
                        )
                    ],
                    parentname=None
                )
            ]
        ))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_declaration_09(self):
        input = r"""
        class main {
            final static float[3] a = {1e+1,10.0e-1,2.2E+1};
            int[5] b = {1,2,3,4,5};
        }
        """
        expect = str(Program(
            [
                ClassDecl(
                    classname=Id("main"),
                    memlist=[
                        AttributeDecl(
                            Static(),
                            ConstDecl(
                                constant=Id("a"),
                                constType=ArrayType(
                                    size=3,
                                    eleType=FloatType()
                                ),
                                value=ArrayLiteral([
                                    FloatLiteral(10.0),
                                    FloatLiteral(1.0),
                                    FloatLiteral(22.0)
                                ])
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                variable=Id("b"),
                                varType=ArrayType(5, IntType()),
                                varInit=ArrayLiteral([
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    IntLiteral(3),
                                    IntLiteral(4),
                                    IntLiteral(5)
                                ])
                            )
                        )
                    ],
                    parentname=None
                )
            ]
        ))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_declaration_10(self):
        input = r"""
        class main {
            float a;
            boolean foo() {}
            string d;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(Instance(), VarDecl(Id("a"), FloatType())),
                MethodDecl(
                    kind=Instance(),
                    name=Id("foo"),
                    param=[],
                    body=Block([], []),
                    returnType=BoolType()
                ),
                AttributeDecl(Instance(), VarDecl(Id("d"), StringType())),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_declaration_11(self):
        input = r"""
        class main {
            static boolean[5] foo() {}
            string d;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                MethodDecl(
                    kind=Static(),
                    name=Id("foo"),
                    param=[],
                    body=Block([], []),
                    returnType=ArrayType(5, BoolType())
                ),
                AttributeDecl(Instance(), VarDecl(Id("d"), StringType())),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_declaration_12(self):
        input = r"""
        class main {
            float[5] foo() {}
            static boolean[5] foo(int a,b; string[2] c,d) {}
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                MethodDecl(
                    kind=Instance(),
                    name=Id("foo"),
                    param=[],
                    body=Block([], []),
                    returnType=ArrayType(5, FloatType())
                ),
                MethodDecl(
                    kind=Static(),
                    name=Id("foo"),
                    param=[
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                        VarDecl(Id("c"), ArrayType(2, StringType())),
                        VarDecl(Id("d"), ArrayType(2, StringType()))
                    ],
                    body=Block([], []),
                    returnType=ArrayType(5, BoolType())
                ),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_declaration_13(self):
        input = r"""
        class Shape extends Object {}
        class main {
            void foo(Shape s; int[100] t) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Shape"),
                memlist=[],
                parentname=Id("Object")
            ),
            ClassDecl(Id("main"),
                      [
                MethodDecl(
                    kind=Instance(),
                    name=Id("foo"),
                    param=[
                        VarDecl(Id("s"), ClassType(Id("Shape"))),
                        VarDecl(Id("t"), ArrayType(100, IntType()))
                    ],
                    body=Block([], []),
                    returnType=VoidType()
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_declaration_14(self):
        input = r"""
        class Object {}
        class Shape extends Object {}
        class main {
            boolean a = true;
            void foo(Shape s; int[100] t) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname=Id("Object"),
                memlist=[]
            ),
            ClassDecl(
                classname=Id("Shape"),
                memlist=[],
                parentname=Id("Object")
            ),
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(Id("a"), BoolType(), BooleanLiteral(True))
                ),
                MethodDecl(
                    kind=Instance(),
                    name=Id("foo"),
                    param=[
                        VarDecl(Id("s"), ClassType(Id("Shape"))),
                        VarDecl(Id("t"), ArrayType(100, IntType()))
                    ],
                    body=Block([], []),
                    returnType=VoidType()
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_declaration_15(self):
        input = r"""
        class main {
            void foo() {
                {}
                {{}}
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block([], [
                            Block([], []),
                            Block([], [Block([], [])]),
                        ]),
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_declaration_16(self):
        input = r"""
        class main {
            void foo() {
                {
                    {}
                    {{}}
                }
            }
            static int yoo(boolean s) {
                {{{{{}}}}}
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block([], [
                            Block([], [
                                Block([], []),
                                Block([], [Block([], [])])
                            ])
                        ]),
                    ),
                    MethodDecl(
                        kind=Static(),
                        name=Id("yoo"),
                        param=[VarDecl(Id("s"), BoolType())],
                        returnType=IntType(),
                        body=Block([], [
                            Block([], [
                                Block([], [
                                    Block([], [
                                        Block([], [
                                            Block([], []),
                                        ]),
                                    ]),
                                ]),
                            ])
                        ]),
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_declaration_17(self):
        input = r"""
        class main {
            void foo() {
                int a = 0;
                {}
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block([VarDecl(Id("a"), IntType(), IntLiteral(0))], [
                                   Block([], [])]),
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_declaration_18(self):
        input = r"""
        class main {
            void foo() {
                int a = 0, b;
                final Shape s = new Shape(a);
                Rect r;
                final boolean[2] arr = {true,false};
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [
                                VarDecl(Id("a"), IntType(), IntLiteral(0)),
                                VarDecl(Id("b"), IntType()),
                                ConstDecl(
                                    Id("s"),
                                    ClassType(Id("Shape")),
                                    NewExpr(Id("Shape"), [Id("a")])
                                ),
                                VarDecl(
                                    Id("r"),
                                    ClassType(Id("Rect"))
                                ),
                                ConstDecl(
                                    Id("arr"),
                                    ArrayType(2, BoolType()),
                                    ArrayLiteral(
                                        [BooleanLiteral(True), BooleanLiteral(False)])
                                ),
                            ],
                            []
                        ),
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_declaration_19(self):
        input = r"""
        class main {
            void foo() {
                int a;
                {
                    string b;
                    a := 0;
                }
                b := "hello";
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType())],
                            [
                                Block(
                                    [VarDecl(Id("b"), StringType())],
                                    [Assign(Id("a"), IntLiteral(0))]
                                ),
                                Assign(Id("b"), StringLiteral("hello"))
                            ]
                        ),
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_declaration_20(self):
        input = r"""
        class main {
            void foo() {
                int a = 0, b;
                final Shape s = new Shape(a);
                {
                    Rect r1, r2 = new Rect(1,2);
                    {
                        final boolean[2] arr = {true,false};
                    }
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [
                                VarDecl(Id("a"), IntType(), IntLiteral(0)),
                                VarDecl(Id("b"), IntType()),
                                ConstDecl(
                                    Id("s"),
                                    ClassType(Id("Shape")),
                                    NewExpr(Id("Shape"), [Id("a")])
                                )
                            ],
                            [
                                Block([
                                    VarDecl(
                                        Id("r1"),
                                        ClassType(Id("Rect"))
                                    ),
                                    VarDecl(
                                        Id("r2"),
                                        ClassType(Id("Rect")),
                                        NewExpr(
                                            Id("Rect"),
                                            [IntLiteral(1), IntLiteral(2)]
                                        )
                                    )
                                ], [
                                    Block([
                                        ConstDecl(
                                            Id("arr"),
                                            ArrayType(2, BoolType()),
                                            ArrayLiteral(
                                                [BooleanLiteral(True), BooleanLiteral(False)])
                                        )
                                    ], [])
                                ])
                            ]
                        ),
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 330))

    # ---------------------------------------------------------------------------

    def test_expression_01(self):
        input = r"""
        class main {
            boolean a = true && false;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp("&&", BooleanLiteral(
                            True), BooleanLiteral(False))
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_expression_02(self):
        input = r"""
        class main {
            int a = 1 + 2;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=IntType(),
                        varInit=BinaryOp("+", IntLiteral(1), IntLiteral(2))
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_expression_03(self):
        input = r"""
        class main {
            int a = 1 + + 2;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=IntType(),
                        varInit=BinaryOp(
                            op="+",
                            left=IntLiteral(1),
                            right=UnaryOp("+", IntLiteral(2))
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_expression_04(self):
        input = r"""
        class main {
            int a = 1 + 2 + 3 + 4;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=IntType(),
                        varInit=BinaryOp(
                            op="+",
                            left=BinaryOp(
                                op="+",
                                left=BinaryOp(
                                    op="+",
                                    left=IntLiteral(1),
                                    right=IntLiteral(2)
                                ),
                                right=IntLiteral(3)
                            ),
                            right=IntLiteral(4)
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_expression_05(self):
        input = r"""
        class main {
            int a = - 1 + + + 2 + (3 - 5);
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=IntType(),
                        varInit=BinaryOp(
                            op="+",
                            left=BinaryOp(
                                op="+",
                                left=UnaryOp("-", IntLiteral(1)),
                                right=UnaryOp("+", UnaryOp("+", IntLiteral(2)))
                            ),
                            right=BinaryOp(
                                op="-",
                                left=IntLiteral(3),
                                right=IntLiteral(5)
                            )
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_expression_06(self):
        input = r"""
        class main {
            boolean a = b && c;
            boolean d = e || f;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="&&",
                            left=Id("b"),
                            right=Id("c")
                        )
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("d"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="||",
                            left=Id("e"),
                            right=Id("f")
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_expression_07(self):
        input = r"""
        class main {
            boolean a = b && (c || d) || e;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="||",
                            left=BinaryOp(
                                op="&&",
                                left=Id("b"),
                                right=BinaryOp(
                                    op="||",
                                    left=Id("c"),
                                    right=Id("d")
                                )
                            ),
                            right=Id("e")
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_expression_08(self):
        input = r"""
        class main {
            boolean a = b == c;
            boolean d = 2 != e;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="==",
                            left=Id("b"),
                            right=Id("c")
                        )
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("d"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="!=",
                            left=IntLiteral(2),
                            right=Id("e")
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_expression_09(self):
        input = r"""
        class main {
            boolean a = b == (c == false);
            boolean d = 2 != true && e;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="==",
                            left=Id("b"),
                            right=BinaryOp(
                                op="==",
                                left=Id("c"),
                                right=BooleanLiteral(False)
                            )
                        )
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("d"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="!=",
                            left=IntLiteral(2),
                            right=BinaryOp(
                                op="&&",
                                left=BooleanLiteral(True),
                                right=Id("e")
                            )
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_expression_10(self):
        input = r"""
        class main {
            boolean a = b < 2 ;
            boolean c = (d >= 1) && (e > f) || (g <= 1)
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="<",
                            left=Id("b"),
                            right=IntLiteral(2)
                        )
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("c"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="||",
                            left=BinaryOp(
                                op="&&",
                                left=BinaryOp(
                                    op=">=",
                                    left=Id("d"),
                                    right=IntLiteral(1)
                                ),
                                right=BinaryOp(
                                    op=">",
                                    left=Id("e"),
                                    right=Id("f")
                                )
                            ),
                            right=BinaryOp(
                                op="<=",
                                left=Id("g"),
                                right=IntLiteral(1)
                            )
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_expression_10(self):
        input = r"""
        class main {
            boolean a = -+-2+-0.1e+1 <= -+1;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=BinaryOp(
                            op="<=",
                            left=BinaryOp(
                                op="+",
                                left=UnaryOp(
                                    "-", UnaryOp("+", UnaryOp("-", IntLiteral(2)))),
                                right=UnaryOp("-", FloatLiteral(1.0))
                            ),
                            right=UnaryOp("-", UnaryOp("+", IntLiteral(1)))
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_expression_11(self):
        input = r"""
        class main {
            float a = 1 * 20E-1;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=FloatType(),
                        varInit=BinaryOp(
                            op="*",
                            left=IntLiteral(1),
                            right=FloatLiteral(2.0)
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_expression_12(self):
        input = r"""
        class main {
            float a = b * c \ d / e % f;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=FloatType(),
                            varInit=BinaryOp(
                                op="%",
                                left=BinaryOp(
                                    op="/",
                                    left=BinaryOp(
                                        op="\\",
                                        left=BinaryOp(
                                            op="*",
                                            left=Id("b"),
                                            right=Id("c")
                                        ),
                                        right=Id("d")
                                    ),
                                    right=Id("e")
                                ),
                                right=Id("f")
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_expression_13(self):
        input = r"""
        class main {
            float a = b * ((c \ d) / e) % f;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=FloatType(),
                            varInit=BinaryOp(
                                op="%",
                                left=BinaryOp(
                                    op="*",
                                    left=Id("b"),
                                    right=BinaryOp(
                                        op="/",
                                        left=BinaryOp(
                                            op="\\",
                                            left=Id("c"),
                                            right=Id("d")
                                        ),
                                        right=Id("e")
                                    )
                                ),
                                right=Id("f")
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_expression_14(self):
        input = r"""
        class main {
            string a = "hello" ^ "world";
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=StringType(),
                        varInit=BinaryOp(
                            op="^",
                            left=StringLiteral("hello"),
                            right=StringLiteral("world")
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_expression_15(self):
        input = r"""
        class main {
            string a = "hello" ^ "world" ^ b ^ c;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=StringType(),
                        varInit=BinaryOp(
                            op="^",
                            left=BinaryOp(
                                op="^",
                                left=BinaryOp(
                                    op="^",
                                    left=StringLiteral("hello"),
                                    right=StringLiteral("world")
                                ),
                                right=Id("b")
                            ),
                            right=Id("c")
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_expression_16(self):
        input = r"""
        class main {
            string a = b ^ (c ^ (d ^ e)) ^ f;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=StringType(),
                        varInit=BinaryOp(
                            op="^",
                            left=BinaryOp(
                                op="^",
                                left=Id("b"),
                                right=BinaryOp(
                                    op="^",
                                    left=Id("c"),
                                    right=BinaryOp(
                                        op="^",
                                        left=Id("d"),
                                        right=Id("e")
                                    )
                                )
                            ),
                            right=Id("f")
                        )
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_expression_17(self):
        input = r"""
        class main {
            boolean a = !!!b;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
                      [
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        variable=Id("a"),
                        varType=BoolType(),
                        varInit=UnaryOp("!", UnaryOp(
                            "!", UnaryOp("!", Id("b"))))
                    )
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_expression_18(self):
        input = r"""
        class main {
            boolean a = !!(!true);
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=BoolType(),
                            varInit=UnaryOp("!", UnaryOp(
                                "!", UnaryOp("!", BooleanLiteral(True))))
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_expression_19(self):
        input = r"""
        class main {
            boolean a = b[0];
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=BoolType(),
                            varInit=ArrayCell(Id("b"), IntLiteral(0))
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_expression_20(self):
        input = r"""
        class main {
            boolean a = b[1+-2];
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=BoolType(),
                            varInit=ArrayCell(
                                Id("b"),
                                BinaryOp(
                                    op="+",
                                    left=IntLiteral(1),
                                    right=UnaryOp("-", IntLiteral(2))
                                ))
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_expression_21(self):
        input = r"""
        class main {
            boolean a = b[c[d * 1 * 2] + 3];
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=BoolType(),
                            varInit=ArrayCell(
                                arr=Id("b"),
                                idx=BinaryOp(
                                    op="+",
                                    left=ArrayCell(
                                        arr=Id("c"),
                                        idx=BinaryOp(
                                            op="*",
                                            left=BinaryOp(
                                                op="*",
                                                left=Id("d"),
                                                right=IntLiteral(1)
                                            ),
                                            right=IntLiteral(2)
                                        )),
                                    right=IntLiteral(3)
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_expression_22(self):
        input = r"""
        class main {
            boolean a = b * c[-+-+1];
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=BoolType(),
                            varInit=BinaryOp(
                                op="*",
                                left=Id("b"),
                                right=ArrayCell(
                                    Id("c"),
                                    UnaryOp(
                                        "-",
                                        UnaryOp(
                                            "+", UnaryOp("-", UnaryOp("+", IntLiteral(1))))
                                    )
                                ),
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_expression_23(self):
        input = r"""
        class main {
            int a = this.b;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=FieldAccess(SelfLiteral(), Id("b"))
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_expression_24(self):
        input = r"""
        class main {
            int a = b.c.d.e;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=FieldAccess(
                                FieldAccess(
                                    FieldAccess(Id("b"), Id("c")),
                                    Id("d")),
                                Id("e"))
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_expression_25(self):
        input = r"""
        class main {
            int a = b.c();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                obj=Id("b"),
                                method=Id("c"),
                                param=[]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_expression_26(self):
        input = r"""
        class main {
            int a = b.c().d.e();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                obj=FieldAccess(
                                    CallExpr(
                                        obj=Id("b"),
                                        method=Id("c"),
                                        param=[]
                                    ),
                                    Id("d")
                                ),
                                method=Id("e"),
                                param=[]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_expression_27(self):
        input = r"""
        class main {
            int a = (b.c().d + e).f();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                obj=BinaryOp(
                                    op="+",
                                    left=FieldAccess(
                                        CallExpr(
                                            obj=Id("b"),
                                            method=Id("c"),
                                            param=[]
                                        ),
                                        Id("d")
                                    ),
                                    right=Id("e")
                                ),
                                method=Id("f"),
                                param=[]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_expression_27(self):
        input = r"""
        class main {
            int a = b.c(d,e+1,f && g).h;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=FieldAccess(
                                CallExpr(
                                    obj=Id("b"),
                                    method=Id("c"),
                                    param=[
                                        Id("d"),
                                        BinaryOp("+", Id("e"), IntLiteral(1)),
                                        BinaryOp("&&", Id("f"), Id("g"))
                                    ]
                                ),
                                Id("h")
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_expression_28(self):
        input = r"""
        class main {
            int a = this.b().c().d();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                obj=CallExpr(
                                    obj=CallExpr(
                                        obj=SelfLiteral(),
                                        method=Id("b"),
                                        param=[]
                                    ),
                                    method=Id("c"),
                                    param=[]
                                ),
                                method=Id("d"),
                                param=[]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_expression_29(self):
        input = r"""
        class main {
            Shape s = new Shape();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("s"),
                            varType=ClassType(Id("Shape")),
                            varInit=NewExpr(
                                classname=Id("Shape"),
                                param=[]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_expression_30(self):
        input = r"""
        class main {
            A a = new A(a,new B(c.d()));
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=ClassType(Id("A")),
                            varInit=NewExpr(
                                classname=Id("A"),
                                param=[
                                    Id("a"),
                                    NewExpr(
                                        classname=Id("B"),
                                        param=[
                                            CallExpr(
                                                obj=Id("c"), method=Id("d"), param=[])
                                        ]
                                    )
                                ]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_expression_31(self):
        input = r"""
        class main {
            int a = new A(b).c.d();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                obj=FieldAccess(
                                    obj=NewExpr(
                                        classname=Id("A"),
                                        param=[Id("b")]
                                    ),
                                    fieldname=Id("c")
                                ),
                                method=Id("d"),
                                param=[]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_expression_32(self):
        input = r"""
        class main {
            int a = new A() && new B();
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=BinaryOp(
                                op="&&",
                                left=NewExpr(
                                    classname=Id("A"),
                                    param=[]
                                ),
                                right=NewExpr(
                                    classname=Id("B"),
                                    param=[]
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_expression_33(self):
        input = r"""
        class main {
            int a = new A().foo()[new B().b];
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=ArrayCell(
                                arr=CallExpr(
                                    obj=NewExpr(
                                        classname=Id("A"),
                                        param=[]
                                    ),
                                    method=Id("foo"),
                                    param=[]
                                ),
                                idx=FieldAccess(
                                    obj=NewExpr(
                                        classname=Id("B"),
                                        param=[]
                                    ),
                                    fieldname=Id("b")
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_expression_34(self):
        input = r"""
        class main {
            int a = !--new A(10.0E-1++new B());
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=UnaryOp(
                                op="!",
                                body=UnaryOp(
                                    op="-",
                                    body=UnaryOp(
                                        op="-",
                                        body=NewExpr(
                                            classname=Id("A"),
                                            param=[
                                                BinaryOp(
                                                    op="+",
                                                    left=FloatLiteral(1.0),
                                                    right=UnaryOp(
                                                        "+",
                                                        NewExpr(
                                                            classname=Id("B"),
                                                            param=[]
                                                        )
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_expression_35(self):
        input = r"""
        class main {
            int a = b==!c<=d+e*f^g;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=BinaryOp(
                                op="<=",
                                left=BinaryOp(
                                    op="==",
                                    left=Id("b"),
                                    right=UnaryOp("!", Id("c"))
                                ),
                                right=BinaryOp(
                                    op="+",
                                    left=Id("d"),
                                    right=BinaryOp(
                                        op="*",
                                        left=Id("e"),
                                        right=BinaryOp(
                                            op="^",
                                            left=Id("f"),
                                            right=Id("g")
                                        )
                                    )
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_expression_36(self):
        input = r"""
        class main {
            int a = b==c>d!=!e[new F().g];
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=BinaryOp(
                                op=">",
                                left=BinaryOp(
                                    op="==",
                                    left=Id("b"),
                                    right=Id("c")
                                ),
                                right=BinaryOp(
                                    op="!=",
                                    left=Id("d"),
                                    right=UnaryOp(
                                        "!",
                                        ArrayCell(
                                            arr=Id("e"),
                                            idx=FieldAccess(
                                                obj=NewExpr(Id("F"), []),
                                                fieldname=Id("g")
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_expression_37(self):
        input = r"""
        class main {
            boolean a = b + new c("hello").d && e.f[g==h.i*2.0] || k;
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=BoolType(),
                            varInit=BinaryOp(
                                op="||",
                                left=BinaryOp(
                                    op="&&",
                                    left=BinaryOp(
                                        "+",
                                        Id("b"),
                                        FieldAccess(
                                            NewExpr(
                                                Id("c"), [StringLiteral("hello")]),
                                            Id("d")
                                        )
                                    ),
                                    right=ArrayCell(
                                        FieldAccess(Id("e"), Id("f")),
                                        BinaryOp(
                                            "==",
                                            Id("g"),
                                            BinaryOp(
                                                "*",
                                                FieldAccess(Id("h"), Id("i")),
                                                FloatLiteral(2.0)
                                            )
                                        )
                                    )
                                ),
                                right=Id("k")
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_expression_38(self):
        input = r"""
        class main {
            int a = (new b().c[0] + new d()).e.f("hello"^"world");
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                FieldAccess(
                                    BinaryOp(
                                        "+",
                                        ArrayCell(
                                            FieldAccess(
                                                NewExpr(Id("b"), []),
                                                Id("c")
                                            ),
                                            IntLiteral(0)
                                        ),
                                        NewExpr(Id("d"), [])
                                    ),
                                    Id("e")
                                ),
                                Id("f"),
                                [BinaryOp("^", StringLiteral("hello"),
                                          StringLiteral("world"))]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_expression_39(self):
        input = r"""
        class main {
            int a = this.b(11 % 22 + -33,new c(true,d && f)[44],g.h(i)[55]^k);
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=CallExpr(
                                SelfLiteral(),
                                Id("b"),
                                [
                                    BinaryOp(
                                        "+",
                                        BinaryOp("%", IntLiteral(
                                            11), IntLiteral(22)),
                                        UnaryOp("-", IntLiteral(33))
                                    ),
                                    ArrayCell(
                                        NewExpr(
                                            Id("c"),
                                            [
                                                BooleanLiteral(True),
                                                BinaryOp(
                                                    "&&", Id("d"), Id("f"))
                                            ]
                                        ),
                                        IntLiteral(44)
                                    ),
                                    BinaryOp(
                                        "^",
                                        ArrayCell(
                                            CallExpr(Id("g"), Id(
                                                "h"), [Id("i")]),
                                            IntLiteral(55)
                                        ),
                                        Id("k")
                                    )
                                ]
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_expression_40(self):
        input = r"""
        class main {
            int a = !new A(+new b()[new c().d] \ 1 + (-new e()).f.g);
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            variable=Id("a"),
                            varType=IntType(),
                            varInit=UnaryOp(
                                "!",
                                NewExpr(
                                    Id("A"),
                                    [BinaryOp(
                                        "+",
                                        BinaryOp(
                                            "\\",
                                            UnaryOp(
                                                "+",
                                                ArrayCell(
                                                    NewExpr(Id("b"), []),
                                                    FieldAccess(
                                                        NewExpr(Id("c"), []),
                                                        Id("d")
                                                    )
                                                )
                                            ),
                                            IntLiteral(1)
                                        ),
                                        FieldAccess(
                                            FieldAccess(
                                                UnaryOp(
                                                    "-",
                                                    NewExpr(Id("e"), [])
                                                ),
                                                Id("f")
                                            ),
                                            Id("g")
                                        )
                                    )]
                                )
                            )
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 370))

    # ------------------------------------------------------------------------

    def test_statement_01(self):
        input = r"""
        class main {
            void foo() {
                int a;
                a := 0;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType())],
                            [Assign(Id("a"), IntLiteral(0))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_statement_02(self):
        input = r"""
        class main {
            void foo() {
                int a=0;
                if a then a:=1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType(), IntLiteral(0))],
                            [If(Id("a"), Assign(Id("a"), IntLiteral(1)))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_statement_03(self):
        input = r"""
        class main {
            void foo() {
                int a=0;
                if a==0 then a:=1; else a:=2;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType(), IntLiteral(0))],
                            [If(
                                expr=BinaryOp("==", Id("a"), IntLiteral(0)),
                                thenStmt=Assign(Id("a"), IntLiteral(1)),
                                elseStmt=Assign(Id("a"), IntLiteral(2)))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_statement_04(self):
        input = r"""
        class main {
            void foo() {
                int a = 0;
                if a==0 then if b then a:=1; else a:=2;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType(), IntLiteral(0))],
                            [If(
                                expr=BinaryOp("==", Id("a"), IntLiteral(0)),
                                thenStmt=If(
                                    expr=Id("b"),
                                    thenStmt=Assign(Id("a"), IntLiteral(1)),
                                    elseStmt=Assign(Id("a"), IntLiteral(2))),
                                elseStmt=None
                            )]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_statement_05(self):
        input = r"""
        class main {
            void foo() {
                int a = 0;
                if a==0 then { if b then a:=1; } else a:=2;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType(), IntLiteral(0))],
                            [If(
                                expr=BinaryOp("==", Id("a"), IntLiteral(0)),
                                thenStmt=Block([], [
                                    If(
                                        expr=Id("b"),
                                        thenStmt=Assign(
                                            Id("a"), IntLiteral(1)),
                                        elseStmt=None
                                    )
                                ]),
                                elseStmt=Assign(Id("a"), IntLiteral(2))
                            )]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_statement_05(self):
        input = r"""
        class main {
            void foo() {
                int a = 0;
                if a==0 then { final boolean b = true; if b then a:=1; } else a:=2;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [VarDecl(Id("a"), IntType(), IntLiteral(0))],
                            [If(
                                expr=BinaryOp("==", Id("a"), IntLiteral(0)),
                                thenStmt=Block(
                                    [
                                        ConstDecl(Id("b"), BoolType(),
                                                  BooleanLiteral(True)),
                                    ],
                                    [
                                        If(
                                            expr=Id("b"),
                                            thenStmt=Assign(
                                                Id("a"), IntLiteral(1)),
                                            elseStmt=None
                                        )
                                    ]),
                                elseStmt=Assign(Id("a"), IntLiteral(2))
                            )]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_statement_06(self):
        input = r"""
        class main {
            int foo() {
                return 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Return(IntLiteral(1))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_statement_07(self):
        input = r"""
        class main {
            int foo() {
                return 1+2/2-3+4*5;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Return(BinaryOp(
                                op="+",
                                left=BinaryOp(
                                    op="-",
                                    left=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=BinaryOp(
                                            op="/",
                                            left=IntLiteral(2),
                                            right=IntLiteral(2)
                                        )
                                    ),
                                    right=IntLiteral(3)
                                ),
                                right=BinaryOp(
                                    "*", IntLiteral(4), IntLiteral(5))
                            ))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_statement_08(self):
        input = r"""
        class main {
            int foo() {
                return 1;
                a := 0;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                Return(IntLiteral(1)),
                                Assign(Id("a"), IntLiteral(0))
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_statement_09(self):
        input = r"""
        class main {
            int foo() {
                break;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                Break()
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_statement_10(self):
        input = r"""
        class main {
            int foo() {
                continue;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                Continue()
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_statement_11(self):
        input = r"""
        class main {
            int foo() {
                for i:=1 to 2 do break;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                For(
                                    Id("i"),
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    True,
                                    Break()
                                )
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_statement_12(self):
        input = r"""
        class main {
            int foo() {
                for i:=1 to 2 do for j:=3 downto 4 do continue;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                For(
                                    Id("i"),
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    True,
                                    For(
                                        Id("j"),
                                        IntLiteral(3),
                                        IntLiteral(4),
                                        False,
                                        Continue()
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_statement_13(self):
        input = r"""
        class main {
            int foo() {
                for i:=1 to 2 do {
                    final string s = "hello"; 
                    for j:=3 downto 4 do continue;
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                For(
                                    Id("i"),
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    True,
                                    Block(
                                        [
                                            ConstDecl(
                                                Id("s"),
                                                StringType(),
                                                StringLiteral("hello")
                                            )
                                        ],
                                        [
                                            For(
                                                Id("j"),
                                                IntLiteral(3),
                                                IntLiteral(4),
                                                False,
                                                Continue()
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_statement_14(self):
        input = r"""
        class main {
            int foo() {
                for i:=1 to 2 do {
                    int a = 0;
                    {
                        if i==1 then if a==0 then break; else continue; 
                    }
                    if i>a then return i;
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [
                                For(
                                    Id("i"),
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    True,
                                    Block(
                                        [VarDecl(Id("a"), IntType(),
                                                 IntLiteral(0))],
                                        [
                                            Block([], [
                                                If(
                                                    expr=BinaryOp(
                                                        "==", Id("i"), IntLiteral(1)),
                                                    thenStmt=If(
                                                        BinaryOp(
                                                            "==", Id("a"), IntLiteral(0)),
                                                        Break(),
                                                        Continue()
                                                    )
                                                )
                                            ]),
                                            If(
                                                expr=BinaryOp(
                                                    ">", Id("i"), Id("a")),
                                                thenStmt=Return(Id("i"))
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_statement_15(self):
        input = r"""
        class main {
            int foo() {
                this.foo("hello").a := new B("world");
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Assign(
                                FieldAccess(
                                    CallExpr(SelfLiteral(), Id("foo"),
                                             [StringLiteral("hello")]),
                                    Id("a")
                                ),
                                NewExpr(Id("B"), [StringLiteral("world")])
                            )]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_statement_16(self):
        input = r"""
        class main {
            int foo(string s) {
                this.a[this.foo("hello")] := new B("world");
                return 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[VarDecl(Id("s"), StringType())],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Assign(
                                ArrayCell(
                                    FieldAccess(
                                        SelfLiteral(),
                                        Id("a")
                                    ),
                                    CallExpr(SelfLiteral(), Id("foo"),
                                             [StringLiteral("hello")])
                                ),
                                NewExpr(Id("B"), [StringLiteral("world")])
                            ), Return(IntLiteral(1))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_statement_17(self):
        input = r"""
        class main {
            int foo(string s) {
                this.yoo(a).b[this.foo("hello")] := new C("world");
                return 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[VarDecl(Id("s"), StringType())],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Assign(
                                ArrayCell(
                                    FieldAccess(
                                        CallExpr(SelfLiteral(), Id(
                                            "yoo"), [Id("a")]),
                                        Id("b")
                                    ),
                                    CallExpr(SelfLiteral(), Id("foo"),
                                             [StringLiteral("hello")])
                                ),
                                NewExpr(Id("C"), [StringLiteral("world")])
                            ), Return(IntLiteral(1))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_statement_18(self):
        input = r"""
        class main {
            int foo(string s) {
                this.yoo(a)[this.foo("hello")] := new B("world");
                return 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[VarDecl(Id("s"), StringType())],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Assign(
                                ArrayCell(
                                    CallExpr(SelfLiteral(), Id(
                                        "yoo"), [Id("a")]),
                                    CallExpr(
                                        SelfLiteral(),
                                        Id("foo"),
                                        [StringLiteral("hello")]
                                    )
                                ),
                                NewExpr(Id("B"), [StringLiteral("world")])
                            ), Return(IntLiteral(1))]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_statement_19(self):
        input = r"""
        class main {
            int foo() {
                {
                    (this.foo("hello").x + new A("world")).b := c.d(e)[f];
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=IntType(),
                        body=Block(
                            [],
                            [Block([], [
                                Assign(
                                    FieldAccess(
                                        BinaryOp(
                                            "+",
                                            FieldAccess(
                                                CallExpr(
                                                    SelfLiteral(),
                                                    Id("foo"),
                                                    [StringLiteral("hello")]
                                                ),
                                                Id("x")
                                            ),
                                            NewExpr(
                                                Id("A"), [StringLiteral("world")])
                                        ),
                                        Id("b")
                                    ),
                                    ArrayCell(
                                        CallExpr(Id("c"), Id("d"), [Id("e")]), Id("f"))
                                )
                            ])]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_statement_20(self):
        input = r"""
        class main {
            int[3] foo() {
                {
                    final int[3] a = {1,2,3};
                    return a;
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=ArrayType(3, IntType()),
                        body=Block(
                            [],
                            [Block([
                                ConstDecl(
                                    Id("a"),
                                    ArrayType(3, IntType()),
                                    ArrayLiteral([
                                        IntLiteral(1),
                                        IntLiteral(2),
                                        IntLiteral(3)
                                    ])
                                )
                            ], [
                                Return(Id("a"))
                            ])]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_statement_21(self):
        input = r"""
        class main {
            static int[3] main() {
                {
                    return a;
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("main"),
                [
                    MethodDecl(
                        kind=Static(),
                        name=Id("main"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [],
                            [Block([], [

                                Return(Id("a"))
                            ])]
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_statement_22(self):
        input = r"""
        class Shape {
            A(float[2] a,b;string c) {}
            B(int a) { {{{a:=1;}}} {} }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("Shape"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("<init>"),
                        param=[
                            VarDecl(Id("a"), ArrayType(2, FloatType())),
                            VarDecl(Id("b"), ArrayType(2, FloatType())),
                            VarDecl(Id("c"), StringType())
                        ],
                        returnType=None,
                        body=Block(
                            [], []
                        )
                    ),
                    MethodDecl(
                        kind=Instance(),
                        name=Id("<init>"),
                        param=[VarDecl(Id("a"), IntType())],
                        returnType=None,
                        body=Block([], [
                            Block([], [
                                Block([], [
                                    Block([], [Assign(Id("a"), IntLiteral(1))])
                                ])]
                            ),
                            Block([], [])
                        ])
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_statement_23(self):
        input = r"""
        class Shape {
            void foo() {
                this.a();
                b.c();
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("Shape"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [], [
                                CallStmt(SelfLiteral(), Id("a"), []),
                                CallStmt(Id("b"), Id("c"), [])
                            ]
                        )
                    ),
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_statement_24(self):
        input = r"""
        class Shape {
            void foo() {
                this.foo().a(b.c() + this.d - 2, e[0]);
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("Shape"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("foo"),
                        param=[],
                        returnType=VoidType(),
                        body=Block(
                            [], [
                                CallStmt(CallExpr(
                                    SelfLiteral(), Id("foo"), []
                                ), Id("a"), [
                                    BinaryOp(
                                        "-",
                                        BinaryOp(
                                            "+",
                                            CallExpr(Id("b"), Id("c"), []),
                                            FieldAccess(SelfLiteral(), Id("d"))
                                        ),
                                        IntLiteral(2)
                                    ),
                                    ArrayCell(Id("e"),IntLiteral(0))
                                ]),
                            ]
                        )
                    ),
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_statement_25(self):
        input = r"""
        class Shape {
            void foo(Shape s) {}
            int main() {
                final Shape s = Shape.CreateNew();
                this.foo(s);
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("Shape"),
                [
                    MethodDecl(
                        Instance(),
                        Id("foo"),
                        [VarDecl(Id("s"),ClassType(Id("Shape")))],
                        VoidType(),
                        Block(
                            [],
                            []
                        )
                    ),
                    MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        VoidType(),
                        Block(
                            [ConstDecl(
                                Id("s"),
                                ClassType(Id("Shape")), 
                                CallExpr(
                                    Id("Shape"),
                                    Id("CreateNew"),
                                    []
                                )
                            )], 
                            [CallStmt(SelfLiteral(),Id("foo"),[Id("s")])]
                        )
                    ),
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 395))

    # -------------------------------------------------------------

    def test_program_01(self):
        input = r"""
        class Shape {
            static final int numOfShape = 0;
            final int immuAttribute = 0;
            float length,width;
            
            Shape() {

            }

            static int getNumOfShape() {
                return numOfShape;
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("Shape"),
                [   
                    AttributeDecl(
                        Static(),
                        ConstDecl(
                            Id("numOfShape"),
                            IntType(),
                            IntLiteral(0)
                        )
                    ),
                    AttributeDecl(
                        Instance(),
                        ConstDecl(
                            Id("immuAttribute"),
                            IntType(),
                            IntLiteral(0)
                        )
                    ),
                    AttributeDecl(
                        Instance(),
                        VarDecl(Id("length"),FloatType())
                    ),
                    AttributeDecl(
                        Instance(),
                        VarDecl(Id("width"),FloatType())
                    ),
                    MethodDecl(
                        kind=Instance(),
                        name=Id("<init>"),
                        param=[],
                        returnType=None,
                        body=Block([], [])
                    ),
                    MethodDecl(
                        kind=Static(),
                        name=Id("getNumOfShape"),
                        param=[],
                        returnType=IntType(),
                        body=Block([], [
                            Return(Id("numOfShape"))
                        ])
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_program_02(self):
        input = r"""
        class QuickSort {
            void quickSort(int[6] arr; int low, high) {
                if this.len(arr) == 1 then
                    return arr;
                if low < high then
                    pi := this.partition(arr, low, high);

                this.quickSort(arr, low, pi-1);
                this.quickSort(arr, pi+1, high);
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("QuickSort"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("quickSort"),
                        param=[
                            VarDecl(
                                Id("arr"),
                                ArrayType(6,IntType())
                            ),
                            VarDecl(Id("low"),IntType()),
                            VarDecl(Id("high"),IntType())
                        ],
                        returnType=VoidType(),
                        body=Block(
                            [], [
                                If(
                                    BinaryOp("==",
                                        CallExpr(SelfLiteral(),Id("len"),[Id("arr")]),
                                        IntLiteral(1)
                                    ),
                                    Return(Id("arr"))
                                ),
                                If(
                                    BinaryOp("<",Id("low"),Id("high")),
                                    Assign(
                                        Id("pi"),
                                        CallExpr(
                                            SelfLiteral(),
                                            Id("partition"),
                                            [Id("arr"),Id("low"),Id("high")]
                                        )
                                    )
                                ),
                                CallStmt(SelfLiteral(),Id("quickSort"),[
                                    Id("arr"),
                                    Id("low"),
                                    BinaryOp("-",Id("pi"),IntLiteral(1))
                                ]),
                                CallStmt(SelfLiteral(),Id("quickSort"),[
                                    Id("arr"),
                                    BinaryOp("+",Id("pi"),IntLiteral(1)),
                                    Id("high")
                                ])
                            ]
                        )
                    ),
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_program_03(self):
        input = r"""
        class Example {
            int factorial(int n) {
                if n==0 then return 1; else return n * this.factorial(n - 1);
            }

            void main() {
                int x;
                x:=io.readInt();
                io.writeIntLn(this.factorial(x));
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("Example"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("factorial"),
                        param=[VarDecl(Id("n"), IntType())],
                        returnType=IntType(),
                        body=Block(
                            [], [
                                If(
                                    BinaryOp("==",Id("n"),IntLiteral(0)),
                                    Return(IntLiteral(1)),
                                    Return(BinaryOp("*",
                                        Id("n"),
                                        CallExpr(
                                            SelfLiteral(),
                                            Id("factorial"),
                                            [BinaryOp("-",Id("n"),IntLiteral(1))]
                                        )
                                    ))
                                )
                            ]
                        )
                    ),
                    MethodDecl(
                        kind=Static(),
                        name=Id("main"),
                        param=[],
                        returnType=VoidType(),
                        body=Block([
                            VarDecl(Id("x"),IntType())
                        ], [
                            Assign(Id("x"),CallExpr(Id("io"),Id("readInt"),[])),
                            CallStmt(
                                Id("io"),
                                Id("writeIntLn"),
                                [CallExpr(SelfLiteral(),Id("factorial"),[Id("x")])]
                            )
                        ])
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_program_04(self):
        input = r"""
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
        expect = str(Program([
            ClassDecl(
                Id("Shape"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(Id("length"),FloatType())
                    ),
                    AttributeDecl(
                        Instance(),
                        VarDecl(Id("width"),FloatType())
                    ),
                    MethodDecl(
                        kind=Instance(),
                        name=Id("getArea"),
                        param=[],
                        returnType=FloatType(),
                        body=Block(
                            [],[]
                        )
                    ),
                    MethodDecl(
                        kind=Instance(),
                        name=Id("<init>"),
                        param=[
                            VarDecl(Id("length"),FloatType()),
                            VarDecl(Id("width"),FloatType())
                        ],
                        returnType=None,
                        body=Block(
                            [],[
                                Assign(
                                    FieldAccess(SelfLiteral(),Id("length")),
                                    Id("length")
                                ),
                                Assign(
                                    FieldAccess(SelfLiteral(),Id("width")),
                                    Id("width")
                                )
                            ]
                        )
                    ),
                ]
            ),
            ClassDecl(
                classname=Id("Rectangle"),
                parentname=Id("Shape"),
                memlist=[
                    MethodDecl(
                        kind=Instance(),
                        name=Id("getArea"),
                        param=[],
                        returnType=FloatType(),
                        body=Block(
                            [],[
                                Return(BinaryOp(
                                    "*",
                                    FieldAccess(SelfLiteral(),Id("length")),
                                    FieldAccess(SelfLiteral(),Id("width"))
                                ))
                            ]
                        )
                    )
                ]
            ),
            ClassDecl(
                classname=Id("Triangle"),
                parentname=Id("Shape"),
                memlist=[
                    MethodDecl(
                        kind=Instance(),
                        name=Id("getArea"),
                        param=[],
                        returnType=FloatType(),
                        body=Block(
                            [],[
                                Return(BinaryOp(
                                    "/",
                                    BinaryOp(
                                        "*",
                                        FieldAccess(SelfLiteral(),Id("length")),
                                        FieldAccess(SelfLiteral(),Id("width"))
                                    ),
                                    IntLiteral(2)
                                ))
                            ]
                        )
                    )
                ]
            ),
            ClassDecl(
                classname=Id("Example2"),
                parentname=None,
                memlist=[
                    MethodDecl(
                        kind=Static(),
                        name=Id("main"),
                        param=[],
                        returnType=VoidType(),
                        body=Block([
                            VarDecl(Id("s"),ClassType(Id("Shape")))
                        ], [
                            Assign(Id("s"),NewExpr(Id("Rectangle"),[IntLiteral(3),IntLiteral(4)])),
                            CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])]),
                            Assign(Id("s"),NewExpr(Id("Triangle"),[IntLiteral(3),IntLiteral(4)])),
                            CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])])
                        ])
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_program_05(self):
        input = r"""
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
        }
        """
        expect = str(Program([
            ClassDecl(
                Id("QuickSort"),
                [
                    MethodDecl(
                        kind=Instance(),
                        name=Id("partition"),
                        param=[
                            VarDecl(Id("arr"),ArrayType(6,IntType())),
                            VarDecl(Id("low"),IntType()),
                            VarDecl(Id("high"),IntType())
                        ],
                        returnType=IntType(),
                        body=Block(
                            [
                                VarDecl(
                                    Id("i"),
                                    IntType(),
                                    BinaryOp("-",Id("low"),IntLiteral(1))
                                ),
                                VarDecl(
                                    Id("pivot"),
                                    IntType(), 
                                    ArrayCell(Id("arr"), Id("high"))
                                )
                            ], [
                                For(Id("j"),Id("low"),Id("high"),True,
                                    If(
                                        BinaryOp(
                                            "<=",
                                            ArrayCell(Id("arr"),Id("j")),
                                            Id("pivot")
                                        ),
                                        Block([],[
                                            Assign(
                                                Id("i"),
                                                BinaryOp(
                                                    "+",
                                                    Id("i"),
                                                    IntLiteral(1)
                                                )
                                            ),
                                            Assign(
                                                ArrayCell(Id("arr"),Id("i")),
                                                ArrayCell(Id("arr"),Id("j"))
                                            ),
                                            Assign(
                                                ArrayCell(Id("arr"),Id("j")),
                                                ArrayCell(Id("arr"),Id("i"))
                                            )
                                        ])
                                    )
                                ),
                                Assign(
                                    ArrayCell(
                                        Id("arr"),
                                        BinaryOp(
                                            "+",
                                            Id("i"),
                                            IntLiteral(1)
                                        )
                                    ),
                                    ArrayCell(Id("arr"),Id("high"))
                                ),
                                Assign(
                                    ArrayCell(Id("arr"), Id("high")),
                                    ArrayCell(
                                        Id("arr"),
                                        BinaryOp(
                                            "+",
                                            Id("i"),
                                            IntLiteral(1)
                                        )
                                    )
                                ),
                                Return(BinaryOp("+",Id("i"),IntLiteral(1)))
                            ]                       
                        )
                    ),
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 300))