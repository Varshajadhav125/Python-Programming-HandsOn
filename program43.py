def display(No):
    if(No > 0):
        print("*",end = " ") #end function is used for display on new line
        No  = No - 1
        display(No)

display(5)

