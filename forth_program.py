
days = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for day in days:
    if days.index(day) == len(days) - 1:
       print('Toi ko di lam vao ' + day)
    else:
       print('Toi di lam vao ' + day)
