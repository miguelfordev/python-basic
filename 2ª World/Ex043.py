''' Desafio 43: Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela baixo:
- Abaixo de 18.5:
    ABAIXO DO PESO
- Entre 18.5 e 25:
    PESO IDEAL
- 25 ate 30:
    SOBREPESO
- 30 ate 40:
    OBESIDADE
- Acima de 40:
    OBESIDADE MORBIDA
'''

p = float(input('\nDigite o peso: '))
a = float(input('Digite a altura: '))
imc=p/a**2
if imc<18.5:
    print('abaixo do peso')
elif imc >=18.5 and imc<25:
    print('peso ideal')
elif imc >=25 and imc<30:
    print('sobrepeso')
elif imc >=30 and imc<40:
    print('obesidade')
else:
    print('obesidade morbida')