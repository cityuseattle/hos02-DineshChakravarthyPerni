income = {'Alice': 90000,
          'Bob': 100000,
          'Jeff': 200000,
          'Apiwat': 999998,
          'Stark': 999999}
lowest = min(income, key=income.get)
print("The lowest income man on earth", end='')
print(lowest + 'with $' + str(income[lowest]))

