# a1 = True && (!True || (!True)) && !False
a1 = True and (not True or (not True)) and not False
print(f'{a1=}')

a2 = not not not True or (not False and not not True and 6 % 2 == 0)
print(f'{a2=}')

a3 = not not not True or (not False and not not True and 6 % 2 != 0)
print(f'{a3=}')

a4 = False or not (True and (not False or True))
print(f'{a4=}')
