print("Choose your temperature conversion units")
while True:
    print("Enter 1 for kelvin to celsius")
    print("Enter 2 for celsius to kelvin")
    print("Enter 3 for fahrenheit to celsius")
    print("Enter 4 for celsius to fahrenheit")
    print("Enter 5 for kelvin to fahrenheit")
    print("Enter 6 for fahrenheit to kelvin")
    print("Enter any other key to exit\n")
    ch=input("-->")
    if ch == '1':
        temp=float(input("Enter temperature in kelvin"))
        new_temp=temp-273.15
        print(temp,"kelvin is ",round(new_temp,2),"degree celsius\n")
    elif ch == '2':
        temp=float(input("Enter temperature in celsius"))
        new_temp=temp+273.15
        print(temp,"degree celsius is",round(new_temp,2),"kelvin\n")
    elif ch == '3':
        temp=float(input("Enter temperature in fahrenheit"))
        new_temp=(5*(temp-32))/9
        print(temp,"degree fahrenheit is",round(new_temp,2),"degree celsius\n")
    elif ch == '4':
        temp=float(input("Enter temperature in celsius"))
        new_temp=(9*temp)/5 +32
        print(temp,"degree celsius is",round(new_temp,2),"degree fahrenheit\n")
    elif ch == '5':
        temp = float(input("Enter temperature in kelvin"))
        new_temp=(9*(temp-273.15))/5 +32
        print(temp, "kelvin is ", round(new_temp,2), "degree fahrenheit\n")
    elif ch == '6':
        temp = float(input("Enter temperature in fahrenheit"))
        new_temp=(5*(temp-32))/9 +273.15
        print(temp, "degree fahrenheit is", round(new_temp,2), "kelvin\n")
    else:
        break

