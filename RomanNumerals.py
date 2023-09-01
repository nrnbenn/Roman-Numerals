def NumeralsToDecimal(numerals):
    
    numerals = numerals.lower()

    #define numerals
    i = 1
    v = 5
    x = 10
    l = 50
    c = 100
    d = 500
    m = 1000
    
    total = 0

    #turn numerals into list
    listofchars = []
    for a in range(len(numerals)):
        listofchars.append(numerals[a])
    
    listofchars.reverse()

    #translate
    on = -1
    for b in listofchars:
        on += 1
        if b == "i":
            total += i
        else:
            #get number
            if b == "v":
                number = v
            elif b == "x":
                number = x
            elif b == "l":
                number = l
            elif b == "c":
                number = c
            elif b == "d":
                number = d
            elif b == "m":
                number = m

            #get before number in list if not on last rotation
            if not on-1 == -1:
                beforechar = listofchars[on-1]
            
                if beforechar == "x":
                    beforenumber = v
                elif beforechar == "x":
                    beforenumber = x
                elif beforechar == "l":
                    beforenumber = l
                elif beforechar == "c":
                    beforenumber = c
                elif beforechar == "d":
                    beforenumber = d
                elif beforechar == "m":
                    beforenumber = m
            else:
                beforenumber = 0

            #translate
            if number <= beforenumber:
                total += number
            elif number > beforenumber:
                total += (number-beforenumber)

    return(total)


            



#Main
print("Hello")
if input("If you would like to do Roman Numerals to Decimal, Input '1'.") == "1":
    print("You are in Roman Numerals To Decimal Mode")
    print("")
    print(NumeralsToDecimal(input("Please input your numerals that you would like to translate")))

else:
    print("That is not an option")