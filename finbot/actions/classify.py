# This class returns the hklv bucket classification according to the rules

def my_classifier(data):
    name = data['name']

    age = int(data['age'])

    income_nature = "Adhoc" if data['employement_status']=="False" else "Regular"

    income = data['annual_income']
    income = income.replace(",","")                                                                 #data is processed and assigned 
    income = float(income)                                                                            #to the respectve field variables

    martial_status = "Married" if data['marital_status'] == "True" else "Unmarried"

    no_of_depedents = int(data['number_of_dependents'])

    annual_liability  = "not defined"

    result = []                         #for every cassification step an identifier will be added to the list

    if age>15 and age<25 :
        result.append("AGE-CAT1")                               #first identifier
        if income_nature == "Adhoc":
            result.append("A")                                  #second
            if income<=6185.78:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 6185.78 and income<=13605.22:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >13605.22 and income<=23382:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >23382:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")

        else:
            result.append("R")
            if income<=6185.78:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 6185.78 and income<=13605.22:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >13605.22 and income<=23382:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >23382:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")




    elif age>24 and age < 35:
        result.append("AGE-CAT2")
        if income_nature == "Adhoc":
            result.append("A")
            if income<=23986.90:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 23986.90 and income<=40274.30:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >40274.30 and income<=62683.70:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >62683.70:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")
        else:
            result.append("R")
            if income<=23986.90:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 23986.90 and income<=40274.30:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >40274.30 and income<=62683.70:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >62683.70:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")



    elif age>34 and age <45 :
        result.append("AGE-CAT3")
        if income_nature == "Adhoc":
            result.append("A")
            if income<=29306.90:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 29306.90 and income<=50838.60:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >50838.60 and income<=84640.40:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >84640.40:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")
        else:
            result.append("R")
            if income<=29306.90:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 29306.90 and income<=50838.60:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >50838.60 and income<=84640.40:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >84640.40:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")



    else:
        result.append("AGE-CAT4")
        if income_nature == "Adhoc":
            result.append("A")
            if income<=30473.97:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 30473.97 and income<=53266.42:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >53266.42 and income<=91856.06:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >91856.06:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")
        else:
            result.append("R")
            if income<=30473.97:
                result.append("IN-CAT1")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income > 30473.97 and income<=53266.42:
                result.append("IN-CAT2")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >53266.42 and income<=91856.06:
                result.append("IN-CAT3")                        #third
                if martial_status == "Married":
                    result.append("M")                          #fourth
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents < 3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
            elif income >91856.06:
                result.append("IN-CAT4")
                if martial_status == "Married":
                    result.append("M")
                    if no_of_depedents<3:
                        result.append("-3")
                    elif no_of_depedents == 3:
                        result.append(".3")
                    else:
                        result.append("+3")
                else:
                    result.append("U")
                    if no_of_depedents<3:
                            result.append("-3")
                    elif no_of_depedents == 3:
                            result.append(".3")
                    else:
                        result.append("+3")
    mapp = {'AGE-CAT1/A/IN-CAT1/M/-3': '1', 'AGE-CAT1/A/IN-CAT1/M/+3': '1', 'AGE-CAT1/A/IN-CAT1/M/.3': '1', 'AGE-CAT1/A/IN-CAT1/U/-3': '1', 'AGE-CAT1/A/IN-CAT1/U/+3': '1', 'AGE-CAT1/A/IN-CAT1/U/.3': '1', 'AGE-CAT1/A/IN-CAT2/M/-3': '2', 'AGE-CAT1/A/IN-CAT2/M/+3': '2', 'AGE-CAT1/A/IN-CAT2/M/.3': '2', 'AGE-CAT1/A/IN-CAT2/U/-3': '2', 'AGE-CAT1/A/IN-CAT2/U/+3': '2', 'AGE-CAT1/A/IN-CAT2/U/.3': '2', 'AGE-CAT1/A/IN-CAT3/M/-3': '3', 'AGE-CAT1/A/IN-CAT3/M/+3': '3', 'AGE-CAT1/A/IN-CAT3/M/.3': '3', 'AGE-CAT1/A/IN-CAT3/U/-3': '3', 'AGE-CAT1/A/IN-CAT3/U/+3': '3', 'AGE-CAT1/A/IN-CAT3/U/.3': '3', 'AGE-CAT1/A/IN-CAT4/M/-3': '4', 'AGE-CAT1/A/IN-CAT4/M/+3': '4', 'AGE-CAT1/A/IN-CAT4/M/.3': '4', 'AGE-CAT1/A/IN-CAT4/U/-3': '4', 'AGE-CAT1/A/IN-CAT4/U/+3': '4', 'AGE-CAT1/A/IN-CAT4/U/.3': '4', 'AGE-CAT1/R/IN-CAT1/M/-3': '1', 'AGE-CAT1/R/IN-CAT1/M/+3': '1', 'AGE-CAT1/R/IN-CAT1/M/.3': '1', 'AGE-CAT1/R/IN-CAT1/U/-3': '1', 'AGE-CAT1/R/IN-CAT1/U/+3': '1', 'AGE-CAT1/R/IN-CAT1/U/.3': '1', 'AGE-CAT1/R/IN-CAT2/M/-3': '2', 'AGE-CAT1/R/IN-CAT2/M/+3': '2', 'AGE-CAT1/R/IN-CAT2/M/.3': '2', 'AGE-CAT1/R/IN-CAT2/U/-3': '2', 'AGE-CAT1/R/IN-CAT2/U/+3': '2', 'AGE-CAT1/R/IN-CAT2/U/.3': '2', 'AGE-CAT1/R/IN-CAT3/M/-3': '3', 'AGE-CAT1/R/IN-CAT3/M/+3': '3', 'AGE-CAT1/R/IN-CAT3/M/.3': '3', 'AGE-CAT1/R/IN-CAT3/U/-3': '3', 'AGE-CAT1/R/IN-CAT3/U/+3': '3', 'AGE-CAT1/R/IN-CAT3/U/.3': '3', 'AGE-CAT1/R/IN-CAT4/M/-3': '4', 'AGE-CAT1/R/IN-CAT4/M/+3': '4', 'AGE-CAT1/R/IN-CAT4/M/.3': '4', 'AGE-CAT1/R/IN-CAT4/U/-3': '4', 'AGE-CAT1/R/IN-CAT4/U/+3': '4', 'AGE-CAT1/R/IN-CAT4/U/.3': '4', 'AGE-CAT2/A/IN-CAT1/M/-3': '5', 'AGE-CAT2/A/IN-CAT1/M/+3': '5', 'AGE-CAT2/A/IN-CAT1/M/.3': '5', 'AGE-CAT2/A/IN-CAT1/U/-3': '5', 'AGE-CAT2/A/IN-CAT1/U/+3': '5', 'AGE-CAT2/A/IN-CAT1/U/.3': '5', 'AGE-CAT2/A/IN-CAT2/M/-3': '6', 'AGE-CAT2/A/IN-CAT2/M/+3': '6', 'AGE-CAT2/A/IN-CAT2/M/.3': '6', 'AGE-CAT2/A/IN-CAT2/U/-3': '6', 'AGE-CAT2/A/IN-CAT2/U/+3': '6', 'AGE-CAT2/A/IN-CAT2/U/.3': '6', 'AGE-CAT2/A/IN-CAT3/M/-3': '7', 'AGE-CAT2/A/IN-CAT3/M/+3': '7', 'AGE-CAT2/A/IN-CAT3/M/.3': '7', 'AGE-CAT2/A/IN-CAT3/U/-3': '7', 'AGE-CAT2/A/IN-CAT3/U/+3': '7', 'AGE-CAT2/A/IN-CAT3/U/.3': '7', 'AGE-CAT2/A/IN-CAT4/M/-3': '8', 'AGE-CAT2/A/IN-CAT4/M/+3': '8', 'AGE-CAT2/A/IN-CAT4/M/.3': '8', 'AGE-CAT2/A/IN-CAT4/U/-3': '8', 'AGE-CAT2/A/IN-CAT4/U/+3': '8', 'AGE-CAT2/A/IN-CAT4/U/.3': '8', 'AGE-CAT2/R/IN-CAT1/M/-3': '5', 'AGE-CAT2/R/IN-CAT1/M/+3': '5', 'AGE-CAT2/R/IN-CAT1/M/.3': '5', 'AGE-CAT2/R/IN-CAT1/U/-3': '5', 'AGE-CAT2/R/IN-CAT1/U/+3': '5', 'AGE-CAT2/R/IN-CAT1/U/.3': '5', 'AGE-CAT2/R/IN-CAT2/M/-3': '6', 'AGE-CAT2/R/IN-CAT2/M/+3': '6', 'AGE-CAT2/R/IN-CAT2/M/.3': '6', 'AGE-CAT2/R/IN-CAT2/U/-3': '6', 'AGE-CAT2/R/IN-CAT2/U/+3': '6', 'AGE-CAT2/R/IN-CAT2/U/.3': '6', 'AGE-CAT2/R/IN-CAT3/M/-3': '7', 'AGE-CAT2/R/IN-CAT3/M/+3': '7', 'AGE-CAT2/R/IN-CAT3/M/.3': '7', 'AGE-CAT2/R/IN-CAT3/U/-3': '7', 'AGE-CAT2/R/IN-CAT3/U/+3': '7', 'AGE-CAT2/R/IN-CAT3/U/.3': '7', 'AGE-CAT2/R/IN-CAT4/M/-3': '8', 'AGE-CAT2/R/IN-CAT4/M/+3': '8', 'AGE-CAT2/R/IN-CAT4/M/.3': '8', 'AGE-CAT2/R/IN-CAT4/U/-3': '8', 'AGE-CAT2/R/IN-CAT4/U/+3': '8', 'AGE-CAT2/R/IN-CAT4/U/.3': '8', 'AGE-CAT3/A/IN-CAT1/M/-3': '9', 'AGE-CAT3/A/IN-CAT1/M/+3': '9', 'AGE-CAT3/A/IN-CAT1/M/.3': '9', 'AGE-CAT3/A/IN-CAT1/U/-3': '9', 'AGE-CAT3/A/IN-CAT1/U/+3': '9', 'AGE-CAT3/A/IN-CAT1/U/.3': '9', 'AGE-CAT3/A/IN-CAT2/M/-3': '10', 'AGE-CAT3/A/IN-CAT2/M/+3': '10', 'AGE-CAT3/A/IN-CAT2/M/.3': '10', 'AGE-CAT3/A/IN-CAT2/U/-3': '10', 'AGE-CAT3/A/IN-CAT2/U/+3': '10', 'AGE-CAT3/A/IN-CAT2/U/.3': '10', 'AGE-CAT3/A/IN-CAT3/M/-3': '11', 'AGE-CAT3/A/IN-CAT3/M/+3': '11', 'AGE-CAT3/A/IN-CAT3/M/.3': '11', 'AGE-CAT3/A/IN-CAT3/U/-3': '11', 'AGE-CAT3/A/IN-CAT3/U/+3': '11', 'AGE-CAT3/A/IN-CAT3/U/.3': '11', 'AGE-CAT3/A/IN-CAT4/M/-3': '12', 'AGE-CAT3/A/IN-CAT4/M/+3': '12', 'AGE-CAT3/A/IN-CAT4/M/.3': '12', 'AGE-CAT3/A/IN-CAT4/U/-3': '12', 'AGE-CAT3/A/IN-CAT4/U/+3': '12', 'AGE-CAT3/A/IN-CAT4/U/.3': '12', 'AGE-CAT3/R/IN-CAT1/M/-3': '9', 'AGE-CAT3/R/IN-CAT1/M/+3': '9', 'AGE-CAT3/R/IN-CAT1/M/.3': '9', 'AGE-CAT3/R/IN-CAT1/U/-3': '9', 'AGE-CAT3/R/IN-CAT1/U/+3': '9', 'AGE-CAT3/R/IN-CAT1/U/.3': '9', 'AGE-CAT3/R/IN-CAT2/M/-3': '10', 'AGE-CAT3/R/IN-CAT2/M/+3': '10', 'AGE-CAT3/R/IN-CAT2/M/.3': '10', 'AGE-CAT3/R/IN-CAT2/U/-3': '10', 'AGE-CAT3/R/IN-CAT2/U/+3': '10', 'AGE-CAT3/R/IN-CAT2/U/.3': '10', 'AGE-CAT3/R/IN-CAT3/M/-3': '11', 'AGE-CAT3/R/IN-CAT3/M/+3': '11', 'AGE-CAT3/R/IN-CAT3/M/.3': '11', 'AGE-CAT3/R/IN-CAT3/U/-3': '11', 'AGE-CAT3/R/IN-CAT3/U/+3': '11', 'AGE-CAT3/R/IN-CAT3/U/.3': '11', 'AGE-CAT3/R/IN-CAT4/M/-3': '12', 'AGE-CAT3/R/IN-CAT4/M/+3': '12', 'AGE-CAT3/R/IN-CAT4/M/.3': '12', 'AGE-CAT3/R/IN-CAT4/U/-3': '12', 'AGE-CAT3/R/IN-CAT4/U/+3': '12', 'AGE-CAT3/R/IN-CAT4/U/.3': '12', 'AGE-CAT4/A/IN-CAT1/M/-3': '13', 'AGE-CAT4/A/IN-CAT1/M/+3': '13', 'AGE-CAT4/A/IN-CAT1/M/.3': '13', 'AGE-CAT4/A/IN-CAT1/U/-3': '13', 'AGE-CAT4/A/IN-CAT1/U/+3': '13', 'AGE-CAT4/A/IN-CAT1/U/.3': '13', 'AGE-CAT4/A/IN-CAT2/M/-3': '14', 'AGE-CAT4/A/IN-CAT2/M/+3': '14', 'AGE-CAT4/A/IN-CAT2/M/.3': '14', 'AGE-CAT4/A/IN-CAT2/U/-3': '14', 'AGE-CAT4/A/IN-CAT2/U/+3': '14', 'AGE-CAT4/A/IN-CAT2/U/.3': '14', 'AGE-CAT4/A/IN-CAT3/M/-3': '15', 'AGE-CAT4/A/IN-CAT3/M/+3': '15', 'AGE-CAT4/A/IN-CAT3/M/.3': '15', 'AGE-CAT4/A/IN-CAT3/U/-3': '15', 'AGE-CAT4/A/IN-CAT3/U/+3': '15', 'AGE-CAT4/A/IN-CAT3/U/.3': '15', 'AGE-CAT4/A/IN-CAT4/M/-3': '16', 'AGE-CAT4/A/IN-CAT4/M/+3': '16', 'AGE-CAT4/A/IN-CAT4/M/.3': '16', 'AGE-CAT4/A/IN-CAT4/U/-3': '16', 'AGE-CAT4/A/IN-CAT4/U/+3': '16', 'AGE-CAT4/A/IN-CAT4/U/.3': '16', 'AGE-CAT4/R/IN-CAT1/M/-3': '13', 'AGE-CAT4/R/IN-CAT1/M/+3': '13', 'AGE-CAT4/R/IN-CAT1/M/.3': '13', 'AGE-CAT4/R/IN-CAT1/U/-3': '13', 'AGE-CAT4/R/IN-CAT1/U/+3': '13', 'AGE-CAT4/R/IN-CAT1/U/.3': '13', 'AGE-CAT4/R/IN-CAT2/M/-3': '14', 'AGE-CAT4/R/IN-CAT2/M/+3': '14', 'AGE-CAT4/R/IN-CAT2/M/.3': '14', 'AGE-CAT4/R/IN-CAT2/U/-3': '14', 'AGE-CAT4/R/IN-CAT2/U/+3': '14', 'AGE-CAT4/R/IN-CAT2/U/.3': '14', 'AGE-CAT4/R/IN-CAT3/M/-3': '15', 'AGE-CAT4/R/IN-CAT3/M/+3': '15', 'AGE-CAT4/R/IN-CAT3/M/.3': '15', 'AGE-CAT4/R/IN-CAT3/U/-3': '15', 'AGE-CAT4/R/IN-CAT3/U/+3': '15', 'AGE-CAT4/R/IN-CAT3/U/.3': '15', 'AGE-CAT4/R/IN-CAT4/M/-3': '16', 'AGE-CAT4/R/IN-CAT4/M/+3': '16', 'AGE-CAT4/R/IN-CAT4/M/.3': '16', 'AGE-CAT4/R/IN-CAT4/U/-3': '16', 'AGE-CAT4/R/IN-CAT4/U/+3': '16', 'AGE-CAT4/R/IN-CAT4/U/.3': '16'}
    perc_map = {'1':[100,0],'2':[80,20],'3':[60,40],'4':[40,60],
                '5':[100,0],'6':[90,10],'7':[70,30],'8':[50,50],
                '9':[100,0],'10':[90,10],'11':[70,30],'12':[60,40],
                '13':[30,70],'14':[20,80],'15':[10,90],'16':[10,90]}
    ans="/"
    ans = ans.join(result)                                      #final values concatenated into one string
    return (ans,perc_map[mapp[ans]])                                      #and then returned along with a type mapping

# data = {
#             "name":"my name",
#             "age":"66",
#             "employement_status":"True",
#             "annual_income":"238000",
#             "marital_status":"True",
#             "number_of_dependents":"0"
#             }

# result = my_classifier(data)
# print(result)
# ans="/"
# ans = ans.join(result)
# #print(result)
# print("\n"+ans+"\n")
# mapp = {'AGE-CAT1/A/IN-CAT1/M/-3': 'type1', 'AGE-CAT1/A/IN-CAT1/M/+3': 'type2', 'AGE-CAT1/A/IN-CAT1/M/.3': 'type3', 'AGE-CAT1/A/IN-CAT1/U/-3': 'type4', 'AGE-CAT1/A/IN-CAT1/U/+3': 'type5', 'AGE-CAT1/A/IN-CAT1/U/.3': 'type6', 'AGE-CAT1/A/IN-CAT2/M/-3': 'type7', 'AGE-CAT1/A/IN-CAT2/M/+3': 'type8', 'AGE-CAT1/A/IN-CAT2/M/.3': 'type9', 'AGE-CAT1/A/IN-CAT2/U/-3': 'type10', 'AGE-CAT1/A/IN-CAT2/U/+3': 'type11', 'AGE-CAT1/A/IN-CAT2/U/.3': 'type12', 'AGE-CAT1/R/IN-CAT1/M/-3': 'type13', 'AGE-CAT1/R/IN-CAT1/M/+3': 'type14', 'AGE-CAT1/R/IN-CAT1/M/.3': 'type15', 'AGE-CAT1/R/IN-CAT1/U/-3': 'type16', 'AGE-CAT1/R/IN-CAT1/U/+3': 'type17', 'AGE-CAT1/R/IN-CAT1/U/.3': 'type18', 'AGE-CAT1/R/IN-CAT2/M/-3': 'type19', 'AGE-CAT1/R/IN-CAT2/M/+3': 'type20', 'AGE-CAT1/R/IN-CAT2/M/.3': 'type21', 'AGE-CAT1/R/IN-CAT2/U/-3': 'type22', 'AGE-CAT1/R/IN-CAT2/U/+3': 'type23', 'AGE-CAT1/R/IN-CAT2/U/.3': 'type24', 'AGE-CAT2/A/IN-CAT1/M/-3': 'type25', 'AGE-CAT2/A/IN-CAT1/M/+3': 'type26', 'AGE-CAT2/A/IN-CAT1/M/.3': 'type27', 'AGE-CAT2/A/IN-CAT1/U/-3': 'type28', 'AGE-CAT2/A/IN-CAT1/U/+3': 'type29', 'AGE-CAT2/A/IN-CAT1/U/.3': 'type30', 'AGE-CAT2/A/IN-CAT2/M/-3': 'type31', 'AGE-CAT2/A/IN-CAT2/M/+3': 'type32', 'AGE-CAT2/A/IN-CAT2/M/.3': 'type33', 'AGE-CAT2/A/IN-CAT2/U/-3': 'type34', 'AGE-CAT2/A/IN-CAT2/U/+3': 'type35', 'AGE-CAT2/A/IN-CAT2/U/.3': 'type36', 'AGE-CAT2/R/IN-CAT1/M/-3': 'type37', 'AGE-CAT2/R/IN-CAT1/M/+3': 'type38', 'AGE-CAT2/R/IN-CAT1/M/.3': 'type39', 'AGE-CAT2/R/IN-CAT1/U/-3': 'type40', 'AGE-CAT2/R/IN-CAT1/U/+3': 'type41', 'AGE-CAT2/R/IN-CAT1/U/.3': 'type42', 'AGE-CAT2/R/IN-CAT2/M/-3': 'type43', 'AGE-CAT2/R/IN-CAT2/M/+3': 'type44', 'AGE-CAT2/R/IN-CAT2/M/.3': 'type45', 'AGE-CAT2/R/IN-CAT2/U/-3': 'type46', 'AGE-CAT2/R/IN-CAT2/U/+3': 'type47', 'AGE-CAT2/R/IN-CAT2/U/.3': 'type48', 'AGE-CAT3/A/IN-CAT1/M/-3': 'type49', 'AGE-CAT3/A/IN-CAT1/M/+3': 'type50', 'AGE-CAT3/A/IN-CAT1/M/.3': 'type51', 'AGE-CAT3/A/IN-CAT1/U/-3': 'type52', 'AGE-CAT3/A/IN-CAT1/U/+3': 'type53', 'AGE-CAT3/A/IN-CAT1/U/.3': 'type54', 'AGE-CAT3/A/IN-CAT2/M/-3': 'type55', 'AGE-CAT3/A/IN-CAT2/M/+3': 'type56', 'AGE-CAT3/A/IN-CAT2/M/.3': 'type57', 'AGE-CAT3/A/IN-CAT2/U/-3': 'type58', 'AGE-CAT3/A/IN-CAT2/U/+3': 'type59', 'AGE-CAT3/A/IN-CAT2/U/.3': 'type60', 'AGE-CAT3/R/IN-CAT1/M/-3': 'type61', 'AGE-CAT3/R/IN-CAT1/M/+3': 'type62', 'AGE-CAT3/R/IN-CAT1/M/.3': 'type63', 'AGE-CAT3/R/IN-CAT1/U/-3': 'type64', 'AGE-CAT3/R/IN-CAT1/U/+3': 'type65', 'AGE-CAT3/R/IN-CAT1/U/.3': 'type66', 'AGE-CAT3/R/IN-CAT2/M/-3': 'type67', 'AGE-CAT3/R/IN-CAT2/M/+3': 'type68', 'AGE-CAT3/R/IN-CAT2/M/.3': 'type69', 'AGE-CAT3/R/IN-CAT2/U/-3': 'type70', 'AGE-CAT3/R/IN-CAT2/U/+3': 'type71', 'AGE-CAT3/R/IN-CAT2/U/.3': 'type72', 'AGE-CAT4/A/IN-CAT1/M/-3': 'type73', 'AGE-CAT4/A/IN-CAT1/M/+3': 'type74', 'AGE-CAT4/A/IN-CAT1/M/.3': 'type75', 'AGE-CAT4/A/IN-CAT1/U/-3': 'type76', 'AGE-CAT4/A/IN-CAT1/U/+3': 'type77', 'AGE-CAT4/A/IN-CAT1/U/.3': 'type78', 'AGE-CAT4/A/IN-CAT2/M/-3': 'type79', 'AGE-CAT4/A/IN-CAT2/M/+3': 'type80', 'AGE-CAT4/A/IN-CAT2/M/.3': 'type81', 'AGE-CAT4/A/IN-CAT2/U/-3': 'type82', 'AGE-CAT4/A/IN-CAT2/U/+3': 'type83', 'AGE-CAT4/A/IN-CAT2/U/.3': 'type84', 'AGE-CAT4/R/IN-CAT1/M/-3': 'type85', 'AGE-CAT4/R/IN-CAT1/M/+3': 'type86', 'AGE-CAT4/R/IN-CAT1/M/.3': 'type87', 'AGE-CAT4/R/IN-CAT1/U/-3': 'type88', 'AGE-CAT4/R/IN-CAT1/U/+3': 'type89', 'AGE-CAT4/R/IN-CAT1/U/.3': 'type90', 'AGE-CAT4/R/IN-CAT2/M/-3': 'type91', 'AGE-CAT4/R/IN-CAT2/M/+3': 'type92', 'AGE-CAT4/R/IN-CAT2/M/.3': 'type93', 'AGE-CAT4/R/IN-CAT2/U/-3': 'type94', 'AGE-CAT4/R/IN-CAT2/U/+3': 'type95', 'AGE-CAT4/R/IN-CAT2/U/.3': 'type96'}
# print(mapp[ans])