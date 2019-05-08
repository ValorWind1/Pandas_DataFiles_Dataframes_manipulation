import csv


f = open("schedule.csv")

csv_f = csv.reader(f)

evaluation = []
teachers = []
classes = ['section  A', 'section  B', 'section  C', 'section  D', 'section  E', 'section  F', 'section  G', 'section  H', 'section  I', 'section  J', 'section  K', 'section  L', 'section  M', 'section  N', 'section  O', 'section  P', 'section  Q', 'section  R', 'section  S', 'section  T', 'section  U', 'section  V', 'section  W', 'section  X', 'section  Y', 'section  Z']
fives= []


for row in csv_f:
    evaluation.append(row[1])
    teachers.append(row[0])


print(classes)
print(evaluation)
print(teachers)
# print(len(evaluation))
# print(len(teachers))


f.close()

evaluation1 = dict([(k,v)for k,v in zip (evaluation[::],evaluation[::])])
teachers1 = dict([(k,v)for k,v in zip (teachers[::],teachers[::])])
classes1 = dict([(k,v)for k,v in zip (classes[::],classes[::])])

for value in evaluation1:
    print(value)

for value in teachers1:
    print(value)

for value in classes1:
   print(value)

sorted(evaluation)

for i in evaluation:
    evaluation.remove('1')
    print(i)
    classes.insert(3,i)
    print(classes)