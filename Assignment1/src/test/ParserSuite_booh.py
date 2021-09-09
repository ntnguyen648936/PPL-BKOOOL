import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):

        input = """class Example1 {
                        void main(){}
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):

        input = """class Example1 {
                        void main(){
                            int x;
                        }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """class Example1 {
                        void main(){
                            int x;
                        }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_204(self):
        input = """ class Shape {
                        static final int numOfShape = 0;
                        
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        """  test attribute """
        input = """ class Shape {
                        static final int numOfShape = 0;
                        final int immuAttribute = 0;
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        """  test attribute """
        input = """ class Shape {
                        final static int numOfShape = 0;
                        final int immuAttribute = 0;
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        """  test attribute """
        input = """ class Shape {
                        float length,width;
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208 (self):
        input = """ class Shape {
                        float length,width;
                        static int getNumOfShape() {
                            }
                             }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209 (self):
        input = """ class Shape {
                        float length,width;
                        static int getNumOfShape() {
                            return numOfShape; }
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210 (self):
        """test empty classs"""
        input = """ class Shape {
                       
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        """test attribute"""
        input = """ class Shape {
                    final int My1stCons = 1 + 5;
                    static int x,y = 0 ;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        """test attribute"""
        input = """ class Shape {
                    final int My1stCons = 1 + 5, My2ndCons = 2;
                    static int x,y = 0 ;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        """test constructor"""
        input = """ class Shape {
                        Shape(){}
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        """test parameter"""
        input = """ class Shape {
                        static int getNumOfShape(int a; float b) {
                            return numOfShape;
                        }
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        """no class declared"""
        input = """ 
static int getNumOfShape(int a; float b) {}
                    """
        expect = "Error on line 2 col 0: static"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        """no class declared"""
        input = """
Class Shape {
static int getNumOfShape(int a; float b) {}
                       } """
        expect = "Error on line 2 col 0: Class"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
            """without type"""
            input = """
class Shape {
static getNumOfShape(int a; float b) {}
                           } """
            expect = "Error on line 3 col 7: getNumOfShape"
            self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = """
class Shape {
static int x,y = 5.0;
                               } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):

        input = """ class Shape {
                        Shape(){}
                        boolean z = true;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):

        input = """ class Shape {
                        boolean z,y = true;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):

        input = """ class Shape {
                        string z,y = true;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        """test string list"""
        input = """ class Shape {
                        string z ="hello" ,y = "hji";
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):

        input = """ class Shape {
                        #commentline;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):

        input = """ class Shape {
                        /* #comment block \n */
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):

        input = """ class Shape {
                        int[5] a ;
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):

        input = """ class Shape {
                        int[5] a ;
                        static void assign()
                         { b:= 10;}
                        }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):

        input = """ class Shape {
                        int[5] a ;
                        static void assign()
                         { b:= 10;}
                        }
                    class a{}
                    class b{}
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """ class Shape {
                           int[5] a ;
                           static void assign()
                            { b:= 10;}
                           }
                       class a{}
                       class b{}
                       """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """ class Shape {
                           int[5] a ;
                           static void assign()
                            { b:= 10;}
                           }
                       class a{}
                       class b{
                           boolean[4] b;     
                       }
                       """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    # def test_230(self):
    #     input = """ class Shape {
    #
    #                 boolean[4] b:= {false, false, true, true}
    #                   }
    #                    """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 230))
    #

    def test_231(self):
        input = """ 
                   class Shape {
                        float length,width;
                        Shape(float length,width){}    
                      }
                       """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = """ 
                          class Example1 {
int factorial(int n){
if n == 0 then return 1; else return n * this.factorial(n - 1);}
}
                               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = """ 
                class Example1 {
                    int factorial(int n){
                        a[3+x.foo(2)] := a[b[2]] +3;
                    }
        }
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = """ 
                class Example1 {
                    int factorial(int n){
                        x.b[2] := x.m()[3];
                    }
        }
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    # def test_235(self):
    #     input = """
    #             class Example1 {
    #                 int factorial(int n){
    #                     x.b[true] := x.m()[3];
    #                 }
    #     }
    #                                """
    #     expect = "Error "
    #     self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """ 
                class Example1 {
                    int factorial(int n){
                        x.b[1] := x.m()[3];
                    }
                }
                class Example2 {
                   void main(){
                        s := new Rectangle(3,4);
                        }
                }    
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """ 
                class Example2 {
                   void main(){
                        float r,s;
                        int[5] a,b;
                        #list of statements
                     
                        }
                }    
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """ 
                class Example2 {
                   void main(){
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
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """ 
                class Example2 {
                   void main(){
                        float r,s;
                        int[5] a,b;
                        #list of statements
                        r:=2.0;
                        s:=r*r*this.myPI;
                        a[0]:= s;
                        }
                }
                class E {
                    int x =0, y = 10;
                }    
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """ 
                class Example2 {
                   void main(){
                       this.aPI := 3.14;
                        value := x.foo(5);
                        l[3] := value * 2;
                        }
                }
                class E {
                    E(){}
                }    
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """ 
               class Example1 {
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
                }
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """ 
               class Example2 {
                    void main(){
                   
                    s := new Rectangle(3,4);
                    io.writeFloatLn(s.getArea());
                    s := new Triangle(3,4);
                    io.writeFloatLn(s.getArea());
                    }
            }
                                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """ 
                       class Example2 {
                            int[true]5;
                    }
                                           """
        expect = "Error on line 3 col 32: true"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """ 
                       class Example {
                            void main(){
                    }
                                           """
        expect = "Error on line 5 col 43: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """ 
                       class Example {
                            void main(){
                                if flag then
                                    io.writeStrLn("Hello");
                                else
                                    io.writeStrLn();
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """ 
                       class Example {
                            void main(){
                                if flag then
                                    io.writeStrLn("Hello");
                                else
                                    io.writeStrLn(23456789);
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """ 
                       class Example {
                            void main(){
                                if a&&c&&b then
                                    io.writeStrLn("Hello");
                            
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """ 
                       class Example {
                            void main(){
                                if a&&c&&b then
                                    if 1 then
                                        io.writeStrLn("Hello");

                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_249(self):
        input = """ 
                       class Example {
                            void main(){
                                if a&&c&&b then
                                    if 1 then
                                        io.writeStrLn("Hello");
                                    else 
                                        return 729;

                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """ 
                       class Example {
                            void main(){
                                if a&&c&&b then
                                    if 1 then
                                        io.writeStrLn("Hello");
                                    else 
                                        return 729;
                                else
                                    break;
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 100 do {
                                    io.writeIntLn(i);
                                    Intarray[i] := i + 1;
                                    }
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 3 do {
                                    if true then
                                        io.writeIntLn(i);
                                        Intarray[i] := i + 1;
                                    }
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 3 do {
                                    if true then
                                        io.writeIntLn(i);
                                    else
                                        Intarray[i] := i + 1;
                                    }
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_253(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 3 do {
                                    if true then
                                        io.writeIntLn(i);
                                    else
                                        Intarray[i] := i + 1;
                                    }
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 3 do {
                                   for j:= 0 to 3 do {
                                        this.a[i] := j;   
                                   }
                                }
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_254(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 3 do {
                                   for j:= 0 to 3 do {
                                        this.a[i] := j;   
                                   }
                                }
                            }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = """ 
                       class Example {
                            void main(){
                                for i := 1 to 3 do {
                                   for j:= 0 to 3 do {
                                        this.a[i] := j;   
                                   }
                                }
                            }
                        class Ex {
                            Ex (int a, b) {
                                
                            }
                        }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = """ 
                    class Example {
                        void main(){
                               for i := 1 to 3 do {
                                  for j:= 0 to 3 do {
                                  if a||b&&c then
                                    continue;
                                   else
                                       this.a[i] := j;   
                                  }
                                }
                            }
                    class Ex {
                            Ex (int a, b) {

                            }
                            
                        }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = """ 
                    class Example {
                        void main(){
                               for i := 1 to 3 do {
                                  for j:= 0 to 3 do {
                                  if a||b&&c then
                                    continue;
                                   else
                                       this.a[i] := j;   
                                  }
                                }
                            }
                    class Ex {
                            Ex (int a, b) {
                                this.a := 10;
                                this.b:= 1;
                            }

                        }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = """ 
                    class Example {
                        int sum(int x, y) {
                            if x==y then return x+y;
                            else
                                return x-y;
                        }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = """ 
                    class Example {
                        int sum(int x, y) {
                            if x==y then return x+y;
                            else
                                return x-y;
                        }
                        Example(boolean a; int x) {
                            if a==true then x:=1;
                            else x:=-9;
                        }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_259(self):
        input = """ 
                    class Example {
                        int[5] array;
                        boolean  check(int x, y) {
                            for i:=0 to 10 do {
                                    if i<=10 then continue;
                                    if x==y  then
                                        x:=x+y;
                                    else this.array[4]:=true;
                                    
                                }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = """ 
                    class Example {
                        int[5] array = {2.3, 4.2, 102e3};
                        static float test(boolean x; int y; float z) {
                            if x==true then
                                return y;
                            else 
                                return z;
                        }
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = """ 
                    class Example {
                        final int My1stCons = 1 + 5,My2ndCons = 2;
                        static int x,y = 0; 
                        boolean z = true && false;
                        void main(){
                            if x != y then
                            return z || false;
                        }
                        
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = """ 
                    class Example {
                        final int My1stCons = 1 + 5,My2ndCons = 2;
                        static int x,y = 0; 
                        boolean z = true && false;
                        void main(){
                            if x != y && z == true then
                                break;
                            else 
                                for i:= 10 downto 0 do 
                                    return 10.34e-09;
                        }

                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """ 
                    class Example {
                        int[5] a;
                        void main(){
                            if x != y || z == true  && a[0]!=a[x] then
                                break;
                            
                        }

                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """ 
                    class Example {
                        int[5] a;
                        void main(){
                            if flag then
                                a[3+x.foo(2)] := a[b[2]] +3;
                            else
                                if flag == false || true && false then
                                    return  0;                    
                        }

                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """ 
                    class Example {
                        int[5] a;
                        string s1 = "" , s2 = "";
                        void main(){
                            if flag then
                               s:= new String();
                            s:= s1^s2;                
                        }

                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """ 
                    class Example {
                        int[5] a;
                        string s1 = "" , s2 = "";
                        void main(){
                            if flag then
                               s:= new String();
                            s :=  s1 + " Hello";              
                        }

                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """ 
                     class Node {
                        Node(){}
                        }
                    class AVL {
                        string x = "Hello";
                        void main(){
                            obj := new Node();
                            return obj.writeStrLn(x);
                        }
                        
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """ 
                    class Node {
                        Node(){}
                        }
                    class AVL {
                        string x = "Hello";
                        int x = y < x;
                        
                        /*void main(){
                        #ualasao?
                        }*/
                        
                    }
                                           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """ 
                    class Node {
                        Node(){}
                        }
                    class AVL {
                        void main(){
                            if x == 10 then return
                        }
                    }
                                           """
        expect = "Error on line 8 col 24: }"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """ 
                class Exm {
                    int sum() {
                        int x = 10;
                        float t = 10.53e45544,y = 10.0;
                        return x + t -y % 10 / 1000;    
                    }
                }                
                  
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """ 
                class Exm {
                    int sum() {
                        int x = 10;
                        float t = 10.53e45544,y = 10.0;
                        return x + t -y % 10 / 1000;    
                    }
                    
                }   
                class A extends  Exm {
                        void print() {
                            this.writeLnStr("Hi");
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """ 
                class Exm {
                    int sum() {
                        int x = 10;
                        float t = 10.53e45544,y = 10.0;
                        return x + t -y % 10 / 1000;    
                    }

                }  
                class B extends A {
                        static void check(int p; string str) {
                            s:= str^str;
                            if flag then p:=10;
                            for j:= 0 to 10 do {
                                this.writeLnStr(str \n);
                            }
                        }
                    }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """ 
                class Exm {
                    int posting_invoice() {
                        if bill == true then
                            this.postinvoice(ok);
                        else
                            return -1; 
                    }

                }   
                
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_273(self):
        input = """ 
                class Exm {
                    int posting_invoice() {
                        if bill == true then
                            this.postinvoice(ok);
                        else
                            return -1; 
                    }
                }   

               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """ 
                class Exm {
                    void main() {
                        boolean x = true || false || true && true;
                    }
                }   

               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """ 
                class Exm {
                    void main() {
                        boolean x = true || false || true && true;
                    }
                    class Child {
                        string[3] str; 
                        string s = "";
                        void main() {
                        s := str[1] +. str[2];
                    }
                    }
                } 
               """
        expect = "Error on line 10 col 37: ."
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """ 
                    class Child {
                        void main() {
                            s := str[1] || str[2];
                            if s == nil then return 0;
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """ 
                    class Child {
                        int foo () {
                            s := a - b && c; 
                            b[u] := u; 
                            a := k + u[j]; 
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """ 
                    class Child {
                        int foo () {
                            a := (a <= b) < c;
                            a := (a < b) <= c; 
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = """ 
                    class Child {
                        int foo () {
                            return 10.0e9;
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = """ 
                    class Child {
                        int foo () {
                            aBc.import();
                            return -10.0e9;
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = """ 
                    class Child {
                        int foo () {
                            a := a && b && b; 
                        }
                    
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = """ 
                    class Ex {
                        int foo () {
                           a := !b; b := -c;
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """ 
                    class Child {
                        int foo () {
                            a := (a * b \ c % d  + f - h > b || c && m) == (v || a != a);
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """ 
                    class Child {
                        int foo () {
                            break; 
                            continue; 
                        }
                } 
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """
                    class Example2 {
                        void main(){
                        #s:Shape;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                        }
                        }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_287(self):
        input = """
                    class Child {
                        int foo () {
                           t:= x.factor(x,t);
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """
                    class Child {
                        int foo () {
                           l[4] := true;
                           if 1 then return dasdas;
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = """
                    class Child {
                        int foo (boolean a; boolean c) {
                        for i := 1 to  4  do 
                            { this.print(i);} 
                        x := x % y;
                        y := y * z; 
                        z := z && x; 
                        return a + c; 
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = """
                    class Child {
                        void main() {
                            this.import(pprint); 
                            this.import(stringIO); 
                            this.stream := new stringIO(); 
                            this.runner := this.unittest(textTestRunner(stream==stream));
                            this.result := Parent.runner(run(suite));
                            this.print("Tests run", result(testsRun)); 
                            this.print("Errors ", result(errors));
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """
                    class Child {
                        int foo () {
                            
                        }}
                }
               """
        expect = "Error on line 6 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """
                    class Child {
                        int foo () {

                        };
                }
               """
        expect = "Error on line 5 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """
                    class Child {
                        foo() {

                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """
                    class Child {
                        void foo () {
                                for x := 5 downto 2 do
                                    if flag then
                                        io.writeIntLn(x);
                                    else break;

                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
                    class Child {
                        void foo () {
                             a[3 + foo(2)] := a[b[2][3]]] ;
                        }
                }
               """
        expect = "Error on line 4 col 56: ]"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """
                    class Child {
                        void foo () {
                             a[3 + foo(2)] := a[b[2][3] + 3];
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
                    class Child {
                        int foo () {
                            for i:=0 to n/2 do {
                                this.print(i);
                                }
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """
                    class Child {
                        void foo () {
                            if i==n / 2 * length - n < 10 then
                                break;
                            else
                                for j:=x+10/2 to 20%5 +y do {
                                        this.num:=this.num-1;
                                    }
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """
                    class Child {
                        int foo (boolean x) {
                            if x == true then
                                b[x+this.func(m/30)%3 + x] := 1;
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """
                    class Child {
                        void foo () {
                             int mid;
                            if rightIdx >= leftIdx then
                                mid := leftIdx + (rightIdx - leftIdx) \ 2;
                                /* If found target */
                                if arr[mid] == target then
                                    return mid;
                               
                                /* Target is at left branch */
                                if arr[mid] > target then
                                    return this.binarySearch(arr, 1, mid - 1, target);
                                
                            return -1;  
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = """
                    class Child {
                        int sum;
                        int foo () {
                                if sum > 21 then
                                if a == 11 then
                                    sum := 1 + b;
                                else 
                                    sum := 1 + a;
                            
                            return sum;
                        }
                }
               """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))