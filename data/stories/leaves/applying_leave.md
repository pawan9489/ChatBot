## Apply Leave 1
* apply_leave
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_leave_type
* saying_leave_type
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 2
* apply_leave
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_leave_type
* saying_leave_type
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* confirmation.no
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 3
* apply_leave{"leave_type": "annual"}
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 4
* apply_leave{"leave_type": "annual"}
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* confirmation.no
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 5 Couldn't find employee ID
* apply_leave
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_leave_type
* saying_leave_type
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 6 Already a leave on So and So dates
* apply_leave
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_leave_type
* saying_leave_type
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset

