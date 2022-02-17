# Added to actions 



# zip_code
# disease_history:      
# present_major_illness:
# present_major_treatment:
# tobacco_consumption:
class ValidateClienthealthInfoForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_client_health_info_form"

  async def required_slots(
    self,
    slots_mapped_in_domain: List[Text],
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    # if tracker.get_slot("health_or_life_ins") == True:
    #     return ["health1","health2"]
    # else:
    if tracker.get_slot("confirm_data_retreived") == False:  
        return ["zip_code","disease_history","present_major_illness","present_major_treatment","tobacco_consumption"]
    else:
        return []

class healthRegexAndStore(Action):

    def name(self) -> Text:
        return "action_health_regexandstore_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        zip_code = re.findall(r"([\d.,]*\d+)", tracker.get_slot("zip_code"))

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
            "zip_code":zip_code[0],
            "disease_history":tracker.get_slot('disease_history'),
            "present_major_illness":tracker.get_slot('present_major_illness'),
            "present_major_treatment":tracker.get_slot('present_major_treatment'),
            "tobacco_consumption":tracker.get_slot('tobacco_consumption')
        }
        userid = custom_data['userid']
        adb = database.Firebase()
        adb.write_data(userid,data,'health')
        print("\n\n wrote data \n\n")
        return [SlotSet("zip_code", zip_code[0])]

class healthGetData(Action):
    def name(self) -> Text:
        return "action_health_get_user_data"
        # zip_code
        # disease_history:      
        # present_major_illness:
        # present_major_treatment:
        # tobacco_consumption:  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
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
                print("\n\n data val was none \n\n")
                dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_data_retreived",False)]
            print("\n\n read data successfully \n\n")
            return [
            SlotSet("name",name),
            SlotSet("zip_code", data.val()['zip_code']),
            SlotSet("disease_history", data.val()['disease_history']),
            SlotSet("present_major_illness", data.val()['present_major_illness']),
            SlotSet("present_major_treatment", data.val()['present_major_treatment']),
            SlotSet("confirm_data_retreived",True)]
        except:
            print("\n\nin except\n\n")
            data = {}
            return [SlotSet("name",name),SlotSet("confirm_data_retreived",False)]

        

        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
        
        
class healthCalcCover(Action):
    def name(self) -> Text:
        return "action_health_calc_suggest_hvl"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         hvl = []
        #hvlMap={"0":"Unemployed Kid", "1":"LowIncome LowAge","2":"HighIncome LowAge","3":"LowIncome HighAge","4":"HighIncome HighAge"}
        
        message = "this is a health related suggestion"
        return [SlotSet("suggestion",message)] 

class healthUpdateSlots(Action):

    def name(self) -> Text:
        return "action_health_update_slots"

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
        adb.remove_data(custom_data["userid"],'health')
        return [SlotSet("name",custom_data['name']),SlotSet("confirm_data_retreived",False)]


class healthPolicySuggestion(Action):

    def name(self) -> Text:
        return "action_health_utter_policy_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("in suggest policy function")
        #dispatcher.utter_message(text = tracker.get_slot("Type_pred"))
        dispatcher.utter_message(text = tracker.get_slot("suggestion"))
        print("out of suggest policy")
        return []