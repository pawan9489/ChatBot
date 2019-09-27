<!-- ## Fetch entitlement - this year
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
    - action_slot_reset -->

## Fetch entitlement - Happy Path
* ask_for_balances
    - seek_balances_form
    - form{"name": "seek_balances_form"}
    - form{"name": null}
* appraisal.good OR confirmation.yes
    - form{"name": "apply_leave_form"}
    - action_slot_reset_except_employee_id
    - form{"name": null}
