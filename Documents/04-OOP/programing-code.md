# PC

## Q1

```python
class Lit:
    def eval(self):
        pass

class Exp():
    def eval(self):
        pass

class IntLit(Lit):
    def __init__(self,x):
        self.val = int(x)
        
    def eval(self):
        return self.val
        
class FloatLit(Lit):
    def __init__(self,x):
        self.val = float(x)
        
    def eval(self):
        return self.val
        
class BinExp(Exp):
    def __init__(self,l,op:str,r):
        self.op = op
        self.l  = l.eval()
        self.r  = r.eval()

    
    def eval(self):
        if self.op == "+":
            return self.l+self.r
        if self.op == "-":
            return self.l-self.r
        if self.op == "*":
            return self.l*self.r
        if self.op == "/":
            return self.l/self.r
        
class UnExp(Exp):
    
    def __init__(self,op:str,e):
        self.op = op
        self.e  = e
        
    def eval(self):
        if self.op == "+":
            return +self.e.eval()
        if self.op == "-":
            return -self.e.eval()
            

```

## Q2

```python
class Lit:
    def eval(self):
        pass
    def printPrefix(self):
        pass
    
class Exp():
    def eval(self):
        pass
    def printPrefix(self):
        pass

class IntLit(Lit):
    def __init__(self,x):
        self.val = int(x)
        
    def printPrefix(self):
        return str(self.val)
        
    def eval(self):
        return self.val
        
class FloatLit(Lit):
    def __init__(self,x):
        self.val = float(x)
        
    def printPrefix(self):
        return str(self.val)
        
    def eval(self):
        return self.val
        
class BinExp(Exp):
    def __init__(self,l,op:str,r):
        self.op = op
        self.l = l
        self.r = r
        self.l_val  = l.eval()
        self.r_val  = r.eval()
    
    def printPrefix(self):
        _l = self.l.printPrefix() 
        _r = self.r.printPrefix()
        return self.op + " " + _l + " " + _r
    
    def eval(self):
        if self.op == "+":
            return self.l_val+self.r_val
        if self.op == "-":
            return self.l_val-self.r_val
        if self.op == "*":
            return self.l_val*self.r_val
        if self.op == "/":
            return self.l_val/self.r_val
        
class UnExp(Exp):
    
    def __init__(self,op:str,e):
        self.op = op
        self.e  = e
        
    def eval(self):
        if self.op == "+":
            return +self.e.eval()
        if self.op == "-":
            return -self.e.eval()
        
    def printPrefix(self):
        _e = self.e.printPrefix()
        return self.op + ". " + str(_e)
            
```

## Q3

```python
class Eval:
    def visitBinExp(self, exp):
        if exp.op == "+":
            return exp.l.accept(self)+exp.r.accept(self)
        if exp.op == "-":
            return exp.l.accept(self)-exp.r.accept(self)
        if exp.op == "*":
            return exp.l.accept(Eval())*exp.r.accept(Eval())
            
    def visitUnExp(self, exp):
        if exp.op == "+":
            return +exp.e.accept(self)
        if exp.op == "-":
            return -exp.e.accept(self)
            
    def visitLit(self,lit):
        return lit.val
    

class PrintPrefix:
    def visitBinExp(self, exp):
        _l = exp.l.accept(self)
        _r = exp.r.accept(self)
        return exp.op + " " + _l + " " + _r
        
    def visitUnExp(self, exp):
        _e = exp.e.accept(self)
        return exp.op + ". " + str(_e)
            
    def visitLit(self,lit):
        return str(lit.val)

class PrintPostfix:
    def visitBinExp(self, exp):
        _l = exp.l.accept(PrintPostfix())
        _r = exp.r.accept(PrintPostfix())
        return _l + " " + _r + " "  + exp.op
    def visitUnExp(self, exp):
        _e = exp.e.accept(PrintPostfix())
        return str(_e) + " " + exp.op + "."
        
    def visitLit(self,lit):
        return str(lit.val)

class Lit:
    def accept(self,cmd):
        pass
    
class Exp():
    def accept(self,cmd):
        pass

class IntLit(Lit):
    def __init__(self,x):
        self.val = int(x)
        
    def accept(self,cmd):
        return cmd.visitLit(self)
        
class FloatLit(Lit):
    def __init__(self,x):
        self.val = float(x)
        
    def accept(self,cmd):
        return cmd.visitLit(self)
        
class BinExp(Exp):
    def __init__(self,l,op:str,r):
        self.op = op
        self.l = l
        self.r = r
    
    
    def accept(self,cmd):
        return cmd.visitBinExp(self)
        

        
class UnExp(Exp):
    
    def __init__(self,op:str,e):
        self.op = op
        self.e  = e
        
    def accept(self,cmd):
        return cmd.visitUnExp(self)

```