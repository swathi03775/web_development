s=[1,2,3,4,5,-9]
for i in s:
    if(i==0):
        print("invalid input")
    prime=False
    for k in range(2,i):
        if i%k!=0:
            prime=True
            break
    else:
        print(i)

