# -*- coding: utf-8 -*-
#intro function for the application with latest functionality details
def calcalc():
    #line spacing is repeated throughout the app to clarify the text display in the command line
    print("")
    print("CalCalc is a single-variable derivative and integral calculator that functions properly for most non-trig equations involving positive integer exponents. [Equations with π are currently not supported]")
    print("")
    values()
#this equation guides users in building the single-variable 
def values():
    print("")
    #this variable determines how many elements exist in ƒ(x)
    n = int(input("What is the exponent on the leading element of ƒ(x)? --> "))
    #save n for later reference; leadCoEx will be changed / n will not
    leadCoEx = n
    #equat is the array of n coefficients and a single constant for ƒ(x)
    equat = []
    while leadCoEx > -1 :
        #user input for coefficients
        if leadCoEx > 0 :
            print("")
            print("Enter the coefficient on the element of ƒ(x) with an exponent of " + str(leadCoEx) + ".")
            print("If no element exists, enter 0")
            coefs = int(input("--> "))
            equat.append(coefs)
            leadCoEx = leadCoEx - 1
        #user input for constant
        elif leadCoEx == 0:
            print("")
            print("Enter the Y-intercept of ƒ(x), including the case in which the constant is equal to 0.")
            constant = int(input("--> "))
            equat.append(constant)
            leadCoEx = leadCoEx - 1
    print("")
    #initialize the equation string to eventually be printed in terms of x
    equatStr = ""
    #iteration reference for forming the equation string
    rem = len(equat)
    for typeProxy in range(rem):
        #coefficient OR constant for THIS (typeProxy) iteration
        e = equat[typeProxy]
        #if e is the constant
        if typeProxy == (rem-1):
            #plus sign if positive, no sign if negative, nothing if e is 0
            if e > 0:
                equatStr += " + " + str(e)
            elif e < 0:
                equatStr += " " + str(e)
        #if e is the coefficient on a variable with no exponent (x or x^1)
        elif typeProxy == (rem-2):
            #if equatStr has not yet been changed for higher order equation elements
            #see EXPLAINED (elif typeProxy ==0) below for further details
            if equatStr == "":
                #no sign or initial space
                if e != 0:
                    equatStr += e + "x"
            else:
                #plus sign if positive, no sign if negative, nothing if e is 0
                if e > 0:
                    equatStr += " + " + str(e) + "x"
                elif e < 0:
                    equatStr += " " + str(e) + "x"
        #if e is the leading coefficient, assuming NO user input errors at the leading element exponent (n)
        elif typeProxy == 0:
            #EXPLAINED: if the user entered 3 as the exponent on the leading element (n), but meant 0, he/she might proceed anyways and enter 0 as the coefficient
            #on the element with an exponent of 3. This error should be accounted for, i.e. if 0 is entered here the equation string does not change
            if e != 0:
                equatStr += str(e) + "x^" + str(rem - 1 - typeProxy)
        #all other coefficients on variables with an exponent greater than 2 and less than n
        else:
            #see EXPLAINED: here, if the equation string is still blank because of an input error on n, no plus sign or additional spacing should be included at the front of the equation string
            if equatStr == "":
                if e != 0:
                    equatStr += str(e) + "x^" + str(rem - 1 - typeProxy)
            else:
                #plus sign if positive, no sign if negative, nothing if e is 0
                if e > 0:
                    equatStr += " + " + str(e) + "x^" + str(rem - 1 - typeProxy)
                elif e < 0:
                    equatStr += " " + str(e) + "x^" + str(rem - 1 - typeProxy)
    #print the equation in the console
    print("ƒ(x) = " + equatStr)
    #ask the user what they want to do with the equation
    def switch():
        #ask the user if they want to repeat the application for another equation, switch between integration and derivation or exit the application
        def repeat():
            print("")
            repeat = raw_input("Enter `restart` to enter a new equation or `switch` to do something different with the current equation; any other input will exit the application --> ")
            repeat = repeat.lower()
            if repeat == "restart":
                #start from the beginning to reset equation  
                values()
            elif repeat == "switch":
                #restart switch function to integrate or derive
                switch()
            else:
                #exit message and application close
                print("Thank you for using CalCalc! Check back soon for updates in our functionality ...")
                exit()
        print("")
        step = raw_input("Would you like to find the `integral` or the `derivative` of the equation? --> ")
        step = step.lower()
        if step == "integral":
            print("")
            #ask the user whether they want to integrate over a set of continuous values for x or in variable terms
            solType = raw_input("Type `num` if the integral solution you are looking for is numerical. Alternatively, press ENTER if the solution should be calculated in variable terms only --> ")
            solType = solType.lower()
            #numerical
            if solType == "num":
                print("")
                val1 = int(input("Lower limit across the X-axis --> "))
                val2 = int(input("Upper limit across the X-axis --> "))
                #integrate with these limits included in the function arguments
                integrate(equat, val1, val2)
                repeat()
            #variable
            else:
                #integrate without limits included in the function arguments
                integrate(equat)
                repeat()
        elif step == "derivative":
            print("")
            #ask the user whether they are looking for a numerical derivative or a variable derivative
            solType = raw_input("Type `num` if the derivative solution you are looking for is numerical. Alternatively, press ENTER if the solution should be calculated in variable terms only--> ")
            solType = solType.lower()
            #numerical
            if solType == "num":
                print("")
                #what is x equal to
                varVal = int(input("Solve the derivative where x is equal to --> "))
                #pass the x value into the derivative function arguments
                derivative(equat, varVal)
                repeat()
            #variable
            else:
                #no x value in the derivative function arguments
                derivative(equat)
                repeat()
        #repeat if neither was entered
        else:
            step = raw_input("That is not a proper command. Would you like to find the `integral` or the `derivative` of the equation? --> ")
            return
    #call the switch function for the first time
    switch()
    print("")
def integrate(array, lim1="na", lim2="na"):
	#initialize integral coefficient list and variable integral string
    integral = []
    intStr = ""
    #initialize the lower integral solution (solution where x = lim1) and higher integral solution (where x = lim2)
    loInt = 0
    hiInt = 0
    #length of the initial equation coefficient list (ƒ(x))
    rem = len(array)
    for typeProxy in range(rem):
    	#set the value to manipulate based on integral formulation
        e = array[typeProxy]
        #if the current reference is the last element in the list
        if typeProxy == (rem-1):
        	#add the integral coefficient to the array and then update the string (logic: constant of ƒ(x) to constant*x)
            integral.append((e/(rem-typeProxy)))
            #if string is still blank (error mentioned in values())
            if intStr == "":
                if e != 0:
                    intStr += str(e) + "x"
       		#positive or negative
            else:
                if e > 0:
                    intStr += " + " + str(e) + "x"
                elif e < 0:
                    intStr += " " + str(e) + "x"
        #if the current reference is the first element in the list
        elif typeProxy == 0:
        	#append the coefficient
            integral.append((e/(rem)))
            if (e % rem) == 0:    
                if e != 0:
                    intStr += str(e/rem) + "x^" + str(rem)
            else:
                if e != 0:
                    intStr += "(" + str(e) + "/" + str(rem) + ")x^" + str(rem)
        #all other elements in the equation to be included in the integral
        else:
            integral.append((e/(rem-typeProxy)))
        	#if the integral string doesn't exist yet (see error in values())
            if intStr == "":
                if e != 0:
                    if (e % (rem-typeProxy)) == 0:
                        intStr += str(e/(rem-typeProxy)) + "x^" + str(rem-typeProxy)
                    else:
                        intStr += "(" + str(e) + "/" + str(rem-typeProxy) + ")x^" + str(rem-typeProxy)
            #integral formula logic
            else:
                if e != 0:
                	#integer or float
                    if (e % (rem-typeProxy)) == 0:
                        if e > 0:
                            intStr += " + " + str(e/(rem-typeProxy)) + "x^" + str(rem-typeProxy)
                        elif e < 0:
                            intStr += " " + str(e/(rem-typeProxy)) + "x^" + str(rem-typeProxy)
                    #fractional
                    else:
                        if e != 0:
                            intStr += " + " + "(" + str(e) + "/" + str(rem-typeProxy) + ")x^" + str(rem-typeProxy)
    #numerical integral calculation
    if lim1 != "na":
        rem = len(integral)
        for i in range(rem):
            e = integral[i]
            exp = rem - 1 - i
            loInt += (e*lim1)**exp
            hiInt += (e*lim2)**exp
        ifx = hiInt - loInt
        print("")
        print("∫ƒ(x)dx = " + intStr + " + c")
        print("")
        print("The integral of this equation from x = " + str(lim1) + " to x = " + str(lim2) + " is " + str(ifx) + " units^2.")
    #indefinite integral string presentation
    else:
        print("")
        print("∫ƒ(x)dx = " + intStr + " + c")      
def derivative(array, val="na"):
	#initialize the string, derivative coefficient array and numerical derivative value
    dStr = ""
    deriv = []
    dx = 0
    rem = len(array)
    #first order derivative string formulation logic with logic for avoiding unnecessary operators
    for typeProxy in range(rem):
        e = array[typeProxy]
        if typeProxy == (rem - 1):
            break
        elif typeProxy == (rem - 2):
            deriv.append((rem-1-typeProxy)*e)
            if e > 0:
                dStr += " + " + str(e)
            elif e < 0:
                dStr += " " + str(e)
        elif typeProxy == (rem - 3):
            deriv.append((rem-1-typeProxy)*e)
            if dStr == "":
                if e != 0:
                    dStr += str(2*e) + "x"
            else:
                if e > 0:
                    dStr += " + " + str(2*e) + "x"
                elif e < 0:
                    dStr += " " + str(2*e) + "x"
        elif typeProxy == 0:
            deriv.append((rem-1-typeProxy)*e)
            if e != 0:
                dStr += str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
        else:
            deriv.append((rem-1-typeProxy)*e)
            if dStr == "":
                if e != 0:
                    dStr += str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
            else:
                if e > 0:
                    dStr += " + " + str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
                elif e < 0:
                    dStr += " " + str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
    #initialize second order derivative string, coefficient array and numerical value
    ddStr = ""
    derivTwo = []
    ddx = 0
    rem = len(deriv)
    #second order derivative string formulation with logic for avoiding unnecessary operations
    for typeProxy in range(rem):
        e = deriv[typeProxy]
        if typeProxy == (rem - 1):
            break
        elif typeProxy == (rem - 2):
            derivTwo.append((rem-1-typeProxy)*e)
            if e > 0:
                ddStr += " + " + str(e)
            elif e < 0:
                ddStr += " " + str(e)
        elif typeProxy == (rem - 3):
            derivTwo.append((rem-1-typeProxy)*e)
            if ddStr == "":
                if e != 0:
                    ddStr += str(2*e) + "x"
            else:
                if e > 0:
                    ddStr += " + " + str(2*e) + "x"
                elif e < 0:
                    ddStr += " " + str(2*e) + "x"
        elif typeProxy == 0:
            derivTwo.append((rem-1-typeProxy)*e)
            if e != 0:
                ddStr += str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
        else:
            derivTwo.append((rem-1-typeProxy)*e)
            if ddStr == "":
                if e != 0:
                    ddStr += str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
            else:
                if e > 0:
                    ddStr += " + " + str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
                elif e < 0:
                    ddStr += " " + str(e*(rem-1-typeProxy)) + "x^" + str(rem - 2 - typeProxy)
    #if numerical derivative
    if val != "na":
        rem = len(deriv)
        torem = len(derivTwo)
        for i in range(rem):
            e = deriv[i]
            exp = rem - 1 - i
            if exp > 0:
                dx += (e*val)**exp
            else:
                dx += e
        for i in range(torem):
            e = derivTwo[i]
            exp = torem - 1 - i
            if exp > 0: 
                ddx += (e*val)**exp
            else:
                ddx += e    
        print("")
        print("ƒ'(x) = " + dStr + " | ƒ'(" + str(val) + ") = " + str(dx))
        print("")
        print("ƒ''(x) = " + ddStr + " | ƒ''(" + str(val) + ") = " + str(ddx))
    #if variable derivative spit out strings without dx and ddx
    else:
        print("")
        print("ƒ'(x) = " + dStr)
        print("")
        print("ƒ''(x) = " + ddStr)
#run the calculator at onset
calcalc()
