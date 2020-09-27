# SA-deposit-split

## Requiments
Python 3+

### Summary

A user is pre-configured with 1 monthly and 1 one-time deposit plan. 
The deposit plans have been set up for 3 different portfolios named very lazily.

Running the `main.py` will trigger a pre-defined fund deposit.

Most assumptions have been stated as comments.

I recognise that there is a DB on repl, but I'm developing this locally, so I won't be leveraging it.
 
#### Known limitations

* Maximum deposit plans = 2
* Fund deposits are whole dollars

Edge cases handled:
* Fund deposit more than specified in deposit plans

Edge cases thought of but not handled:
* Fund deposit less than specified in deposit plans
* Providing multiple One Time Deposit Plans
* Providing multiple Monthly Deposit Plans
* Non-whole dollar fund deposit amounts
* Bugged state - negative fund deposit

There is a lot of nuance and edge cases to be handled which far exceeds the time 
I would like to spend on this test even on a happy path.
### Running

```bash
python ./main.py
```

### Adding a new deposit plan

While in the python console - copy this snippet, the `recurrance = ['one_time'|'monthly']`
```python
one_time_plan = DepositPlan(
    [
        Deposit('high_risk', 100, 'sgd'),
        Deposit('core', 200, 'sgd'),
        Deposit('buy_a_home', 300, 'sgd')
    ],
    'one_time',
    False
)
```
Then trigger a fund deposit 
```python
    process_deposit([one_time_plan], 1000)
```