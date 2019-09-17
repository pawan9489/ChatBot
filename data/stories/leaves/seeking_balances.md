## Fetch entitlement - this year
* ask_for_balances
    - utter_leave_type
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
