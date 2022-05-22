"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 ...
float - real/poonto flutuante - 10.50  1.5  -10.10 -50.93 ...
bool - booleano/lógico - True/False  10 == 10 True  10 == 20 False
"""
# print(type('Diogo'))
# print(type(1234546))
# print(type(10.50))
#print(type(10 == 10))

nome = 'Diogo'
idade = 37
altura = 1.77
maiorDeidade = idade > 18

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(maiorDeidade, type(maiorDeidade))

if maiorDeidade == True:
    print(nome + ' é maior de idade')
