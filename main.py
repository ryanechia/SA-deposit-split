class Portfolio:
    def __init__(self, name, amount, risk):
        self.name = name
        self.amount = amount
        self.risk = risk


class DepositPlan:
    def __init__(self, deposits, recurrence, completed):
        self.deposits = deposits
        self.recurrence = recurrence
        self.completed = completed


class Deposit:
    def __init__(self, target_portfolio, amount, currency, ratio):
        self.target_portfolio = target_portfolio
        self.amount = amount
        self.currency = currency,


class User:
    def __init__(self, name, portfolios, deposit_plans):
        self.name = name
        self.portfolios = portfolios
        self.deposit_plans = deposit_plans


# we're not going to handle creating new plans. user has already created 2 plans.
one_time_plan = DepositPlan(
    [
        Deposit('high_risk', 100, 'sgd'),
        Deposit('core', 200, 'sgd'),
        Deposit('buy_a_home', 300, 'sgd')
    ],
    'one_time',
    False
)
monthly_plan = DepositPlan(
    [
        Deposit('high_risk', 20, 'sgd'),
        Deposit('core', 10, 'sgd'),
        Deposit('buy_a_home', 30, 'sgd')
    ],
    'monthly',
    False
)


def main():
    print('hello world')


if __name__ == "__main__":
    main()
