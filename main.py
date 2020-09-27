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
        self.completed: bool = completed


class Deposit:
    def __init__(self, target_portfolio, amount, currency, ratio):
        self.target_portfolio = target_portfolio
        self.amount = amount
        self.currency = currency,
        self.ratio = ratio  # assume that on creation of a Deposit object the ratio is calculated and stored


class User:
    def __init__(self, name, portfolios, deposit_plans):
        self.name = name
        self.portfolios = portfolios
        self.deposit_plans = deposit_plans


# we're not going to handle creating new plans. user has already created 2 plans.
one_time_plan = DepositPlan(
    [
        Deposit('high_risk', 100, 'sgd', 1 / 6),
        Deposit('core', 200, 'sgd', 2 / 6),
        Deposit('buy_a_home', 300, 'sgd', 3 / 6)
    ],
    'one_time',
    False
)
monthly_plan = DepositPlan(
    [
        Deposit('high_risk', 20, 'sgd', 2 / 6),
        Deposit('core', 10, 'sgd', 1 / 6),
        Deposit('buy_a_home', 30, 'sgd', 3 / 6)
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

    cash = Decimal(cash_received)
    global portfolio_list

    # SEMI-HAPPY PATH - users will deposit equal or more money than plans require. use case for less deposit not handled
    for plan in deposit_plans:
        if plan.completed is False:
            for portfolio in portfolio_list:
                for deposit in plan.deposits:
                    if portfolio.name == deposit.target_portfolio:
                        # distribute deposited money to all portfolios
                        deposit_amt = Decimal(cash_received) * Decimal(deposit.ratio)

                        if deposit_amt > deposit.amount:
                            deposit_amt = Decimal(deposit.amount)
                        # perform rounding at the last possible moment
                        deposit_amt = deposit_amt.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)
                        portfolio.amount += deposit_amt
                        cash -= deposit_amt
                    # naive one time deposit plan handling
                    if plan.recurrence == 'one_time':
                        plan.completed = True

    # if there's some left then see allocate to monthly
    if cash > 0:
        leftover_cash = cash
        for plan in deposit_plans:
            if plan.recurrence == 'monthly' and plan.completed is False:
                for portfolio in portfolio_list:
                    for deposit in plan.deposits:
                        if portfolio.name == deposit.target_portfolio:
                            # distribute remaining money to all portfolios
                            deposit_amt = Decimal(leftover_cash) * Decimal(deposit.ratio)
                            # perform rounding at the last possible moment
                            deposit_amt = deposit_amt.quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)
                            portfolio.amount += deposit_amt
                            cash -= deposit_amt

    # console output the result
    for portfolio in portfolio_list:
        print(portfolio.name + ' ' + str(portfolio.amount))


def main():
    # modify the plans and the amount here for repl.it run
    process_deposit([one_time_plan, monthly_plan], 1000)


if __name__ == "__main__":
    main()
