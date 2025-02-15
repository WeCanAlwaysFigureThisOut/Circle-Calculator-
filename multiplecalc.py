def taxes(money, taxrate):
    totaldue = money + (money * taxrate / 100)
    return totaldue


taxes_due = taxes(20, 6)
print("The total due with a 6% tax on $20 is", taxes_due)
taxes_due = taxes(54, 4)
print("The total due with a 4% tax on $20 is", taxes_due)
taxes_due = taxes(68, 8)
print("The total due with a 8% tax on $20 is", taxes_due)

