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
    - utter_not_a_valid_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
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
    - action_utter_already_leave_on_date_range_provided
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 7 Proper dates but No Balances are left to apply
* apply_leave
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_leave_type
* saying_leave_type
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_you_are_out_of_balances
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset

## Apply Leave 8 Already a leave on So and So dates & Proper dates but No Balances are left to apply
* apply_leave
    - utter_provide_the_employee_id
* saying_employee_id
    - utter_wait_till_i_get_you_leave_info
    - utter_leave_type
* saying_leave_type
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_utter_already_leave_on_date_range_provided
* saying_leave_date_range
    - action_utter_you_are_out_of_balances
* saying_leave_date_range
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset
