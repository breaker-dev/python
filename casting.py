age = 23
convert_age = str(age)


print('My name is breaker I am '+convert_age+'years old')
print('My name is breaker I am '+str(age)+'years old')

prize = 30.56
print(int(prize))

item = 30
print(float(item))


name = 'breaker'
number = 4
state = 'chicago'
salary = 2500.55

result = 'I am '+name+', from '+state
result += ' and married with '+str(number)+'children and I earn '+str(salary)
print(result)


result1 = 'I am {}, from {} and married with {} children and I earn {} as salary'.format(name, number, state, salary)
print(result)
result2 = f'I am {name}, from {state} and married with {number} children and i earn {salary}'
print(result)
