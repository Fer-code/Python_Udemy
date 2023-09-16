#OBS: 'tudo em python é um objeto'
#------------f-string---------------------

nome = 'fernanda'

texto = f'olar {nome}'

print(texto)

tamanho = 1.80

texto2 = f'A variavel tamanho tem valor {tamanho:.3f}'
#3f = 3 casas decimais

print(texto2)

dinheiro = 10050.5

texto3 = f'dinheiro é igual a {dinheiro:,.3f}'

print(texto3)

#------------ função format ---------------------
a= 'A'
b = 'B'
c = 1.1

formato = 'a = {0},  b = {1},  c = {2:.4f}'.format(a,b,c)

formato2 = 'a={nome1}, b{nome2}, c{nome3}'

format3 = formato2.format(nome1=a, nome2=b, nome3=c)

print(formato)
print(format3)