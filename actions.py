# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


#   fetch_entitlement:
#   - text: You have 5 days of entitlement left.
#   - text: 5 days of entitlement is remaining.
#   fetch_entitlement_expiring:
#   - text: Still you have 5 days more.
#   - text: You are left with 5 days.

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionFetchEntitlement(Action):

    def name(self) -> Text:
        return "action_fetch_entitlement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Action Registration
        dispatcher.utter_template("action_fetch_entitlement", tracker)

        # Can fill Slots in between
        # SlotSet("Key", [Value])
        
        # Action Resulting Message
        dispatcher.utter_message("You have 5 days of entitlement left.")
        return []

class FallbackAction(Action):

    def name(self) -> Text:
        return "fallback_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        from rasa_core.events import UserUtteranceReverted
        # Action Registration
        dispatcher.utter_template("fallback_action", tracker)

        # Can fill Slots in between
        # SlotSet("Key", [Value])
        
        # Action Resulting Message
        dispatcher.utter_message("Sorry, didn't get that. Try again.")
        return [UserUtteranceReverted()]