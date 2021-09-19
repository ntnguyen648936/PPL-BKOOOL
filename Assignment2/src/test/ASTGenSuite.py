import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program_01(self):
        input = r"""
        class main {}
        """
        expect = str(Program([ClassDecl(Id("main"), [])]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_simple_program_02(self):
        input = r"""
        class main extends parent { }
        """
        expect = str(Program([ClassDecl(Id("main"), [],Id("parent"))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_program_03(self):
        input = r"""
        class main extends parent { 
            int foo() { }
        }
        """
        expect = str(Program([
            ClassDecl(
                classname  = Id("main"),
                parentname = Id("parent"),
                memlist    = [MethodDecl(
                    kind = Instance(),
                    name = Id("foo"),
                    param = [],
                    body = Block([],[]),
                    returnType = IntType()
                    )],
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_simple_program_04(self):
        input = r"""
        class Abc {}
        class main extends parent { }
        """
        expect = str(Program([
            ClassDecl(Id("Abc"),[]),
            ClassDecl(Id("main"),[],Id("parent"))
        ]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_simple_program_05(self):
        input = r"""
        class parent {}
        class child extends parent { }
        class main extends child {}
        """
        expect = str(Program([
            ClassDecl(Id("parent"),[]),
            ClassDecl(Id("child"),[],Id("parent")),
            ClassDecl(Id("main"),[],Id("child"))
        ]))        
        self.assertTrue(TestAST.test(input,expect,305))

    def test_simple_program_06(self):
        input = r"""
        class main extends parent { 
            main() {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname  = Id("main"),
                parentname = Id("parent"),
                memlist    = [MethodDecl(
                    kind = Instance(),
                    name = Id("main"),
                    param = [],
                    body = Block([],[]),
                    returnType = None
                    )],
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_simple_program_07(self):
        input = r"""
        class Abc {
            Abc() {}
        }
        class main extends parent { 
            main() {
            }
        }
        """
        expect = str(Program([
            ClassDecl(
                classname  = Id("Abc"),
                memlist    = [MethodDecl(
                    kind = Instance(),
                    name = Id("Abc"),
                    param = [],
                    body = Block([],[]),
                    returnType = None
                    )],
            ),
            ClassDecl(
                classname  = Id("main"),
                parentname = Id("parent"),
                memlist    = [MethodDecl(
                    kind = Instance(),
                    name = Id("main"),
                    param = [],
                    body = Block([],[]),
                    returnType = None
                    )],
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_simple_program_08(self):
        input = r"""
        class main extends parent { 
            main(int a, b) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname = Id("main"),
                parentname = Id("parent"),
                memlist = [MethodDecl(
                    kind = Instance(),
                    name = Id("main"),
                    param = [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                    ],
                    body = Block([],[]),
                    returnType = None
                )])
        ]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_simple_program_09(self):
        input = r"""
        class main extends parent { 
            main(int a; boolean c) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname = Id("main"),
                parentname = Id("parent"),
                memlist = [MethodDecl(
                    kind = Instance(),
                    name = Id("main"),
                    param = [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("c"),BoolType())
                    ],
                    body = Block([],[]),
                    returnType = None
                )])
        ]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_simple_program_10(self):
        input = r"""
        class main extends parent { 
            main(int a, b; float c,d) {}
        }
        """
        expect = str(Program([
            ClassDecl(
                classname = Id("main"),
                parentname = Id("parent"),
                memlist = [MethodDecl(
                    kind = Instance(),
                    name = Id("main"),
                    param = [
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                        VarDecl(Id("c"),FloatType()),
                        VarDecl(Id("d"),FloatType())
                    ],
                    body = Block([],[]),
                    returnType = None
                )])
        ]))
        self.assertTrue(TestAST.test(input,expect,310))


    # -------------------------------------------------------------------------


    def test_declaration_01(self):
        input = r"""
        class main {
            int a;
        }
        """
        expect = str(Program(
            [ClassDecl(Id("main"), [AttributeDecl(Instance(), VarDecl(Id("a"), IntType()))])]
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
                AttributeDecl(Instance(), VarDecl(Id("b"), IntType()))
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
            final string d;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
            [
                AttributeDecl(Instance(), VarDecl(Id("a"), FloatType())),
                AttributeDecl(Instance(), VarDecl(Id("b"), FloatType())),
                AttributeDecl(Static(), VarDecl(Id("c"), BoolType())),
                AttributeDecl(Instance(), VarDecl(Id("d"), StringType())),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_declaration_05(self):
        input = r"""
        class main {
            static final float a,b;
            static boolean c,d;
            final string e;
            final static int f;
        }
        """
        expect = str(Program([
            ClassDecl(Id("main"),
            [
                AttributeDecl(Static(), VarDecl(Id("a"), FloatType())),
                AttributeDecl(Static(), VarDecl(Id("b"), FloatType())),
                AttributeDecl(Static(), VarDecl(Id("c"), BoolType())),
                AttributeDecl(Static(), VarDecl(Id("d"), BoolType())),
                AttributeDecl(Instance(), VarDecl(Id("e"), StringType())),
                AttributeDecl(Static(), VarDecl(Id("f"), IntType())),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 315))

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
                    kind = Instance(),
                    name = Id("foo"),
                    param = [],
                    body = Block([],[]),
                    returnType = BoolType()
                ),
                AttributeDecl(Instance(), VarDecl(Id("d"), StringType())),
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 320))



