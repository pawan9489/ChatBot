## Happy Path 1, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"requested_slot":"reference"}
* saying_employee_id
    - apply_leave_form
    - slot{"reference":"EID00001"}
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
    - slot{"requested_slot":"start_datetime"}
* saying_leave_date_range
    - apply_leave_form
    - slot{"start_datetime": "tomorrow"}
    - slot{"requested_slot":"is_leave_booking_confirmed"}
* confirmation.no OR user.does_not_want_to_talk
    - action_slot_reset_except_employee_id