def display(No):
    if(No > 0):
        display(No - 1)# ya madhe adhi display function madhe no store zala ani nantr No - 1 statement apply zaal.------recursion call using head concept
        print(No)

display(5)