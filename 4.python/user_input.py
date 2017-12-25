#  Prompt user for input
x = int(input('x = '))
y = int(input('y = '))

#  do some calculation and format the results
print('{} plus {} is {}'.format(x, y, x+y))
print('{} minus {} is {}'.format(x, y, x-y))
print('{} times {} is {}'.format(x, y, x*y))
print('{} divided by {} is {}'.format(x, y, x/y))
print('{} divided by {} (and floored) is {}'.format(x, y, x//y))
print('remainder of {} divided by {} is {}'.format(x, y, x%y))
