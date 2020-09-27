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


def main():
    print('hello world')


if __name__ == "__main__":
    main()
