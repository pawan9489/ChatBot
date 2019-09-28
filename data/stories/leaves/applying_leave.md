<!-- 
## Happy Path 1, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"requested_slot":"reference"}
* saying_employee_id
    - apply_leave_form
    - slot{"reference":"EID00001"}
    - slot{"requested_slot":"leave_type"}
* saying_leave_type
    - apply_leave_form
    - slot{"leave_type":"Annual"}
    - slot{"requested_slot":"start_datetime"}
* saying_leave_date_range
    - apply_leave_form
    - slot{"start_datetime": "tomorrow"}
    - slot{"requested_slot":"is_leave_booking_confirmed"}
* appraisal.good OR confirmation.yes
    - apply_leave_form
    - slot{"is_leave_booking_confirmed": true}
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id
    - form{"name": null}

## UnHappy Path 2, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"requested_slot":"reference"}
* saying_employee_id
    - apply_leave_form
    - slot{"reference":"EID00001"}
    - slot{"requested_slot":"leave_type"}
* saying_leave_type
    - apply_leave_form
    - slot{"leave_type":"Annual"}
    - slot{"requested_slot":"start_datetime"}
* saying_leave_date_range
    - apply_leave_form
    - slot{"start_datetime": "tomorrow"}
    - slot{"requested_slot":"is_leave_booking_confirmed"}
* confirmation.no OR user.does_not_want_to_talk
    - action_slot_reset_except_employee_id 
-->

<!-- 
## UnHappy Path 3, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"requested_slot":"is_leave_booking_confirmed"}
* confirmation.no OR confirmation.cancel OR user.does_not_want_to_talk
    - apply_leave_form
    - action_deactivate_form
    - slot{"is_leave_booking_confirmed": false}
    - action_slot_reset_except_employee_id
    - form{"name": null}

## Happy Path 4, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"requested_slot":"is_leave_booking_confirmed"}
* appraisal.good OR confirmation.yes
    - apply_leave_form
    - slot{"is_leave_booking_confirmed": true}
    - action_slot_reset_except_employee_id
    - form{"name": null} 
-->

## Apply leave - Happy Path via applying leave
* apply_leave
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

## Apply Leave - Think of applying and immediately cancels
* apply_leave
    - apply_leave_form
    - form{"name":"apply_leave_form"}
    - slot{"reference":"eid44220"}
    - slot{"name":"Bob Martin"}
    - slot{"requested_slot":"leave_type"}
* deny_confirmation_of_leave_applying OR confirmation.no OR confirmation.cancel OR user.does_not_want_to_talk
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id
    - slot{"reference":"eid44220"}
    - slot{"is_valid_reference":true}

## Apply Leave - Think of applying and cancels after saying leave type
* apply_leave
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

## Apply Leave - Think of applying and cancels after asking confirmation
* apply_leave
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