# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1)
print('a' + 'b')

# print('1' + 1) # TypeError
print(int('1') + 1, type(int('1') + 1)) 
print(float('1') + 1, type(float('1') + 1))

print('1', type('1'))
print(int('1'), type(int('1')))

print(str(11) + 'b')

print(bool('')) #False
print(bool(' ')) #True

