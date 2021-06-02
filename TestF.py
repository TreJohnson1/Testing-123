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
