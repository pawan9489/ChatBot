## Know upcoming holidays
* ask_for_holidays_information
    - action_fetch_holidays_information
* appraisal.good OR confirmation.yes
    - utter_need_any_more_information
* confirmation.no
    - utter_have_a_nice_day
    - action_slot_reset

## Know upcoming holidays
* ask_for_holidays_information
    - action_fetch_holidays_information
* appraisal.good OR confirmation.yes
    - utter_need_any_more_information
* appraisal.good OR confirmation.yes
    - utter_how_can_i_help_you_more
    - action_slot_reset

## Know upcoming holidays 2
* ask_for_holidays_information
    - action_fetch_holidays_information
* greetings.bye OR greetings.goodnight
    - utter_have_a_nice_day
    - action_slot_reset