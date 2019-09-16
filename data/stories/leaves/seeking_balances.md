## Fetch entitlement - this year
* ask_for_balances
    - utter_leave_type
* saying_leave_type{"leave_type": "annual"}
    - slot{"year_string": "current year"}
    - action_fetch_entitlement

## Remaining entitlement - with Leave Type from user
* ask_for_balances{"leave_type": "annual"}
    - slot{"year_string": "current year"}
    - action_fetch_entitlement

## Remaining entitlement - with Leave Type and Year from user
* ask_for_balances{"leave_type": "annual", "year": "2019"}
    - action_fetch_entitlement

## Remaining entitlement - with Leave Type and Year String from User
* ask_for_balances{"leave_type": "annual", "year_string": "current year"}
    - action_fetch_entitlement

## Remaining entitlement - that are going to expire
* ask_for_expiring_balances
    - utter_leave_type
* saying_leave_type{"leave_type": "annual", "year_string": "current year"}
    - action_fetch_entitlement_expiring
