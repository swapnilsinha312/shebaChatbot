age_ls = ["AGE-CAT1","AGE-CAT2","AGE-CAT3","AGE-CAT4"]
employed_ls = ["A","R"]
income_ls = ["IN-CAT1","IN-CAT2","IN-CAT3","IN-CAT4"]
married_ls = ["M","U"]
dependents_ls = ['-3','+3','.3']

count=1

final_list = []
type_list = []
for age in age_ls:
    for employed in employed_ls:
        for income in income_ls:
            for married in married_ls:
                for dependents in dependents_ls:
                    temp_str = age+"/"+employed+"/"+income+"/"+married+"/"+dependents
                    type_str = "type"+str(count)
                    count+=1
                    type_list.append(type_str)
                    final_list.append(temp_str)

print("AGE-CAT3/R/IN-CAT2/M/.3" in final_list)
print(type_list)

zip_obj = zip(final_list,type_list)
mappp = dict(zip_obj)

print(mappp)

"""
mappp=
{'AGE-CAT1/A/IN-CAT1/M/-3': 'type1', 'AGE-CAT1/A/IN-CAT1/M/+3': 'type2', 'AGE-CAT1/A/IN-CAT1/M/.3': 'type3', 'AGE-CAT1/A/IN-CAT1/U/-3': 'type4', 'AGE-CAT1/A/IN-CAT1/U/+3': 'type5', 'AGE-CAT1/A/IN-CAT1/U/.3': 'type6', 'AGE-CAT1/A/IN-CAT2/M/-3': 'type7', 'AGE-CAT1/A/IN-CAT2/M/+3': 'type8', 'AGE-CAT1/A/IN-CAT2/M/.3': 'type9', 'AGE-CAT1/A/IN-CAT2/U/-3': 'type10', 'AGE-CAT1/A/IN-CAT2/U/+3': 'type11', 'AGE-CAT1/A/IN-CAT2/U/.3': 'type12', 'AGE-CAT1/R/IN-CAT1/M/-3': 'type13', 'AGE-CAT1/R/IN-CAT1/M/+3': 'type14', 'AGE-CAT1/R/IN-CAT1/M/.3': 'type15', 'AGE-CAT1/R/IN-CAT1/U/-3': 'type16', 'AGE-CAT1/R/IN-CAT1/U/+3': 'type17', 'AGE-CAT1/R/IN-CAT1/U/.3': 'type18', 'AGE-CAT1/R/IN-CAT2/M/-3': 'type19', 'AGE-CAT1/R/IN-CAT2/M/+3': 'type20', 'AGE-CAT1/R/IN-CAT2/M/.3': 'type21', 'AGE-CAT1/R/IN-CAT2/U/-3': 'type22', 'AGE-CAT1/R/IN-CAT2/U/+3': 'type23', 'AGE-CAT1/R/IN-CAT2/U/.3': 'type24', 'AGE-CAT2/A/IN-CAT1/M/-3': 'type25', 'AGE-CAT2/A/IN-CAT1/M/+3': 'type26', 'AGE-CAT2/A/IN-CAT1/M/.3': 'type27', 'AGE-CAT2/A/IN-CAT1/U/-3': 'type28', 'AGE-CAT2/A/IN-CAT1/U/+3': 'type29', 'AGE-CAT2/A/IN-CAT1/U/.3': 'type30', 'AGE-CAT2/A/IN-CAT2/M/-3': 'type31', 'AGE-CAT2/A/IN-CAT2/M/+3': 'type32', 'AGE-CAT2/A/IN-CAT2/M/.3': 'type33', 'AGE-CAT2/A/IN-CAT2/U/-3': 'type34', 'AGE-CAT2/A/IN-CAT2/U/+3': 'type35', 'AGE-CAT2/A/IN-CAT2/U/.3': 'type36', 'AGE-CAT2/R/IN-CAT1/M/-3': 'type37', 'AGE-CAT2/R/IN-CAT1/M/+3': 'type38', 'AGE-CAT2/R/IN-CAT1/M/.3': 'type39', 'AGE-CAT2/R/IN-CAT1/U/-3': 'type40', 'AGE-CAT2/R/IN-CAT1/U/+3': 'type41', 'AGE-CAT2/R/IN-CAT1/U/.3': 'type42', 'AGE-CAT2/R/IN-CAT2/M/-3': 'type43', 'AGE-CAT2/R/IN-CAT2/M/+3': 'type44', 'AGE-CAT2/R/IN-CAT2/M/.3': 'type45', 'AGE-CAT2/R/IN-CAT2/U/-3': 'type46', 'AGE-CAT2/R/IN-CAT2/U/+3': 'type47', 'AGE-CAT2/R/IN-CAT2/U/.3': 'type48', 'AGE-CAT3/A/IN-CAT1/M/-3': 'type49', 'AGE-CAT3/A/IN-CAT1/M/+3': 'type50', 'AGE-CAT3/A/IN-CAT1/M/.3': 'type51', 'AGE-CAT3/A/IN-CAT1/U/-3': 'type52', 'AGE-CAT3/A/IN-CAT1/U/+3': 'type53', 'AGE-CAT3/A/IN-CAT1/U/.3': 'type54', 'AGE-CAT3/A/IN-CAT2/M/-3': 'type55', 'AGE-CAT3/A/IN-CAT2/M/+3': 'type56', 'AGE-CAT3/A/IN-CAT2/M/.3': 'type57', 'AGE-CAT3/A/IN-CAT2/U/-3': 'type58', 'AGE-CAT3/A/IN-CAT2/U/+3': 'type59', 'AGE-CAT3/A/IN-CAT2/U/.3': 'type60', 'AGE-CAT3/R/IN-CAT1/M/-3': 'type61', 'AGE-CAT3/R/IN-CAT1/M/+3': 'type62', 'AGE-CAT3/R/IN-CAT1/M/.3': 'type63', 'AGE-CAT3/R/IN-CAT1/U/-3': 'type64', 'AGE-CAT3/R/IN-CAT1/U/+3': 'type65', 'AGE-CAT3/R/IN-CAT1/U/.3': 'type66', 'AGE-CAT3/R/IN-CAT2/M/-3': 'type67', 'AGE-CAT3/R/IN-CAT2/M/+3': 'type68', 'AGE-CAT3/R/IN-CAT2/M/.3': 'type69', 'AGE-CAT3/R/IN-CAT2/U/-3': 'type70', 'AGE-CAT3/R/IN-CAT2/U/+3': 'type71', 'AGE-CAT3/R/IN-CAT2/U/.3': 'type72', 'AGE-CAT4/A/IN-CAT1/M/-3': 'type73', 'AGE-CAT4/A/IN-CAT1/M/+3': 'type74', 'AGE-CAT4/A/IN-CAT1/M/.3': 'type75', 'AGE-CAT4/A/IN-CAT1/U/-3': 'type76', 'AGE-CAT4/A/IN-CAT1/U/+3': 'type77', 'AGE-CAT4/A/IN-CAT1/U/.3': 'type78', 'AGE-CAT4/A/IN-CAT2/M/-3': 'type79', 'AGE-CAT4/A/IN-CAT2/M/+3': 'type80', 'AGE-CAT4/A/IN-CAT2/M/.3': 'type81', 'AGE-CAT4/A/IN-CAT2/U/-3': 'type82', 'AGE-CAT4/A/IN-CAT2/U/+3': 'type83', 'AGE-CAT4/A/IN-CAT2/U/.3': 'type84', 'AGE-CAT4/R/IN-CAT1/M/-3': 'type85', 'AGE-CAT4/R/IN-CAT1/M/+3': 'type86', 'AGE-CAT4/R/IN-CAT1/M/.3': 'type87', 'AGE-CAT4/R/IN-CAT1/U/-3': 'type88', 'AGE-CAT4/R/IN-CAT1/U/+3': 'type89', 'AGE-CAT4/R/IN-CAT1/U/.3': 'type90', 'AGE-CAT4/R/IN-CAT2/M/-3': 'type91', 'AGE-CAT4/R/IN-CAT2/M/+3': 'type92', 'AGE-CAT4/R/IN-CAT2/M/.3': 'type93', 'AGE-CAT4/R/IN-CAT2/U/-3': 'type94', 'AGE-CAT4/R/IN-CAT2/U/+3': 'type95', 'AGE-CAT4/R/IN-CAT2/U/.3': 'type96'}

percentage mapping
{'1':[100,0],'2':[80,20],'3':[60,40],'4':[40,60],
'5':[100,0],'6':[90,10],'7':[70,30],'8':[50,50],
'9':[100,0],'10':[90,10],'11':[70,30],'12':[60,40],
'13':[30,70],'14':[20,80],'15':[10,90],'16':[10,90]}
"""