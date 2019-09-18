# Action => Utter Existing Template or Custom Message
# dispatcher.utter_template("action_fetch_entitlement", tracker)
# dispatcher.utter_message("We")

# Can fill Slots in between
# SlotSet("Key", [Value])

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from db import data
from datetime import datetime
from collections import namedtuple

DateRange = namedtuple('DateRange', ['start', 'end'])

# class ActionUtterProvideTheEmployeeID(Action):
#     def name(self) -> Text:
#         return "utter_ask_reference"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         emp_id = tracker.get_slot('reference')
#         #   utter_provide_the_employee_id:
#         messages = ['Can I have your Employee ID', 'Please provide your Employee ID', 'Enter your Employee ID']
#         if emp_id is None:
#             import random
#             dispatcher.utter_message(random.choice(messages))
#         return []


class ActionValidateEmployeeID(Action):
    def name(self) -> Text:
        return "action_validate_employee_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        emp_id = tracker.get_slot('reference')
        print('emp_id -> action_validate_employee_id -> ', emp_id)
        if emp_id is not None:
            return [SlotSet('is_valid_reference', emp_id in  map(lambda name: name.lower(), data))]
        return []

class ActionValidateLeaveType(Action):
    def name(self) -> Text:
        return "action_validate_leave_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        emp_id = tracker.get_slot('reference')
        print('emp_id -> action_validate_leave_type -> ', emp_id)
        if emp_id is not None:
            leave_type = tracker.get_slot('leave_type')
            valid_leave_type = leave_type in map(lambda a: a["name"].lower(), data[emp_id]["leave_information"]["enrolments"])
            return [SlotSet('is_valid_leave_type', valid_leave_type)]
        return []

class ActionValidateLeaveDateRange(Action): # Check for Overlapping Leaves
    def name(self) -> Text:
        return "action_validate_leave_date_range"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        emp_id = tracker.get_slot('reference')
        if emp_id is not None:
            start_date = tracker.get_slot('time')['from']
            end_date = tracker.get_slot('time')['to']
            apply_range = DateRange(start=datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S'), end=datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S'))
            for r in data[emp_id]["leave_information"]["leaves"]:
                db_range = DateRange(start=datetime.strptime(r["start_date"], '%d/%m/%Y'), end=datetime.strptime(r["end_date"], '%d/%m/%Y'))
                latest_start = max(apply_range.start, db_range.start)
                earliest_end = min(apply_range.end, db_range.end)
                delta = (earliest_end - latest_start).days + 1
                overlap = max(0, delta)
                return [SlotSet('is_valid_date_range', overlap == 0)]
        return []

class ApplyLeaveForm(FormAction):
    def name(self):
        return "apply_leave_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "reference",
            "leave_type",
            "start_datetime",
            "end_datetime"
        ]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "reference": [
                self.from_entity(entity="reference", intent="saying_employee_id")
            ],
            "leave_type": [
                self.from_entity(entity="leave_type", intent="saying_leave_type"),
                # self.from_text(intent="saying_leave_type"),
            ],
            "start_datetime": [
                self.from_entity(entity="start_datetime", intent="apply_leave"),
                self.from_entity(entity="start_datetime", intent="saying_leave_date_range"),
                # self.from_entity(entity="time", intent="apply_leave"), # duckling dimension
                # self.from_entity(entity="time", intent="saying_leave_date_range"),
                # self.from_text(intent="apply_leave"),
            ],
            "end_datetime": [
                self.from_entity(entity="end_datetime", intent="apply_leave"),
                self.from_entity(entity="end_datetime", intent="saying_leave_date_range"),
                # self.from_entity(entity="time", intent="apply_leave"), # duckling dimension
                # self.from_entity(entity="time", intent="saying_leave_date_range"),
                # self.from_text(intent="apply_leave"),
            ]
        }

    def validate_start_datetime(self, value, dispatcher, tracker, domain):
        """Check to see if an time entity was actually picked up by duckling."""
        time = tracker.get_slot("time")
        if time is None:
            return {"start_datetime": None}            
        if isinstance(time, dict):
            # {"start_datetime":"tomorrow","end_datetime":"day after tomorrow",
            #  "time":{"to":"2019-09-21T00:00:00.000-07:00","from":"2019-09-19T00:00:00.000-07:00"}}
            from dateutil.parser import parse
            start = parse(time['from'])
            end = parse(time['to'])
            if start > end:
                dispatcher.utter_template("utter_start_date_is_greater_than_end_date", tracker)
                return {"start_datetime": None}
            else:
                return {
                    'start_datetime': time['from'],
                    'end_datetime': time['to']
                }
        else:
            return {
                'start_datetime': time
            }

    def validate_reference(self, value, dispatcher, tracker, domain):
        if value.lower() in data:
            return {"reference": value}
        else:
            dispatcher.utter_template("utter_not_a_valid_employee_id", tracker)
            return {"reference": None}
    
    def validate_leave_type(self, value, dispatcher, tracker, domain):
        emp_id = tracker.get_slot("reference")
        if emp_id is None:
            return {"leave_type": None}
        if value.lower() in map(lambda a: a["name"].lower(), data[emp_id]["leave_information"]["enrolments"]):
            return {"leave_type": value}
        else:
            dispatcher.utter_template("utter_not_a_valid_leave_type", tracker)
            return {"leave_type": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        reference = tracker.get_slot('reference')
        leave_type = tracker.get_slot('leave_type')
        start_datetime = tracker.get_slot('start_datetime')
        end_datetime = tracker.get_slot('end_datetime')
        dispatcher.utter_message("Your leave is Successfully applied {0} {1} {2} {3}.".format(reference, leave_type, start_datetime, end_datetime))
        return []

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

class ActionUtterYouAreOutOfBalances(Action):
    def name(self) -> Text:
        return "action_utter_you_are_out_of_balances"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You ran out of balances.")
        return []

class ActionUtterAlreadyLeaveOnDateRangeProvided(Action):
    def name(self) -> Text:
        return "action_utter_already_leave_on_date_range_provided"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # - text: Already there is a leave on this date range. Please provide another date range.
        # - text: You cannot apply on this date range since there is another leave. Please provide another date range.
        dispatcher.utter_message("Already there is a leave on this date range. Please provide another date range.")
        return []

class ActionApplyALeave(Action):
    def name(self) -> Text:
        return "action_apply_a_leave"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reference = tracker.get_slot('reference')
        leave_type = tracker.get_slot('leave_type')
        start_datetime = tracker.get_slot('time')['from']
        end_datetime = tracker.get_slot('time')['to']
        dispatcher.utter_message("Your leave is Successfully applied {0} {1} {2} {3}.".format(reference, leave_type, start_datetime, end_datetime))
        return []

class ActionUtterLeaveConfirmationMessage(Action):
    def name(self) -> Text:
        return "action_utter_leave_confirmation_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reference = tracker.get_slot('reference')
        leave_type = tracker.get_slot('leave_type')
        start_datetime = tracker.get_slot('time')['from']
        end_datetime = tracker.get_slot('time')['to']
        dispatcher.utter_message("Can I apply Leave.", reference, leave_type, start_datetime, end_datetime)
        return []

class ActionUtterLeaveConfirmedMessage(Action):
    def name(self) -> Text:
        return "action_utter_leave_confirmed_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Leave Created.")
        return []

class FallbackAction(Action):
    def name(self) -> Text:
        return "fallback_action"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        from rasa_core.events import UserUtteranceReverted
        dispatcher.utter_message("Sorry, didn't get that. Try again.")
        try:
            return [UserUtteranceReverted()]
        except:
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

class ActionSlotResetExceptEmployeeID(Action):
    def name(self):
        return 'action_slot_reset_except_employee_id'
    def run(self, dispatcher, tracker, domain):
        emp_id = tracker.get_slot('reference')
        if emp_id is not None:
            return [AllSlotsReset(), SlotSet('reference', emp_id), SlotSet('is_valid_reference', True)]
        return[AllSlotsReset()]
