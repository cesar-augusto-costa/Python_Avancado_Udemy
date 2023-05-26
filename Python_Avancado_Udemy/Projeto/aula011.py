# PRECEDENCIA
# 1. () de dentro pra fora
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)
conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)
conta_1 = (1 + int(0.5 + 0.5)) ** 5 + 5
print(conta_1)
