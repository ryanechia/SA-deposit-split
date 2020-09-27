from decimal import Decimal, ROUND_HALF_DOWN


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

# we're not going to handle creating new portfolios.
# emulated DB
high_risk_portfolio = Portfolio('high_risk', 0, 'high_risk')
general_investment_portfolio = Portfolio('core', 0, 'core')
buy_a_home_portfolio = Portfolio('buy_a_home', 0, 'core')
portfolio_list = [high_risk_portfolio, general_investment_portfolio, buy_a_home_portfolio]
user = User('112954-1264612', portfolio_list, [one_time_plan, monthly_plan])


# end emulated DB


def process_deposit(deposit_plans, cash_received):
    # can have additional check to check for plan uniqueness
    assert len(deposit_plans) <= 2, 'too many input plans'
    for plan in deposit_plans:
        assert isinstance(plan, DepositPlan), 'wrong argument type!'


def main():
    # modify the plans and the amount here for repl.it run
    process_deposit([one_time_plan, monthly_plan], 1000)


if __name__ == "__main__":
    main()
