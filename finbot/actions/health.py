# Redundant code as added to the actions file



# Health actions 
# confirm_health_data_retreived 

# action_health_next_action
# validate_client_health_info_form
# action_health_update_slots
# action_health_get_user_data
# action_health_regexandstore_slots

class healthNextAction(Action):

    def name(self) -> Text:
        return "action_health_next_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("in life next action")
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
        print(custom_data['userid']) #dispatcher.utter_message(text=custom_data['userid'])
        
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
        return [SlotSet("name",custom_data['name']),SlotSet("confirm_health_data_retreived",False)]


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
                print("\n\n data val was none \n\n") # dispatcher.utter_message(text = "new user")
                return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False)]
            print("\n\n read data successfully \n\n")
            
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
            print("\n\nin except\n\n")
            data = {}
            return [SlotSet("name",name),SlotSet("confirm_health_data_retreived",False)]

        

        # print(data.val())
        #dispatcher.utter_message(text = "user data retrieved")    
        
