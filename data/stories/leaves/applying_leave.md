## Apply Leave 1 (Leave Type, Start, End provided at start)- Already the reference is avaliable, Confirm Yes
* apply_leave{"leave_type": "annual", "start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 1 (Leave Type, Start, End provided at start)- Already the reference is avaliable, Confirm No
* apply_leave{"leave_type": "annual", "start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 1 (Leave Type, Start, End provided at start)- Reference is not available, Confirm Yes
* apply_leave{"leave_type": "annual", "start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_wait_till_i_get_you_leave_info
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 1 (Leave Type, Start, End provided at start)- Reference is not available, Confirm No
* apply_leave{"leave_type": "annual", "start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_wait_till_i_get_you_leave_info
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 1 (Leave Type, Start, End provided at start)- Reference is not available, Provides Invalid Reference, Confirm Yes
* apply_leave{"leave_type": "annual", "start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": false}
    - utter_not_a_valid_employee_id
    - action_utter_provide_the_employee_id
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_wait_till_i_get_you_leave_info
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 1 (Leave Type, Start, End provided at start)- Reference is not available, Provides Invalid Reference, Confirm No
* apply_leave{"leave_type": "annual", "start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": false}
    - utter_not_a_valid_employee_id
    - action_utter_provide_the_employee_id
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_wait_till_i_get_you_leave_info
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 2 (Start and End provided at start)(Valid Leave Type)- Already the reference is avaliable, Confirm Yes
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 2 (Start and End provided at start)(Valid Leave Type)- Already the reference is avaliable, Confirm No
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 2 (Start and End provided at start)(Valid Leave Type)- Already the reference is avaliable, Provided Invalid Leave Type, Confirm yes
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 2 (Start and End provided at start)(Valid Leave Type)- Already the reference is avaliable, Provided Invalid Leave Type, Confirm No
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 2 (Start and End provided at start)(Valid Leave Type)- Reference is not available, Confirm Yes
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 2 (Start and End provided at start)(Valid Leave Type)- Reference is not available, Confirm No
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 3 (Start and End provided at start)(InValid Leave Type)- Already the reference is avaliable, Confirm Yes
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": false}
    - utter_not_a_valid_leave_type
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 3 (Start and End provided at start)(InValid Leave Type)- Already the reference is avaliable, Confirm No
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": false}
    - utter_not_a_valid_leave_type
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 3 (Start and End provided at start)(InValid Leave Type)- Reference is not available, Confirm Yes
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": false}
    - utter_not_a_valid_leave_type
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 3 (Start and End provided at start)(InValid Leave Type)- Reference is not available, Confirm No
* apply_leave{"start_datetime": "tomorrow", "end_datetime": "day after tomorrow"}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": false}
    - utter_not_a_valid_leave_type
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 4 Nothing is provided- Reference is not available, Confirm Yes
* apply_leave{"start_datetime": null, "end_datetime": null, "leave_type": null}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 4 Nothing is provided- Reference is not available, Confirm No
* apply_leave{"start_datetime": null, "end_datetime": null, "leave_type": null}
    - action_utter_provide_the_employee_id
    - slot{"reference": null}
* saying_employee_id
    - action_validate_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 4 Nothing is provided- Reference is available, Confirm Yes
* apply_leave{"start_datetime": null, "end_datetime": null, "leave_type": null}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 4 Nothing is provided- Reference is available, Confirm No
* apply_leave{"start_datetime": null, "end_datetime": null, "leave_type": null}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 5 Nothing is provided- Reference is available, Invalid date range, Confirm Yes
* apply_leave{"start_datetime": null, "end_datetime": null, "leave_type": null}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": false}
    - action_utter_already_leave_on_date_range_provided
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": true}
    - action_utter_leave_confirmation_message
* appraisal.good OR confirmation.yes
    - action_apply_a_leave
    - action_utter_leave_confirmed_message
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

## Apply Leave 5 Nothing is provided- Reference is available, Invalid date range, Confirm No
* apply_leave{"start_datetime": null, "end_datetime": null, "leave_type": null}
    - action_utter_provide_the_employee_id
    - slot{"is_valid_reference": true}
    - utter_leave_type
* saying_leave_type
    - action_validate_leave_type
    - slot{"is_valid_leave_type": true}
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": false}
    - action_utter_already_leave_on_date_range_provided
    - utter_provide_start_and_end_date_of_leave
* saying_leave_date_range
    - action_validate_leave_date_range
    - slot{"is_valid_date_range": true}
    - action_utter_leave_confirmation_message
* confirmation.no OR user.does_not_want_to_talk
    - utter_have_a_nice_day
    - action_slot_reset_except_employee_id

<!-- ## Apply Leave 1
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
    - action_slot_reset -->
