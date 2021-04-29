try :
    x = int(input("x:"))
    y = int(input("Y:"))
except ValueError :
    print("Please enter numbers")
    exit(1)
try : 
    result = x / y
except ZeroDivisionError : 
    print("cant devide by 0")
    exit(1)

    exit(1)
print(result)
