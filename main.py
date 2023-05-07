from transactions_app.accounts import Accounts
from transactions_app.loader import JSONFileLoader
from transactions_app.transactions import Transactions


def main():
    file_path: str = 'card-transaction-data.json'
    file_reader: JSONFileLoader = JSONFileLoader(file_path)
    json_list: list[dict] = file_reader.read_file()['cardTransactionList']

    Transactions(json_list)
    accounts = Accounts().collection.values()

    for account in accounts:
        print(f'Cashback for account {account.id} is {account.get_cash_back()}')


if __name__ == '__main__':
    main()