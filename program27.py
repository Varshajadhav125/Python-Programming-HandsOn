power = lambda no : no * no

print("Enter element you want to power")
size = int(input())

print("Enter element")
for i in range(0,size):
    no = int(input())
    ans = power(no)
    print("power is",ans)




