import csv

with open('schedule.csv', 'r') as f:
  reader = csv.reader(f)

  your_list = list(reader)

  for position, item in enumerate(your_list):
    if item == 1:
        print(position)

print(your_list)
