n=int(input('Enter any number : '))
x=str(n)
def checkarm():
    v=len(x)
    s=0
    for i in x :
        s=s+int(i)**v
    if s==n:
        print("Number Is Armstrong")
checkarm()