#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('digite algo:')

print('o tipo primitivo dessa variavel é ' , type(n))

print('Só tem espaços? ' , n.isspace())
print('É um numero? ' , n.isnumeric())
print('É alfabetico? ' , n.isalpha())
print('É alfanumerico? ' , n.isalnum())
print('Está em maiusculo? ' , n.isupper())
print('Está em minusculo? ' , n.islower())
print('Está capitallizada? ' , n.istitle())


