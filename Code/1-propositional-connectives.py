# not operator
# p = the value is less than 10
p=8
print(p<10)

p=15
print(p<10)

p=8
print(not(p<10))

p=15
print(not(p<10))

# AND - conjunction
# p = the value is less than 10
# q = the value is less than 20
p,q=8,16
print(p<10 and q<20)  # True and True = True

p,q=8,26
print(p<10 and q<20)  # True and False = False

p,q=18,16
print(p<10 and q<20)  # False and True = False

p,q=18,26
print(p<10 and q<20)  # False and False = True

# OR - disjunction
# p = the value is less than 10
# q = the value is less than 20
p,q=8,16
print(p<10 or q<20)  # T and T = T

p,q=8,26
print(p<10 or q<20)  # T and F = F

p,q=18,16
print(p<10 or q<20)  # F and T = F

p,q=18,26
print(p<10 or q<20)  # F and F = T

# XOR - disjunction
# p = the value is less than 10
# q = the value is less than 20
p,q=8,16
print((p<10) != (q<20))  # T and T = F

p,q=8,26
print((p<10) != (q<20))  # T and F = T

p,q=18,16
print((p<10) != (q<20))  # F and T = T

p,q=18,26
print((p<10 != q<20))  # F and F = F

# Implication if-then
# p = the value is less than 10
# q = the value is less than 20
p,q=8,16
if(p<10):       # T
    print(q<20) # T
p,q=8,26
if(p<10):       # T
    print(q<20) # F
p,q=18,16
if(p<10):       # F
    print(q<20) # T ?
p,q=18,26
if(p<10):       # F
    print(q<20) # F ?

# Converse for p->q, q->p is converse
# p = the value is less than 10
# q = the value is less than 20
q,p=8,16
if(q<10):       # T
    print(p<20) # T
q,p=8,26
if(q<10):       # T
    print(p<20) # F
q,p=18,16
if(q<10):       # F
    print(p<20) # T ?
q,p=18,26
if(q<10):       # F
    print(p<20) # F ?

# inverse: for p->q, inverse is (not p -> not q)
p,q=8,16
if(not(p<10)):       # T
    print(not(q<20)) # T
p,q=8,26
if(not(p<10)):       # T
    print(not(q<20)) # F
p,q=18,16
if(not(p<10)):       # F
    print(not(q<20)) # T ?
p,q=18,26
if(not(p<10)):       # F
    print(not(q<20)) # F ?
