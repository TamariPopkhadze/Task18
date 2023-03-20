div = input()
numbers = div.split("/")
try:
    x = int(numbers[0])
    y = int(numbers[1])
except ValueError:
    print("your numerator and denominator should be Integer") 
else:     
 try:
    div = int ((x / y) * 100)
 except ZeroDivisionError:
    print("ZeroDivisionError")
 else:
    if div <= 1:
        print("E")
    elif div >= 99 and div <= 100 :
        print ("F")
    elif div > 100:
        print("numerator should be less or equal than denominator")    
    else:
        print (str(div) + "%") 


