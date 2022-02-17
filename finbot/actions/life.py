# Added to actions
# Life actions 

#   action_life_regexandstore_slots
#   action_life_get_user_data
#   action_life_update_slots
#   action_life_next_action
#   validate_client_life_info_form    

class lifeNextAction(Action):

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
                        "subtitle": "choose the case you want to go forward with",
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

    def name(self) -> Text:
        return "action_life_regexandstore_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
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
        "number_of_dependents":new_number_of_dependents[0]}
        userid = custom_data['userid']
        adb = database.Firebase()
        adb.write_data(userid,data,'life')
        print("\n\n wrote data \n\n")
        return [SlotSet("existing_insurance_cover", new_existing_insurance_cover[0]),
        SlotSet("expected_rate_of_return", new_expected_rate_of_return[0]),SlotSet("existing_loan", new_existing_loan[0]),
        SlotSet("existing_savings", new_existing_savings[0]),SlotSet("retirement_age", new_retirement_age[0]),
        SlotSet("age", new_age[0]),SlotSet("annual_income", new_annual_income[0]),
        SlotSet("number_of_dependents", new_number_of_dependents[0])]

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
                print("\n\n data val was none \n\n")# dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False)]
            
            print("\n\n read data successfully \n\n")
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
            SlotSet("confirm_life_data_retreived",True)]
        except:
            print("\n\nin except\n\n")
            data = {}
            return [SlotSet("name",name),SlotSet("confirm_life_data_retreived",False)]

        

        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
        
 
class lifeUpdateSlots(Action):

    def name(self) -> Text:
        return "action_life_update_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        adb = database.Firebase()   # adb is the firebase object used to read data from the firebase realtime database
        events = tracker.current_state()['events']
        user_events = []
        for e in events:
            if e['event'] == 'user':
                user_events.append(e)
        custom_data = user_events[-1]['metadata']
        adb.remove_data(custom_data["userid"],'life')
        
        return [SlotSet("name",custom_data['name']),
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
