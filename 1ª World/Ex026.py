'''Faca um programa que leia uma frase pelo teclado e mostre: 
- Quantas vezes aparece a letra "A".
- Em que posicao ela aparece a primeira vez.
- Em que posicao ela aparece a ultima vez. '''
frase = input('\nDigite uma frase no teclado: ').lower().strip()
print(f'''Apareceu {frase.count("a",0)} letras A.
      Aparecendo a primerira vez na posicao: {frase.find("a")+1}
      Aparecendo na ultima vez na posicao: {frase.rfind("a")+1}
      ''')