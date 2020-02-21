p=int(input())
q=bin(p)
print(q)
q=q[2:]
print(q)
print (max(map(len, q.split('0')))) 
