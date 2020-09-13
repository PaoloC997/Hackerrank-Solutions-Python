
#Compare the triplets

a0,a1,a2 = [1,7,9]
A = a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = [1,2,3]
B = b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice = bob = 0

for x,y in zip(A,B):
    if x>y: alice += 1
    if x<y: bob += 1
    result = (alice,bob)