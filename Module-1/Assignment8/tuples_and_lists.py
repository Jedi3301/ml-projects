class Transaction:
    def __init__(self, id, amount, transaction_type, timestamp):
        self.id = id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp

    def __str__(self):
        ts = self.timestamp
        timestamp_format = f"{ts[0]:04d}-{ts[1]:02d}-{ts[2]:02d} Time: {ts[3]:02d}:{ts[4]:02d}:{ts[5]:02d}"
        return f"Transaction id = {self.id}, Amount = {self.amount}, Transaction Type = {self.transaction_type}, Timestamp = {timestamp_format}"


class Account:
    def __init__(self):
        self.transactions = []

    def add_tran(self, transaction):
        self.transactions.append(transaction)

    def calculate_account_balance(self):
        balance = 1000
        print(f"Balance in account Before transaction: {balance}")
        for i in self.transactions:
            if i.transaction_type == "credit":
                balance += i.amount
            elif i.transaction_type == "debit":
                if balance >= i.amount:
                    balance -= i.amount
                else:
                    print(f"Insufficient Balance {i.amount}. Current Balance: {balance}")
        return balance

    def generate_transaction_report(self):
        print("Transaction ID\tAmount\tTransaction Type\tTimestamp")
        for tran in self.transactions:
            ts = tran.timestamp
            timestamp_format = f"{ts[0]:04d}-{ts[1]:02d}-{ts[2]:02d} {ts[3]:02d}:{ts[4]:02d}:{ts[5]:02d}"
            print(f"{tran.id}\t\t{tran.amount}\t\t{tran.transaction_type}\t\t{timestamp_format}")


def test():
    my_account = Account()
    t1 = Transaction(1, 1000, 'credit', (2022, 4, 8, 10, 30, 0))
    t2 = Transaction(2, 200, 'debit', (2023, 4, 9, 15, 45, 0))
    t3 = Transaction(3, 500, 'credit', (2024, 4, 10, 9, 0, 0))
    my_account.add_tran(t1)
    my_account.add_tran(t2)
    my_account.add_tran(t3)

    print("\nAccount Balance:", my_account.calculate_account_balance())
    print("\nTransaction Report:")
    my_account.generate_transaction_report()


test()
