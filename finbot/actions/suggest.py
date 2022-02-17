# Added to actions file 


# Suggestions rules
# story/ rule - These three go back to back
# actions
# action_life_get_user_data
# action_health_get_user_data
# action_utter_policy_suggestion

# intent
# give suggestion

# slots 
# life_suggestion
# health_suggestion

class lifeGetData(Action):
    def name(self) -> Text:
        return "action_life_get_user_data"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text = "inside get user data")
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        name = custom_data['name']
        
        try:
            userid = custom_data['userid']
            adb = database.Firebase()   # adb is the firebase object used to read data from the firebase realtime database
            data = adb.read_data(userid,'life')
            if data.val() is None:
                print("\n\n data val was none \n\n") # dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False),SlotSet("life_suggestion","")]
            print("\n\n read data successfully \n\n")
            
            # change
            income = data['annual_income']
            income = income.replace(",","")
            income = float(income)
            increment = float(data['expected_rate_of_return'])/100
            retirement_age = data['retirement_age']
            retirement_age = retirement_age.replace(",","")
            retirement_age = float(retirement_age) 
            age = data['age']
            age = age.replace(",","")
            age = float(age)
            annual_expense = 0.3*income

            hlvScore=(income*(pow((1+increment),(retirement_age-age))-1) /increment) - (annual_expense*(pow((1+increment),(retirement_age-age))-1) / increment)
            hlvScore=round(hlvScore,2)
            hlvTemp = classify.my_classifier(data)
            pure_risk = round(hlvTemp[1][0]*hlvScore/100,2)
            investment = round(hlvTemp[1][1]*hlvScore/100,2)
            message = "We suggest you to get assured with following amount for respective needs,\n- Pure risk: "+str(pure_risk)+"\n- Investments: "+str(investment)
            # +"\n- Get yourself insured for these needs by clicking following link http://127.0.0.1:8000/buy-portal/"
            # change
            return [SlotSet("age", data.val()['age']),
            SlotSet("name",name),
            SlotSet("employement_status", data.val()['employement_status']),
            SlotSet("annual_income", data.val()['annual_income']),
            SlotSet("retirement_age", data.val()['retirement_age']),
            SlotSet("existing_savings", data.val()['existing_savings']),
            SlotSet("existing_loan", data.val()['existing_loan']),
            SlotSet("expected_rate_of_return", data.val()['expected_rate_of_return']),
            SlotSet("existing_insurance_cover", data.val()['existing_insurance_cover']),
            SlotSet("number_of_dependents", data.val()['number_of_dependents']),
            SlotSet("marital_status", data.val()['marital_status']),
            SlotSet("confirm_data_retreived",True),
            SlotSet("hvlScore", str(hlvScore)),
            SlotSet("hvlCategory",hlvTemp[0]),
            SlotSet("life_suggestion",message)]
        except:
            print("\n\nin except\n\n")
            data = {}
            # utter there was a problem 
            return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False),SlotSet("life_suggestion","")]

        

        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
        
 

 

        # zip_code
        # disease_history:      
        # present_major_illness:
        # present_major_treatment:
        # tobacco_consumption:  


 

class healthGetData(Action):
    def name(self) -> Text:
        return "action_health_get_user_data"
        
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text = "inside get user data")
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        name = custom_data['name']
        try:
            userid = custom_data['userid']
            adb = database.Firebase()   # adb is the firebase object used to read data from the firebase realtime database
            data = adb.read_data(userid,'health')
            
            if data.val() is None:
                print("\n\n data val was none \n\n")# dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_data_retreived",False),SlotSet("health_suggestion","")]
            
            print("\n\n read data successfully \n\n")
            message="We have done your health analysis."
            # message = "We would sugest you to buy the health cover availible on this link http://127.0.0.1:8000/buy-portal/"
            # change the line above

            # dispatcher.utter_message(text = tracker.get_slot("suggestion")) suggestion-message
            # dispatcher.utter_message(text = tracker.get_slot("suggestion")) 
            return [SlotSet("health_suggestion",message),
            SlotSet("name",name),
            SlotSet("zip_code", data.val()['zip_code']),
            SlotSet("disease_history", data.val()['disease_history']),
            SlotSet("tobacco_consumption", data.val()['tobacco_consumption']),
            SlotSet("present_major_illness", data.val()['present_major_illness']),
            SlotSet("present_major_treatment", data.val()['present_major_treatment']),
            SlotSet("confirm_data_retreived",True)]
        except:
            print("\n\nin except\n\n")
            data = {}
            # return [SlotSet("name",name),SlotSet("confirm_data_retreived",False),SlotSet("suggestion","")]
            return [SlotSet("name",name),SlotSet("confirm_data_retreived",False),SlotSet("health_suggestion","")]
            
 
        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
   
 

class PolicySuggestion(Action):

    def name(self) -> Text:
        return "action_utter_policy_suggestion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("in suggest policy function")

        life_suggestion=str(tracker.get_slot("life_suggestion"))
        health_suggestion=str(tracker.get_slot("health_suggestion"))
        link="Please go to this link to buy policies http://127.0.0.1:8000/buy-portal/" 

        if life_suggestion is not "" and health_suggestion is not "":
            dispatcher.utter_message(text = tracker.get_slot("life_suggestion"))
            dispatcher.utter_message(text = tracker.get_slot("health_suggestion"))
            dispatcher.utter_message(text = link)        
        elif life_suggestion is not "":
            dispatcher.utter_message(text = tracker.get_slot("life_suggestion"))
            dispatcher.utter_message(text = link)   
        elif health_suggestion is not "":
            dispatcher.utter_message(text = tracker.get_slot("health_suggestion"))
            dispatcher.utter_message(text = link)   
        else:
            no_suggestion="Please go to the health or life insurance analysis first."
            dispatcher.utter_message(text = no_suggestion)   
             
        print("out of suggest policy")
        return []
