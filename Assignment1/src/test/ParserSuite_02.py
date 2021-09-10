import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """class Rectangle extends Shape {

                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = """class Rectangle extends Shape {
                    static final int numOfShape = 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """class Shape {
                    static final int numOfShape = 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """class Shape {
                    static final int numOfShape = 0;
                    final int immuAttribute = 0;
                    float length,width;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """class Shape {
                    final int My1stCons = 1 + 5;
                    static final int My2ndCons = 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = """class Shape {
                    int my1stVar;
                    int[5] myArrayVar ;
                    static Shape my2ndVar, my3rdVar;
                    static Shape[6] my2ndArray, my3rdArray;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = """class Shape {
                        float getArea(){
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = """class Shape {
                        float getArea(){
                            return this.length*this.width;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = """class Shape {
                        static void getArea(int a, b, c){
                            return this.length*this.width;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = """class Shape {
                        static void getArea(float a, b, c){
                            return this.length*this.width;
                        }
                    }
                    class abc {
                        int my1stVar;
                        int[5] myArrayVar;
                        static Shape my2ndVar, my3rdVar;
                        static Shape[6] my2ndArray, my3rdArray;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        input = """class abc {
                        static void getArea(int a, b, c){
                            return a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        input = """class abc {
                        string getArea(int a, b, c){
                            a[7+x.foo(2)] := a[b[2]] +7+x.foo(2);
                            return abc[1+2];
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    # TODO: CHECK 213
    def test_213(self):
        input = """class abc {
                        void getArea(string a, b, c){
                            return b[[4]];
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        input = """class abc {
                        static void getArea(float length,width){
                            {
                                this.length := length;
                                this.length := length;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        input = """class abc {
                        static void getArea(int length,width){
                                #start of declaration part
                                float r = 3,s;
                                int[5] a,b;
                                /*list of statements*/
                                r := r ;
                                s:=r*r*this.myPI;
                                a[0]:= 2.0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        input = """class abc {
                        void getArea(int length,width){
                            this.aPI := 3.14;
                            value := x.foo(5);
                            l[3] := value * 2;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = """class abc {
                        void getArea(int length,width){
                            if a > 1 then
                                io.writeStr("aa");
                            else
                                io.writeStr("def", arg);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = """class abc {
                        void getArea(float length, width){
                            if a == 1 then
                                io.write("abc");
                                if b < 0 then
                                    b := c + 3;
                                else
                                    b[1] := a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = """class abc {
                        void getArea(float length,width){
                            if a <= b + c then
                                value := x.foo(5);
                                l[3] := value * 2;
                                io.write("abc");
                                if b < 0 then
                                    b := c + 3;
                                else
                                    b[1] := a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        input = """class abc {
                        void getArea(float length,width){
                            if a[3] == 1 then
                                io.write("abc");
                                if b < 0 then
                                    b := c + 3;
                                else
                                    if c >= 1 then
                                        b[1] := a;
                                        io.write("def");
                                    if z != 1 then
                                        continue;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = """class abc {
                        static final int a = 1;
                        final static int b = 2;
                        final int c = 3;
                        static int d = 4;
                        int e = 5;
                        static void getArea(float length,width){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = """class abc {
                        static int getArea(float length,width){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return abc;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = """class abc {
                        void empty(){
                        }
                        int test(){
                        int b = 1;
                        a := 1;
                        x.xxxx(xx);
                        }
                        void getArea(int length,width){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                                break;
                            for i := 1 to 100 do {
                                break;
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = """class abc {
                        void getArea(float length,width){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                                if x == 3 then
                                    break;
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = """class abc {
                        void getArea(float length,width){
                            a = 1;
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                                if (a*3 < 10) then
                                    continue;
                            }
                        }
                    }"""
        expect = "Error on line 3 col 30: ="
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = """class abc {
                        string getArea(float length,width){
                            a := 1;
                            int a = 2;
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return this.a;
                        }
                    }"""
        expect = "Error on line 4 col 28: int"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = """class abc {
                        int getArea(float length,width){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                if a < 1 then
                                    continue;
                                else
                                    break;
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """class abc {
                        abc(){
                            for x := 5 downto 2 do
                                Sha.getString();
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """class abc {
                        int getArea(float length,width){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return a.getNumber(10);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = """class abc {
                        void getArea(float length,width){
                            b.getMax(a[5]);
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }
                    class abc {
                        void getArea(float length,width){
                            b.getMax(a[5]);
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = """class abc {
                        int Mouse(int a,b){
                            b.getMax("abc");
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = """class abc {
                        int Mouse(int a,b){
                            b.getMax("1", a + b / 10);
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = """class abc {
                        int Main(){
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = """class abc {
                        int float(){
                            return 0;
                        }
                    }"""
        expect = "Error on line 2 col 28: float"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = """class abc____123 {
                        int go(int a,b){
                            b.getMax(c.a(c[3 + c[4]]));
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """class abc {
                        int abc(){
                            b.getMax(b, -a);
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """class abc {
                        abc(int a,b){
                            b.getMax(c.getT(e, a));
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """class abc {
                        int Cal(int a,b){
                            b.getMax("e", a*10/b);
                            return this.t;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """class abc {
                        int Cat(string a,b){
                            a := a^b;
                            return a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """class Example2 {
                        void main(){
                            s := new Rectangle(3,4);
                            io.writeFloatLn(s.getArea());
                            s := new Triangle(3,4);
                            io.writeFloatLn(s.getArea());
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """class abc {
                        int Mouse(int a,b){
                            b.getMax(--z, 10);
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """class Shape {
                    float length,width;
                    float getArea() {}
                    Shape(float length,width){
                        this.length := length;
                        this.width := width;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """class abc {
                        int foo(string a,b){
                            b.getMax(a[i], b[j], c[z]);
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n == 0 then return 1; 
                        else return n * this.factorial(n - 1);
                    }
                    void main(){
                        int x;
                        x := io.readInt();
                        io.writeIntLn(this.factorial(x));
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n == 0 then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                    void main(){
                        float x;
                        x := io.read("Input");
                        x := io.readInt();
                        io.writeIntLn(this.factorial(x));
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """class Example1 {
                    int factorial(){
                        if n == 0 then return 1; 
                        else return n * this.factorial(n - 1) \\ 10 + [1 - 4];
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """class Rectangle extends Shape {
                        float getArea(){
                            return this.length*this.width;
                        }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }"""
        expect = "Error on line 3 col 30: s"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """class Shape {
                    float length,width;
                    float getArea() {}
                    Shape(float length,width){
                        this.length := length;
                        this.width := width;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = """class abc {
                        static final string getArea(){
                            for x := 5 + a.getT() downto 2 do
                                io.writeIntLn(x);
                            for i := 1 - b.getN() to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return this.a;
                        }
                    }"""
        expect = "Error on line 2 col 51: ("
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = """class abc {
                        static string getArea(float length,width){
                            for x := 5*ee.g(a,b) downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return this.a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = """class abc {
                        int getArea(float length,width){
                            for x := 5 + b * 2 % 10 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return this.a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = """class abc {
                        float getArea(){
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                            for i := 1 - b to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                                if a != 1 then
                                    return t;
                            }
                            return this.a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 || a / 5 + 4 then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n == 0 || k <= 4 && m < 5 then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "Error on line 3 col 49: <"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 || a < b + 34 then return 1; 
                        else return n * this.factorial(n - 1, "abc");
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 && [a - b == 2] then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 then return 1; 
                        else return n.get("abc") * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = """class Example1 {
                    int factorial(int n){
                        if n * 1.6e-1 == 0 && [!a - !b == 2] then return 1; 
                        else return n * this.factorial(n - 1);
                        break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = """class abc {
                        static void getArea(float length,width){
                            {
                                this.length := length;
                                this.length := ! length;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """class abc { #cmt
                        static void getArea(float length,width){ #cmt
                            { #cmt
                                this.length := length; #cmt
                                this.length := ! length; #cmt
                                a := a + [a + 1]; #cmt
                                return a; #cmt
                            } #cmt
                        } #cmt
                    } #cmt"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """class abc {
                        static void getArea(float length,width){
                            {
                                this.length := length;
                                this.length := ! length;
                                a := a + [a + Mouse.get()];
                                return a;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """class abc {
                        static void getArea(float length,width){
                            {
                                this.length := length;
                                this.length := ! length;
                                a := a + [a + b % 10];
                                return a;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """class abc {
                        void getArea(string a, b, c, d){
                            {
                                this.length := length;
                                this.length := ! length;
                                a := a + [a + b % 10];
                                if a == b then
                                    io.write("ABC");
                                return a;

                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """class abc {
                        void getArea(string a, b, c, d){
                            {
                                this.length := -length;
                                this.length := !length;
                                a := a + [a + b % 10];
                                if a == b then
                                    io.write("ABC");
                                return a;

                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """class abc {
                        void getArea(string a, b, c, d){
                            {
                                this.length := length;
                                this.length := ! length;
                                a := a + [a + b % 10];
                                if a == b then
                                    io.write("ABC");
                                else
                                    io.read();
                                return a*a*b-5;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """class abc {
                        void getArea(string a, b, c, d){
                            {
                                this.length := length;
                                this.length := ! length;
                                a := a + [a + b % 10];
                                if a == b then
                                    io.write("ABC");
                                    for a := 1*b.get("length") to 100 do
                                        tong := tong + 1;
                                return tong;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """class abc {
                        void getArea(string a, b, c, d){
                            {
                                this.length := length;
                                this.length := !length;
                                a := a + [a + b % 10];
                                if a == b then
                                    io.write("ABC");
                                    break;
                                return a;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """class abc {
                        static void getArea(float length,width){
                            if a == 1 then
                                io.write("abc");
                                if b < 0 then
                                    b := c + 3;
                                else
                                    b[1] := a.get();
                                this.valid := a;
                            return temp;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """class abc {
                        static void getArea(float length,width){
                            if a == 1 then
                                io.write("abc");
                                if b < 0 then
                                    b := c + 3;
                                else
                                    b[1] := a;
                                    for x := 5 downto 2 do
                                    io.writeIntLn(x);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """class abc {
                        static void getArea(int length,width){
                            if a == 1 then
                                io.write("abc");
                                if b < 0 then
                                    b := c + 3;
                                else
                                    b[1] := a;
                                    for i := 1 to 100 do {
                                        io.writeIntLn(i);
                                        Intarray[i] := i + 1;
                                    }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """class abc {
                        string getArea(){
                            if a == 1 then
                                io.write("abc");
                                if b < 0 then
                                {	b := c + 3;
                                    this.aPI := 3.14;
                                    value := x.foo(5, "abc");
                                    l[3] := value * 2;
                                }
                                else
                                    b[1] := a;
                            return "MMMMMM";
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """class abc {
                        void getArea(){
                            if a == 1 then
                                io.write(x*y + x.foo(a[1]));
                                if b < 0 then
                                    b := c.get("Dog") + 3 - c.get("Cat");
                                else
                                    b[1] := a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """class Example2 {
                    void main(){
                        s := new Rectangle("et",4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """class Example2 {
                    void main(){
                        s := new Rectangle(3,4, 0);
                        io.writeFloatLn(s.getArea());
                        this.B := new Triangle(3,4, "TAnv");
                        io.writeFloatLn(s.getArea());
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """class Example2 {
                    void main(){
                        s := new Rectangle(r.getVa(),4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = """class Example2 {
                    void main(){
                        s := new Rectangle(3,4,Mouse.get("Anh"));
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = """class Example2 {
                    void main(){
                        s := new Rectangle(b, e, f);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle();
                        io.writeFloatLn(s.getArea());
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = """class Shape {
                        static void getArea(int a, b, c){
                            if a < [b - c] then
                                return a;
                            return this.length*this.width;
                        }
                    }
                    class abc {
                        int[5] myArrayVar;
                        static Shape my2ndVar, my3rdVar;
                        static Shape[6] my2ndArray, my3rdArray;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = """class Shape {
                        static void getArea(int a, b, c){
                            my1stVar := 10000;
                            return this.length*this.width;
                        }
                    }
                    class abc {
                        int my1stVar;
                        int[5] myArrayVar;
                        static Shape my2ndVar, my3rdVar;
                        static Shape[6] my2ndArray, my3rdArray;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """class Shape {
                        static void getArea(int a, b, c){
                            if a==1 then 
                                return 0;
                            return this.getArea(a-1, b-2, c-3);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """class Shape {
                        static void getArea(int a, b, c){
                            if [a == 1] || [b == 10] then
                                return this.getArea(a/10, b/10,c);
                            return this.length*this.width;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """class Shape {
                        static void getArea(int a, b, c){
                            for i := a + b to c * c do{
                                if i == 10 then continue;
                                a := a + 10;
                            }
                            return a;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = """class abc {
                        void getArea(){
                                r := this.length ;
                                s:=r*r*this.myPI;
                                a[0]:= 2.0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """class abc {
                        void getArea(){
                                r := r ;
                                s:=r*r*this.myPI("Ne", a);
                                a[0]:= 2.0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = """class abc {
                        void getArea(){
                                #list of statements
                                r := r ;
                                s:=r*r*this.myPI;
                                a[0]:= 2.0;
                                return this.length;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = """class abc {
                        void getArea(){
                                #list of statements
                                r := r ;
                                s:=r*r*this.myPI;
                                a[0]:= 2.0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """class abc {
                        static void getArea(){
                                r := r ;
                                s:=r*r*this.myPI % 10;
                                a[0]:= 2.0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """class abc {
                        static float getArea(){
                            for x := 5 downto 2 do
                                Sha.getString();
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                                a := 5;
                            }
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """class abc {
                        static void getArea(){
                            for x := 5 downto 2 do
                                Sha.getString();
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                                if i == 10 then
                                    a := 3;
                                    continue;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """class abc {
                        static void getArea(){
                            for x := 5*a.get("bet") downto 2 do
                                Sha.getString();
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """class abc {
                        static void getArea(){
                            for x := 5 downto 1 - 10/5 do
                                Sha.getString();
                                io.writeIntLn(x);
                                if x > 1 then
                                    x := x*2;
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """class abc {
                        static int getArea(int a,b){
                            for x := 5 downto 2 do
                                a := a/10;
                                Sha.getString();
                                io.writeIntLn(x);
                            for i := 1 to 100 do {
                                b := b+10;
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            return a+b;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """class Shape {
                        float getArea(){
                            a := "b";
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """class Shape {
                        float getArea(){
                            a := 3 - this.N;
                            return a % 10;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """class Shape {
                        float getArea(int abc, c){
                            if c == 1 && [abc < 1] then return 0;
                            tong := tong*abc + 1;
                            return this.getArea(abc/2, c-1);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """class Shape {
                        float getArea(){
                            this.Temp := 10;
                            return this.Temp;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = """class Shape {
                        float getArea(){
                            this.getName := this.B;
                            return 0;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))


