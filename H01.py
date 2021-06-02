```
# name: ?????????????????  <----  put your name here!!!!


'''
Copy everything in this description and save it as 'H01_work.py'.


Fix the function eval(self, exprn) so that it can evaluate any expression of sums of non-negative fractions.
The function returns the sum as a string (an integer or reduced fraction) if the expression is legal;
   it returns the string 'ERROR' otherwise.

Note:
   There may be spaces between numbers and symbols in the input expression.  The output of eval() does
       not contain any space.
   The input expression may contains non-reduced fractions such as 12/20, 70/25, and 40/8. The output
       must be simplified: either an integer or a reduced fraction.
   The slash '/' is part of the fractional notation, do NOT perform any division! With a finite number
       of storage of digits in decimal numbers, it is impossible to convert back and forth between
       a fraction and its decimal representation.
   You must solve this problem from the scratch, use only the basic Python string methods.  You will
       parse the expression using a somewhat naive and brute-force approach. Do NOT use regular
       expressions methods, parsers, finite machines or any libraries. You will learn sophisticated
       theories and methods to evaluate much more complicated expressions later in this course.
   Do not change any of the following:
       class name:                                       H01
       name and signature of the constructor:            __init(self)__
       name and signature of the 'target' function:      eval(self, exprn)
       file name:                                        H01_work.py
   Make sure your name appear as a comment at the VERY TOP of this file.
   Submit 'H01_work.py' to Codegrade before the due date.


Examples of legal expressions and their answers:
 0                ==>   0
 3                ==>   3
 3/1              ==>   3
 15 / 5           ==>   3
 2 +4/1+0         ==>   6
 0  + 0/1  +  0/2  + 0/3             ==>   0
 1/2 +     1/   3 + 0/5 + 1/4        ==>   13/12
 2 + 2/3 + 5/12     + 1   /6         ==>   13/4
 1/2 + 3/4 + 5/6 +      7/8          ==>   71/24
 4/100 + 16/100 +50/100+30/100+0                       ==>   1
 10 / 20 +  30  /  19 +22 /15                          ==>   2021/570
 6 / 4  +  21 /5 + 29  /  17 +9 / 19                   ==>   25451/3230
 12  /12+25 /7+ 29+ 22/ 18                             ==>   2192/63
 1/2 + 3/4 + 5/6 + 7/8+9/10+11    /   12 + 13/14       ==>   1597/280
 123/456 + 789/98765 + 432                                        ==>   6489474253/15012280
 70/1440 + 31/2500 + 11/6480 + 13/625                             ==>   33821/405000
 0 + 1 + 2/1 + 3/10 + 4/100 + 5/1000 + 6/10000 + 7/100000         ==>   334567/100000
 9/1 + 8/7 + 6/5 + 4/3 + 2/1 + 1/2 + 3/4 + 5/6 + 7/8 + 10         ==>   23213/840
 4321+1/2 + 10/3+ 100/4 + 1000/5 + 10000/6 + 100000/7 + 10/98765  ==>   5669723371/276542

Examples of illegal expressions, the eval() returns 'ERROR'
                       (empty string)
 1.2                   (decimal points not allowed)
 457c                  (not a number)
 3/                    (not a fraction)
 /7                    (not a fraction)
 1.0  + 4/5            (decimal points not allowed)
 4  3                  (missing addition sign)
 3/2 @ 5/6             (illegal character)
 hello                 (not a mathematical expression)
 3/2 + + 5/6           (illegal use of plus sign)
 3/2 + ( 1 +2)         (no parentheses allowed)
 3/2 - 0/6             (only additions allowed)
 1/2 * 1/3 + 1/4       (only additions allowed)
 2 + 6/0 +  4/1        (fractions can not have zero in the denominators)
More examples of illegal expressions:
 2 +  2/3 + /12 + 9
 1/2 + 3//4 + 5/6 + 7/8
 1/8 + + 2/3
 1/2 + 3//4 + 5/6 + 7/8

========================  HINTS  ====================
Add as many variables and methods as necessary.

Add method(s) to test your 'eval' function.
   (or create another class to test the 'eval' function of H01)


Here are some milestones for your program:

Milestone 1:   single integers
   0       ===>   0
   4       ===>   4
   25786   ===>   25786

Milestone 2:   single reduced fractions
   1/2     ===>   1/2
   4/15    ===>   4/15
   36/55   ===>   36/55

Milestone 3:   single non-reduced integers
   48/12   ===>   3
   80/5    ===>   16
   5/1     ===>   5

Milestone 4:   single non-reduced fractions
   4/12     ===>   1/3
   36/15    ===>   12/5
   770/49   ===>   110/7

Milestone 5:   sum of two terms (integers or fractions)
   3 + 4             ===>   7
   2 + 16/20         ===>   14/5
   32/12 + 105/30    ===>   37/6

Milestone 6:   sum of three or more terms
   3 + 4 + 10                     ===>   17
   2 + 0 + 4/3                    ===>   10/3
   3/2 + 5/8 + 1/8 + 3/4          ===>   3
   1/2 + 3/8 + 1/6 + 7/8          ===>   71/24
   62/59 + 25 + 70/38 + 21/8      ===>   273685/8968
   4321 + 1/2 + 10/3 + 100/4 + 1000/5 + 10000/6 + 100000/ 7 + 10/98765  ===>  5669723371/276542


IMPORTANT:
   Make sure eval() returns 'ERROR' for illegal expression.

------------------------------------------------------------------------------------------------------
'''
class H01:
    def __init__(self):
        pass
    def eval(self,exprn):
        numbers = exprn.split('+')
        total = 0
        number = 0
        denom = 1

        if len(exprn) == 0:
            return "Error"
        for i in exprn:
            if i == '/' or i in '1234567890' or i == '+' or i == " ":
                pass
            else:
                return "ERROR"
        for number in numbers:
            if "/" not in number:
                number = number.strip()
                try:
                    total += int(number)
                except:
                    return "ERROR"
            else:
                try:
                    number = number.strip()
                    nnum,nden = number.split('/')
                    if nnum == '0' or nden == '0':
                        return "EEROR"
                    else:
                        num = (int(nnum)*denom) + num * int(nden)
                        den = (int(nnum)*denom)
                except:
                    return "ERROR"
        num = num + total * den
        total = self.reduce_fraction(num,den)

        if total.split('/')[1] == '1':
            total = total.split('/')[0]
        return total

    def reduce_fraction(self,num,den):
        gcd = self.gcd(num,denom)

        num=num // gcd
        denom=denom // gcd

        return "%d/%d"%(num,denom)
    
    def gcd(self,num,dem):
        if dem == 0:
          return num
        return self.gcd(dem,num%dem)

if __name__ == '__main__':
  print(eval('36/15'))
