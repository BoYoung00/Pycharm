# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' %('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (424545))
print('{:4d}'.format(42))
print()

# %f
print('%1.8f' % (3.144654644))
print('{:f}'.format(3.154546465))

print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
print()