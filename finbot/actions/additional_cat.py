# This was used to make the different classifications for the life case in accordance with the life rules



age_ls = ["AGE-CAT1","AGE-CAT2","AGE-CAT3","AGE-CAT4"]
employed_ls = ["A","R"]
income_ls = ["IN-CAT1","IN-CAT2","IN-CAT3","IN-CAT4"]
married_ls = ["M","U"]
dependents_ls = ['-3','+3','.3']

final_list = []
cat_list = []
for age in age_ls:
    for employed in employed_ls:
        for income in income_ls:
            for married in married_ls:
                for dependents in dependents_ls:
                    temp_str = age+"/"+employed+"/"+income+"/"+married+"/"+dependents
                    final_list.append(temp_str)

for ans in final_list:
    res=''
    if(ans.find("AGE-CAT1")!=-1):
        if(ans.find("IN-CAT1")!=-1):
            res = res+"1"
        elif(ans.find('IN-CAT2')!=-1):
            res = res+'2'
        elif(ans.find('IN-CAT3')!=-1):
            res = res+'3'
        elif(ans.find('IN-CAT4')!=-1):
            res = res+'4'
    elif(ans.find("AGE-CAT2")!=-1):
        if(ans.find("IN-CAT1")!=-1):
            res = res+"5"
        elif(ans.find('IN-CAT2')!=-1):
            res = res+'6'
        elif(ans.find('IN-CAT3')!=-1):
            res = res+'7'
        elif(ans.find('IN-CAT4')!=-1):
            res = res+'8'
    elif(ans.find("AGE-CAT3")!=-1):
        if(ans.find("IN-CAT1")!=-1):
            res = res+"9"
        elif(ans.find('IN-CAT2')!=-1):
            res = res+'10'
        elif(ans.find('IN-CAT3')!=-1):
            res = res+'11'
        elif(ans.find('IN-CAT4')!=-1):
            res = res+'12'
    elif(ans.find("AGE-CAT4")!=-1):
        if(ans.find("IN-CAT1")!=-1):
            res = res+"13"
        elif(ans.find('IN-CAT2')!=-1):
            res = res+'14'
        elif(ans.find('IN-CAT3')!=-1):
            res = res+'15'
        elif(ans.find('IN-CAT4')!=-1):
            res = res+'16'
    cat_list.append(res)
print(dict(zip(final_list,cat_list)))

            # if income<=30473.97:
            #     result.append("IN-CAT1")                        #third
            #     if martial_status == "Married":
            #         result.append("M")                          #fourth
            #         if no_of_depedents<3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
            #         else:
            #             result.append("+3")
            #     else:
            #         result.append("U")
            #         if no_of_depedents < 3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")
            #         else:
            #             result.append("+3")
            # elif income > 30473.97 and income<=53266.42:
            #     result.append("IN-CAT2")                        #third
            #     if martial_status == "Married":
            #         result.append("M")                          #fourth
            #         if no_of_depedents<3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
            #         else:
            #             result.append("+3")
            #     else:
            #         result.append("U")
            #         if no_of_depedents < 3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")
            #         else:
            #             result.append("+3")
            # elif income >53266.42 and income<=91856.06:
            #     result.append("IN-CAT3")                        #third
            #     if martial_status == "Married":
            #         result.append("M")                          #fourth
            #         if no_of_depedents<3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")                        #and finally the number of dependents makes for the fifth categorization
            #         else:
            #             result.append("+3")
            #     else:
            #         result.append("U")
            #         if no_of_depedents < 3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")
            #         else:
            #             result.append("+3")
            # elif income >91856.06:
            #     result.append("IN-CAT4")
            #     if martial_status == "Married":
            #         result.append("M")
            #         if no_of_depedents<3:
            #             result.append("-3")
            #         elif no_of_depedents == 3:
            #             result.append(".3")
            #         else:
            #             result.append("+3")
            #     else:
            #         result.append("U")
            #         if no_of_depedents<3:
            #                 result.append("-3")
            #         elif no_of_depedents == 3:
            #                 result.append(".3")
            #         else:
            #             result.append("+3")