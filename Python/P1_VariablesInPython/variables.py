#Rules for variable names:
# Should be meaning name
# Alphanumeric & underscore is allowed - no other special character even space.
# Start with letters or underscore
#Should not be a keyword/reserve word
# Python keywords
#None, break, except, in, raise, False, await, else, import, pass, and,
#continue, for, lambda, try, True, class, finally, is, return, as, def,
#from, nonlocal, while, async, elif, if, not, with, assert, del, global,
#or, yield
#Multiple Declaration
name, price, qty = 'soap', 12.5, 5
print(name, price, qty)
print(id(name), id(price), id(qty))

a,b,c = 1,1,1
print(a, b, c)
#As the values are same for 3 different variables so the python point all 3 variable to one location with value 1 can be seen as below
print(id(a), id(b), id(c))

length = 15
print(length)

prices = [10,7,8,9]
print(prices)

# Dynamically Types:
a = 15
b = 12.75
c = 'sanjeev'
print(a, b, c)
a = 'gaikwad' #a pointed to latest new value in memory.
print(a)

a = 15
print(type(a))

a = 12.45
print(type(a))

a = 'agd'
print(type(a))

a = [10,11,12,13]
print(type(a))

#False = 10 #Give syntax error
print(False)
false = 21  #Allowed
print(type(false))
