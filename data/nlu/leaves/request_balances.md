## synonym:balances   <!-- synonyms, method 2 -->
- balances
- entitlement
- entitlements

## regex:year
- \b[2]\d{3}\b

## lookup:leave_type  <!-- no list to specify lookup table file -->
data/nlu/leaves/leave_types.txt

## intent:ask_for_balances
- what is my [balance](balance:balances)
- May I know my [balance](balance:balances)
- My [balance](balance:balances) please
- Fetch my [balance](balance:balances)
- Get my [balance](balance:balances)
- [Sick](leave_type) Leave [balance](balance:balances)
- [balance](balance:balances)?
- [Annual](leave_type) leave [balance](balance:balances)
- [Annual](leave_type) [balance](balance:balances)
- My [balance](balance:balances) for [2019](year) year
- [balance](balance:balances) of [current year](year_string)
- [balance](balance:balances) of [next year](year_string)
- May i know my [balance](balance:balances) of [this year](year_string)
- My remaining [balance](balance:balances)
- Remaining [balance](balance:balances)

## intent:ask_for_expiring_balances
- My [balance](balance:balances) that are about to expire
- Expiring leave [balance](balance:balances)

## intent:saying_leave_type
- [sick](leave_type)
- [sick](leave_type) leave
- My [sick](leave_type) leave

## intent:saying_which_year
- [this year](year_string)
- [current year](year_string)
- [next year](year_string)
- [last year](year_string)
- [last year](year_string)
