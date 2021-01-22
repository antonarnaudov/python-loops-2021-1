transactions_count = int(input('Enter number of transactions: '))
counter_transactions = 0
total = 0

while transactions_count > counter_transactions:
    transaction_cash = float(input('Enter transaction amount: '))

    if transaction_cash >= 1:
        total += transaction_cash
        counter_transactions += 1
        print(f'Increase: {transaction_cash:.2f}')
    #   continue

    # delete elif
    elif transaction_cash < 1:
        print('Invalid operation!')
        break

print(f'Total: {total:.2f}')
# explain :.2f
