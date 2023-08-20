def display(No):
    if(No > 0):
        print(No)
        No = No - 1
        display(No) #recursion call using tail concept

display(5)     

def display(value):
    print("Enter how many element you want to store")
    store = int(input())
    ans = 0
    
    for i in range(1,store+1):
        no = int(input())
        value.append(no)
        
    #print("addition is",ans)
    return ans

