number = int(input("Enter a number:"))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print("is a prime number")                       
else:
            print("is a not prime number")    
                                 