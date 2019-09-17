# Action => Utter Existing Template or Custom Message
# dispatcher.utter_template("action_fetch_entitlement", tracker)
# dispatcher.utter_message("We")

# Can fill Slots in between
# SlotSet("Key", [Value])

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormAction
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

class ActionFetchEntitlement(Action):
    def name(self) -> Text:
        return "action_fetch_entitlement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You have 5 days of entitlement left.")
        return []

class ActionFetchHolidaysInformation(Action):
    def name(self) -> Text:
        return "action_fetch_holidays_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("We have 3 Holidays coming up Veterans Day on Nov 11 th , Thanksgiving on Nov 28 th , Christmas day on Dec 25 th.")
        return []

class ActionApplyALeave(Action):
    def name(self) -> Text:
        return "action_apply_a_leave"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("We have 3 Holidays coming up Veterans Day on Nov 11 th , Thanksgiving on Nov 28 th , Christmas day on Dec 25 th.")
        return []

class ActionUtterLeaveConfirmationMessage(Action):
    def name(self) -> Text:
        return "action_utter_leave_confirmation_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("We have 3 Holidays coming up Veterans Day on Nov 11 th , Thanksgiving on Nov 28 th , Christmas day on Dec 25 th.")
        return []

class ActionUtterLeaveConfirmedMessage(Action):
    def name(self) -> Text:
        return "action_utter_leave_confirmed_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("We have 3 Holidays coming up Veterans Day on Nov 11 th , Thanksgiving on Nov 28 th , Christmas day on Dec 25 th.")
        return []

class FallbackAction(Action):
    def name(self) -> Text:
        return "fallback_action"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        from rasa_core.events import UserUtteranceReverted
        dispatcher.utter_message("Sorry, didn't get that. Try again.")
        return [UserUtteranceReverted()]

class ApplyLeaveForm(FormAction):
    def name(self):
        return "apply_leave_form"
    
    @staticmethod
    def required_slots(tracker):
        return ["slot1", "slot2"]
    
    def submit(self, dispatcher, tracker, domain):
        # dispatcher.utter_template('utter_submitted', tracker)
        # dispatcher.utter_template('utter_please_wait', tracker)
        return []

class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()]

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]