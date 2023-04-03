numb = int(input())
 
for i in range(2,numb+1):
    if i > numb**0.5 + 1 and numb >1:
        i = int(numb)
        print(i,end=" ")
        break
    while(numb%i == 0):
        print(i,end=" ")
        numb /= i