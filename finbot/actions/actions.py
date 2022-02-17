# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Text, Dict, Any, List
import regex as re
import database
import json
import classify

class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_send_base_carousel"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            print("in the carousel function")
            
            base_carousel ={
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "Hi! I am Sheeba.",
                        "subtitle": "If you are stuck at any place, enter 'Sheeba'. Please choose one of the following.",
                        # "image_url": "https://cdn-icons-png.flaticon.com/512/411/411768.png",
                        "image_url": "https://cdn-icons-png.flaticon.com/512/411/411768.png",
                        "dims": {
                        "width": 200,
                        "height":50
                                },
                        "buttons": [ 
                            {
                                "title": "Health Insurance",
                                "type": "postback",
                                "payload": "/health"
                            },
                            {
                                "title": "Life Insurance",
                                "type": "postback",
                                "payload": "/life"
                            },
                            {
                                "title": "Policy Suggestions",
                                "type": "postback",
                                "payload": "/give_suggestion"
                            }
                            ]
                                }
                    ]
                }
    }

            dispatcher.utter_message(attachment=base_carousel)
            return []



########################################################################################
#Life actions

#   action_life_regexandstore_slots
#   action_life_get_user_data
#   action_life_update_slots
#   action_life_next_action
#   validate_client_life_info_form    

class lifeNextAction(Action):
# Life options carousel: options- show/update details 
    def name(self) -> Text:
        return "action_life_next_action"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("in life next action")
        
        next_action_carousel ={
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "",
                        "subtitle": "Please choose one of the following.",
                        "image_url":"https://cdn.discordapp.com/attachments/842313533185327118/901098797369798666/clicking-finger-icon-hand-click-260nw-1922794949.png",
                        # "image_url": "https://cdn-icons-png.flaticon.com/512/411/411768.png",
                        "dims": {
                        "width": 0, #200 100
                        "height":0
                                },
                        "buttons": [ 
                            {
                                "title": "View details",
                                "type": "postback",
                                "payload": "/show_data_life"
                            },
                            # {
                            #     "title": "give suggestion",
                            #     "type": "postback",
                            #     "payload": "/give_suggestion_life"
                            # },
                            {
                                "title": "Update Details",
                                "type": "postback",
                                "payload": "/update_life"
                            },
                            {
                                "title": "Main Menu",
                                "type": "postback",
                                "payload": "/greet"
                            }
                            ]
                                }
                    ]
                }
            }

        dispatcher.utter_message(attachment=next_action_carousel)
        return []


class ValidateClientlifeInfoForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_client_life_info_form"

  async def required_slots(self,slots_mapped_in_domain: List[Text],dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     
    if tracker.get_slot("confirm_life_data_retreived") == False:  
        return ["age","retirement_age","existing_savings","existing_loan","expected_rate_of_return","existing_insurance_cover","employement_status","annual_income","marital_status","number_of_dependents"]
    else:
        return []

class lifeHelloWorld(Action):
# regex on inputs so as to isolate digits in inputs
# eg- '12000 rupees' to '12000' 
    def name(self) -> Text:
        return "action_life_regexandstore_slots"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_age = re.findall(r"([\d.,]*\d+)", tracker.get_slot("age"))
        new_annual_income = re.findall(r"([\d.,]*\d+)", tracker.get_slot("annual_income"))
        new_number_of_dependents = re.findall(r"([\d.,]*\d+)", tracker.get_slot("number_of_dependents"))
        new_retirement_age = re.findall(r"([\d.,]*\d+)", tracker.get_slot("retirement_age"))
        new_existing_savings = re.findall(r"([\d.,]*\d+)", tracker.get_slot("existing_savings"))
        new_existing_loan = re.findall(r"([\d.,]*\d+)", tracker.get_slot("existing_loan"))
        new_expected_rate_of_return = re.findall(r"([\d.,]*\d+)", tracker.get_slot("expected_rate_of_return"))
        new_existing_insurance_cover = re.findall(r"([\d.,]*\d+)", tracker.get_slot("existing_insurance_cover"))

        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        print(custom_data['userid'])
        #dispatcher.utter_message(text=custom_data['userid'])
        
        data = {
        "name":str(custom_data['name']),
        "age":new_age[0],
        "retirement_age":new_retirement_age[0],
        "existing_savings":new_existing_savings[0],
        "existing_loan":new_existing_loan[0],
        "expected_rate_of_return":new_expected_rate_of_return[0],
        "existing_insurance_cover":new_existing_insurance_cover[0],
        "employement_status":str(tracker.get_slot("employement_status")),
        "annual_income":new_annual_income[0],
        "marital_status":str(tracker.get_slot("marital_status")),
        "number_of_dependents":new_number_of_dependents[0]
        }

        userid = custom_data['userid']
        adb = database.Firebase()
        adb.write_data(userid,data,'life') # firebase class is a helper class

        print("\Data written in regex and store\n")
        return [
            SlotSet("existing_insurance_cover", new_existing_insurance_cover[0]),
            SlotSet("expected_rate_of_return", new_expected_rate_of_return[0]),
            SlotSet("existing_loan", new_existing_loan[0]),
            SlotSet("existing_savings", new_existing_savings[0]),
            SlotSet("retirement_age", new_retirement_age[0]),
            SlotSet("age", new_age[0]),
            SlotSet("annual_income", new_annual_income[0]),
            SlotSet("number_of_dependents", new_number_of_dependents[0])
            ]

class lifeGetData(Action):
# gets data from database and sets slots
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
                print("\n\n data val was none \n\n")# dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False)]
            
            print("\nLife data read\n")
            
            return [
                SlotSet("age", data.val()['age']),
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
                SlotSet("confirm_life_data_retreived",True)
            ]
        except:
            print("\nException in get life data\n")
            data = {}
            return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False)]

        

        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
        
 
class lifeUpdateSlots(Action):
#  Update life form i.e first remove data and thenn trigger form
#  delete here and trigger form in rules/stories 
    def name(self) -> Text:
        return "action_life_update_slots"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        adb = database.Firebase()   # adb is the firebase object used to read data from the firebase realtime database
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        
        adb.remove_data(custom_data["userid"],'life')
        
        return [
            SlotSet("name",custom_data['name']),
            SlotSet("confirm_life_data_retreived",False), 
            SlotSet("age", None), 
            SlotSet("employement_status",None),
            SlotSet("annual_income", None),
            SlotSet("retirement_age", None),
            SlotSet("existing_savings", None),
            SlotSet("existing_loan", None),
            SlotSet("expected_rate_of_return",None),
            SlotSet("existing_insurance_cover", None),
            SlotSet("number_of_dependents", None),
            SlotSet("marital_status", None),
            ]


#####################################################################
#Health actions


# confirm_health_data_retreived 

# action_health_next_action
# validate_client_health_info_form
# action_health_update_slots
# action_health_get_user_data
# action_health_regexandstore_slots

class healthNextAction(Action):
# Health carousel 
# Options- Update/Show details
    def name(self) -> Text:
        return "action_health_next_action"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("\n In life next action\n")
        next_action_carousel ={
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "",
                        "subtitle": "Please choose the next action",
                        # "image_url": "https://cdn-icons-png.flaticon.com/512/411/411768.png",
                        "image_url":"https://cdn.discordapp.com/attachments/842313533185327118/901098797369798666/clicking-finger-icon-hand-click-260nw-1922794949.png",
                        "dims": {
                        "width": 0,
                        "height":0 #200 100
                                },
                        "buttons": [ 
                            {
                                "title": "View Details",
                                "type": "postback",
                                "payload": "/show_data_health"
                            },
                            # {
                            #     "title": "give suggestion",
                            #     "type": "postback",
                            #     "payload": "/give_suggestion_health"
                            # },
                            {
                                "title": "Update Details",
                                "type": "postback",
                                "payload": "/update_health"
                            },
                            {
                                "title": "Main Menu",
                                "type": "postback",
                                "payload": "/greet"
                            }
                            ]
                                }
                    ]
                }
            }

        dispatcher.utter_message(attachment=next_action_carousel)
        return []




class ValidateClienthealthInfoForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_client_health_info_form"

  async def required_slots(self,slots_mapped_in_domain: List[Text],dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    if tracker.get_slot("confirm_health_data_retreived") == False:  
        return ["zip_code","disease_history","present_major_illness","present_major_treatment","tobacco_consumption"]
    else:
        return []



class healthRegexAndStore(Action):

    def name(self) -> Text:
        return "action_health_regexandstore_slots"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        userid = custom_data['userid']
        # print(custom_data['userid']) 
        #dispatcher.utter_message(text=custom_data['userid'])

        zip_code = re.findall(r"([\d.,]*\d+)", tracker.get_slot("zip_code"))
        
        data = {
            "name":str(custom_data['name']),
            "zip_code":zip_code[0],
            "disease_history":tracker.get_slot('disease_history'),
            "present_major_illness":tracker.get_slot('present_major_illness'),
            "present_major_treatment":tracker.get_slot('present_major_treatment'),
            "tobacco_consumption":tracker.get_slot('tobacco_consumption')
        }

        
        
        adb = database.Firebase()
        adb.write_data(userid,data,'health')
        print("\nHealth regex data and store\n")

        return [SlotSet("zip_code", zip_code[0])]


class healthUpdateSlots(Action):

    def name(self) -> Text:
        return "action_health_update_slots"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        adb = database.Firebase()   # adb is the firebase object used to read data from the firebase realtime database
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        
        adb.remove_data(custom_data["userid"],'health')
        
        return [
            SlotSet("name",custom_data['name']),
            SlotSet("confirm_health_data_retreived",False), 
            SlotSet("zip_code", None),
            SlotSet("disease_history", None),
            SlotSet("tobacco_consumption", None),
            SlotSet("present_major_illness", None),
            SlotSet("present_major_treatment", None), 
            ]
 


class healthGetData(Action):
    def name(self) -> Text:
        return "action_health_get_user_data"
        # zip_code
        # disease_history:      
        # present_major_illness:
        # present_major_treatment:
        # tobacco_consumption:  
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
                print("\n\n data val was none \n\n") # dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False)]
            
            print("\nRead health data\n")
            
            return [
            SlotSet("name",name),
            SlotSet("zip_code", data.val()['zip_code']),
            SlotSet("disease_history", data.val()['disease_history']),
            SlotSet("tobacco_consumption", data.val()['tobacco_consumption']),
            SlotSet("present_major_illness", data.val()['present_major_illness']),
            SlotSet("present_major_treatment", data.val()['present_major_treatment']),
            SlotSet("confirm_health_data_retreived",True)
            ]
        except:
            print("\nIn except health read\n")
            data = {}
            return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False)]

        

        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
        

###############################################
#suggestion actions




# story/ rule - These three go back to back
# actions
# action_life_pred_get_user_data
# action_health_pred_get_user_data
# action_utter_policy_suggestion

# intent
# give suggestion

# slots 
# life_suggestion
# health_suggestion

class lifeGetData(Action):
    def name(self) -> Text:
        return "action_life_pred_get_user_data"

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
                print("\nData val was none in life pred\n") # dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False),SlotSet("life_suggestion","")]
            
            print("\n Read data successfully life pred\n")
            data=data.val()
            # print(data) # change
            
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
            # calls the classify class
            
            pure_risk = round(hlvTemp[1][0]*hlvScore/100,2)
            investment = round(hlvTemp[1][1]*hlvScore/100,2)
             
            message = "We suggest you to get assured with following amount for respective needs,\n- Pure risk: "+str(pure_risk)+"\n- Investments: "+str(investment)
             
            return [
                SlotSet("age", data['age']),
                SlotSet("name",name),
                SlotSet("employement_status", data['employement_status']),
                SlotSet("annual_income", data['annual_income']),
                SlotSet("retirement_age", data['retirement_age']),
                SlotSet("existing_savings", data['existing_savings']),
                SlotSet("existing_loan", data['existing_loan']),
                SlotSet("expected_rate_of_return", data['expected_rate_of_return']),
                SlotSet("existing_insurance_cover", data['existing_insurance_cover']),
                SlotSet("number_of_dependents", data['number_of_dependents']),
                SlotSet("marital_status", data['marital_status']),
                SlotSet("confirm_life_data_retreived",True),
                SlotSet("hvlScore", str(hlvScore)),
                SlotSet("hvlCategory",hlvTemp[0]),
                SlotSet("life_suggestion",message)
                ]
        except:
            print("\nExcept in life pred data\n")
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
        return "action_health_pred_get_user_data"
        
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
                print("\n\n data val was none in health pred \n\n")    # dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False),SlotSet("health_suggestion","")]
            
            print("\nRead data action pred\n")
            message="We have done your health analysis."
            # Since there are no classification rules for the health case at the moment, We set this as the recommendation message
            
            # message = "We would sugest you to buy the health cover availible on this link http://127.0.0.1:8000/buy-portal/"
            # dispatcher.utter_message(text = tracker.get_slot("suggestion")) suggestion-message
            # dispatcher.utter_message(text = tracker.get_slot("suggestion")) 
            
            return [
                SlotSet("health_suggestion",message),
                SlotSet("name",name),
                SlotSet("zip_code", data.val()['zip_code']),
                SlotSet("disease_history", data.val()['disease_history']),
                SlotSet("tobacco_consumption", data.val()['tobacco_consumption']),
                SlotSet("present_major_illness", data.val()['present_major_illness']),
                SlotSet("present_major_treatment", data.val()['present_major_treatment']),
                SlotSet("confirm_health_data_retreived",True)
                ]
        except:
            print("\n\nin except health pred data\n\n")
            data = {}
            # return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False),SlotSet("suggestion","")]
            return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False),SlotSet("health_suggestion","")]
            
 
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
