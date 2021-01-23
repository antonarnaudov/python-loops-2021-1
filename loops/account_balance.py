transactions_count = int(input('Enter number of transactions: '))

total = 0

while True:
    if transactions_count <= 0:
        break

    transactions_cash = float(input('Enter transactions amount: '))

    if transactions_cash >= 1:
        total += transactions_cash
        transactions_count -= 1
        continue

    print('Invalid operation!')
    break

print(f'Total: {total:.2f}')