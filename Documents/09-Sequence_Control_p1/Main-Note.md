# SEQUENCE CONTROL

## Expressions

- Syntax: Infix,Prefix,Postfix
- Infix: (a + b) * (c - d)
- Prefix Notation:
  - Polish Prefix: * + a b - c d
  - Cambridge Polish Prefix: (* (+ a b) (- c d))
    - a+b+c=>(+abc)
  - Normal Prefix: *(+(a,b),-(c,d))
    - [LISP](https://www.tutorialspoint.com/lisp/lisp_lists.htm)
- Postfix Notation
  - Polish Postfix: a b + c d - *
  - Cambridge Polish Postfix: ((a b +) (c d -) *)
  - Normal Postfix: ((a,b)+,(c,d)-)
    - [Postscript](http://paulbourke.net/dataformats/postscript/)
- Operand Evaluation Order

    ```c++
    int a = 5;
    int fun1() {
        a = 17;
        return 3;
    }
    void main() {
        a = a + fun1();
    }
    ```

  - C-lang: a = 20 (C# a=8). This because operands are computed first (side-effect).
  - Java: a = 8

- Short-Circuit Evaluation: (a == 0) || (b/a > 2

## Statements

- Assignment:
  - C-lang: a=2 is an expression that returns value of the most rhs operand.

- Two-way selection: If-statement (issue dangling else in C-lang).
- Multiple-way selection: Switch-statement.
- Loop

## Program Units
