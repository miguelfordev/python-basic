'''         Aula 23 - Tratamento de Erros e Exceções
--------------------------------------------------------------
Excpetion - exceção
-------------------
try: (-> tente)
    (operação)
excpet:
    (falha)
else:
    (se o try deu certo)
finally:
    (ele vai acontecer se deu certo/falha, independente.)

    
ex:
try:
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r= a/b
except: (outra maneira para mostrar qual o erro seria -> except Exception as erro:(-> variável)(.__class__) ) - (outra maneira também seria: excpet TypeError: (para especificar se acontecer esse tipo de erro.))
    print('Infelizmente tivemos um problema.')
except (TypeError, ValueError): (para especificar error de valor e de tipo.)
    (falhou)
except OSError:
    (falhou)
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')
'''