def lowest_price():
    prices = {}
    with open('prices.txt') as file:
        line = file.readline().rstrip()
        record = line.split(';')
        while line:
            item = record[0]
            lowest_price = record[1]
            while line and record[0] == item:
                if float(record[1]) < float(lowest_price):
                    lowest_price = record[1]
                line = file.readline().rstrip()
                record = line.split(';')
            prices[item] = lowest_price
    return prices

prices = lowest_price()
print('Price list');
print(len('Price list') * '-')
for item in prices:
    print(item, '\t', prices[item])
print()

item = input('Enter the item (press x if you want to stop): ')
while item.upper() != 'X':
    if item not in prices:
        print('This item is not available.')
    else:
        print('The lowest price of', item.lower(), 'is', prices[item], 'EUR')

    item = input('Enter the item (press x if you want to stop): ')
