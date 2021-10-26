import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = Program([ClassDecl(Id("Child"), [
            MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(SelfLiteral(),Id("foo"),[])]))
        ])],True)
        expect = "Undeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,400))