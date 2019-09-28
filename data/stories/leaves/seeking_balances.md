<!-- 
## Fetch entitlement - this year
* ask_for_balances
    - utter_ask_leave_type
* saying_leave_type{"leave_type": "annual"}
    - slot{"year_string": "current year"}
    - action_fetch_entitlement
    - action_slot_reset

## Remaining entitlement - with Leave Type from user
* ask_for_balances{"leave_type": "annual"}
    - slot{"year_string": "current year"}
    - action_fetch_entitlement
    - action_slot_reset

## Remaining entitlement - with Leave Type and Year from user
* ask_for_balances{"leave_type": "annual", "year": "2019"}
    - action_fetch_entitlement
    - action_slot_reset

## Remaining entitlement - with Leave Type and Year String from User
* ask_for_balances{"leave_type": "annual", "year_string": "current year"}
    - action_fetch_entitlement
    - action_slot_reset 
-->

<!-- 
## Fetch entitlement - Happy Path
* ask_for_balances
    - seek_balances_form
    - form{"name": "seek_balances_form"}
    - form{"name": null}
* confirmation.yes OR appraisal.good
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - action_slot_reset_except_employee_id
    - form{"name": null}

## Fetch entitlement - Sad Path
* ask_for_balances
    - seek_balances_form
    - form{"name": "seek_balances_form"}
    - form{"name": null}
* confirmation.no OR confirmation.cancel OR user.does_not_want_to_talk
    - action_slot_reset_except_employee_id
    - utter_have_a_nice_day 
-->
## Fetch Entitlements - Happy Path via applying leave
* ask_for_balances
    - seek_balances_form
    - form{"name": "seek_balances_form"}
    - slot{"requested_slot": "reference"}
* form: saying_employee_id{"reference": "eid44220", "number": 44220}
    - slot{"reference": "eid44220"}
    - form: seek_balances_form
    - slot{"reference": "eid44220"}
    - slot{"name": "Bob Martin"}
    - form{"name": null}
    - slot{"requested_slot": null}
* confirmation.yes OR appraisal.good
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"reference": "eid44220"}
    - slot{"name": "Bob Martin"}
    - slot{"requested_slot": "leave_type"}
* form: saying_leave_type{"leave_type": "annual"}
    - slot{"leave_type": "annual"}
    - form: apply_leave_form
    - slot{"leave_type": "annual"}
    - slot{"requested_slot": "start_datetime"}
* form: saying_leave_date_range{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow", "time": {"to": "2019-09-30T00:00:00.000-07:00", "from": "2019-09-28T00:00:00.000-07:00"}}
    - slot{"end_datetime": "day after tomorrow"}
    - slot{"start_datetime": "tomorrow"}
    - form: apply_leave_form
    - slot{"start_datetime": "28/09/2019"}
    - slot{"end_datetime": "30/09/2019"}
    - slot{"requested_slot": "is_leave_booking_confirmed"}
* form: confirmation.yes OR appraisal.good
    - form: apply_leave_form
    - slot{"is_leave_booking_confirmed": true}
    - form: reset_slots
    - slot{"reference": "eid44220"}
    - slot{"is_valid_reference": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset_except_employee_id
    - reset_slots
    - slot{"reference": "eid44220"}
    - slot{"is_valid_reference": true}
    - utter_have_a_nice_day

## Fetch Entitlements - But dont apply leave
* ask_for_balances
    - seek_balances_form
    - form{"name":"seek_balances_form"}
    - slot{"requested_slot":"reference"}
* saying_employee_id{"reference":"eid44220","number":44220}
    - slot{"reference":"eid44220"}
    - seek_balances_form
    - slot{"reference":"eid44220"}
    - slot{"name":"Bob Martin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* confirmation.no OR deny_confirmation_of_leave_applying OR confirmation.cancel OR user.does_not_want_to_talk
    - utter_have_a_nice_day

## Fetch Entitlements - Think of applying and immediately cancels
* ask_for_balances
    - seek_balances_form
    - form{"name":"seek_balances_form"}
    - slot{"requested_slot":"reference"}
* saying_employee_id{"reference":"eid44220","number":44220}
    - slot{"reference":"eid44220"}
    - seek_balances_form
    - slot{"reference":"eid44220"}
    - slot{"name":"Bob Martin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* confirmation.yes OR appraisal.good
    - apply_leave_form
    - form{"name":"apply_leave_form"}
    - slot{"reference":"eid44220"}
    - slot{"name":"Bob Martin"}
    - slot{"requested_slot":"leave_type"}
* deny_confirmation_of_leave_applying OR confirmation.no OR confirmation.cancel OR user.does_not_want_to_talk
    - utter_leave_booking_has_been_cancelled
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id
    - slot{"reference":"eid44220"}
    - slot{"is_valid_reference":true}

## Fetch Entitlements - Think of applying and cancels after saying leave type
* ask_for_balances
    - seek_balances_form
    - form{"name": "seek_balances_form"}
    - slot{"requested_slot": "reference"}
* form: saying_employee_id{"reference": "eid44220", "number": 44220}
    - slot{"reference": "eid44220"}
    - form: seek_balances_form
    - slot{"reference": "eid44220"}
    - slot{"name": "Bob Martin"}
    - form{"name": null}
    - slot{"requested_slot": null}
* confirmation.yes OR appraisal.good
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"reference": "eid44220"}
    - slot{"name": "Bob Martin"}
    - slot{"requested_slot": "leave_type"}
* form: saying_leave_type{"leave_type": "annual"}
    - slot{"leave_type": "annual"}
    - form: apply_leave_form
    - slot{"leave_type": "annual"}
    - slot{"requested_slot": "start_datetime"}
* deny_confirmation_of_leave_applying OR confirmation.no OR confirmation.cancel OR user.does_not_want_to_talk
    - utter_leave_booking_has_been_cancelled
    - action_slot_reset_except_employee_id
    - reset_slots
    - slot{"reference": "eid44220"}
    - slot{"is_valid_reference": true}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_have_a_nice_day

## Fetch Entitlements - Think of applying and cancels after asking confirmation
* ask_for_balances
    - seek_balances_form
    - form{"name": "seek_balances_form"}
    - slot{"requested_slot": "reference"}
* form: saying_employee_id{"reference": "eid44220", "number": 44220}
    - slot{"reference": "eid44220"}
    - form: seek_balances_form
    - slot{"reference": "eid44220"}
    - slot{"name": "Bob Martin"}
    - form{"name": null}
    - slot{"requested_slot": null}
* confirmation.yes OR appraisal.good
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"reference": "eid44220"}
    - slot{"name": "Bob Martin"}
    - slot{"requested_slot": "leave_type"}
* form: saying_leave_type{"leave_type": "annual"}
    - slot{"leave_type": "annual"}
    - form: apply_leave_form
    - slot{"leave_type": "annual"}
    - slot{"requested_slot": "start_datetime"}
* form: saying_leave_date_range{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow", "time": {"to": "2019-09-30T00:00:00.000-07:00", "from": "2019-09-28T00:00:00.000-07:00"}}
    - slot{"end_datetime": "day after tomorrow"}
    - slot{"start_datetime": "tomorrow"}
    - form: apply_leave_form
    - slot{"start_datetime": "28/09/2019"}
    - slot{"end_datetime": "30/09/2019"}
    - slot{"requested_slot": "is_leave_booking_confirmed"}
* form: deny_confirmation_of_leave_applying OR confirmation.no OR confirmation.cancel OR user.does_not_want_to_talk
    - utter_leave_booking_has_been_cancelled
    - form: apply_leave_form
    - slot{"is_leave_booking_confirmed": false}
    - form: reset_slots
    - slot{"reference": "eid44220"}
    - slot{"is_valid_reference": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset_except_employee_id
    - reset_slots
    - slot{"reference": "eid44220"}
    - slot{"is_valid_reference": true}
    - utter_have_a_nice_day