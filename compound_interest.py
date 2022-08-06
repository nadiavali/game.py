def final_amt(p, r, n, t):
    
    a = p * (1+ r/n) ** (n*t)
    return a

toInvest = float(input('How much you wanna invest?'))
fnl= final_amt(toInvest, 0.08, 12, 5)
print('At the end of the period you will have', fnl)
