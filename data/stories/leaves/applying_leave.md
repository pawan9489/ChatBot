## Happy Path 1
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow", "leave_type": "annual"}
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - form{"name": null}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Happy Path 2
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow", "leave_type": "annual"}
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - form{"name": null}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Happy Path 3, Ask for Employee Refrence, Leave Type, Start Date and End Date
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
    - form{"name": null}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Happy Path 4, Ask for Employee Refrence, Leave Type, Start Date and End Date
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
    - form{"name": null}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## UnHappy Path 5, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - apply_leave_form
    - form{"name": null}
    - action_slot_reset_except_employee_id

## UnHappy Path 6, Ask for Employee Refrence, Leave Type, Start Date and End Date
* apply_leave
    - utter_agent.sure
    - apply_leave_form
    - form{"name": "apply_leave_form"}
    - slot{"requested_slot":"reference"}
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - apply_leave_form
    - form{"name": null}
    - action_slot_reset_except_employee_id