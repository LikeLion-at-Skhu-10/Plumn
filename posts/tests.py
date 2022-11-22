a= int(input()) #a 입력받기
b= int(input()) #b 입력받기
c= int(input()) #c 입력받기

if(a<b):
    if(b<c):
        print(b)
elif(c<b):
    if(b<a):
        print(b)
elif(b<a):
    if(a<c):
        print(a)
elif(c<a):
    if(a<b):
        print(a)
elif(a<c):
    if(c<b):
        print(c)
elif(b<c):
    if(c<a):
        print(c)
else:
    print(a)