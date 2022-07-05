"""
    CPF Verificador
"""

cpf = input('Digite o CPF para ser verificado :  ')
cpffim = cpf[-2:]
"1 digito"
cpf1 = cpf[:9]
mult1 = 10
dig1 = 0
digi1s = 0
digt1 = 0
cpf1 = cpf[:9]
mult1 = 10
dig1 = 0
digi1s = 0
digt1 = 0

"2 digito"

cpf2 = cpf[:9]
mult2 = 11
dig2 = 0
digi2s = 0
digt2 = 0

for index in range(9):
    dig1 = int(cpf1[index]) * mult1
    digi1s += dig1
    mult1 = mult1 - 1

digt1 = (digi1s * 10) % 11

"2 verificação"

for index in range(9):
    dig2 = int(cpf2[index]) * mult2
    digi2s += dig2
    mult2 = mult2 - 1

digi2s += digt1 * 2
digt2 = (digi2s * 10) % 11

print(f'O digitos finais do cpf:{cpf} são {digt1} e {digt2} ')

if digt1 == int(cpf[9]) and digt2 == int(cpf[10]):
    print('CPF VALIDO')
else:
    print('CPF INVALIDO')