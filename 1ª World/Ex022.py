'''                         Aula 09 - String
-----------------------------------------------------------------------

frase = 'Curso em Video Python'
        01234567891011121314151617181920

-----------------------------------------------------------------------
- Fatiamento:
    print(frase[9]) -> 'V'
    print(frase[9:13]) -> inicio: 9 = 'V', e vai ate final: 12 = 'e'
    print(frase[9:21]) -> 'V' ate 'o'
    print(frase[9:21:2]) -> inicio: 9 = 'V', final 21(para antes): 20 = 'o', e o passo(salto/de qnt em qnt): de dois(2) em dois(2) = 'V','d','o','p','t','o'
    print(frase[:5]) -> inicio: 0, final: 5 = desconsidera e para em 4 = 'o'
    print(frase[15:]) -> inicio: 15 = 'P' e vai ate o final da Str
    print(frase[9::3]) -> inicio: 9 = 'V' e vai ate o final pulando de 3 em 3

-----------------------------------------------------------------------    
- Analise:
    len(frase) == 21 <- 'comprimento da frase'
    frase.count('o') == 3 <- 'conta quantos letras 'o' tem na Str.'
    frase.count('o',0,13) == 1 <- 'conta quantos letras 'o' tem na Str, entre 0 = inicio e final = 12.'
    frase.find('deo') == 11 <- 'mostra o momento que comecou o 'deo'.'
    frase.find('Android') == -1 <- 'mostra que o valor nao existe ou nao foi encontrado.'
    'Curso' in frase == True <- 'mostra se sim ou nao(True/False).'

-----------------------------------------------------------------------    
- Transformacao:
    frase.replace('Python','Android') == 'Curso em Video Android' <- 'substitiu uma letra ou uma palavra da Str.'
    frase.upper() == 'CURSO EM VIDEO PYTHON' <- 'transformar todas as letras que estavam em minusculas em maisculas.' #nao esquecer os paratenses se nao a funcao nao funciona.
    frase.lower() == 'curso em video python' <- 'transformar todas as letras que estavam em maisculos em minusculas.'
    frase.capitalize() == 'Curso em video python' <- 'deixa apenas a primeira letra para maiuscula.'
    frase.title() == 'Curso Em Video Python' <- 'transforma a proxima letra a cada quebra de espaco em maiuscula.'
    
    frase = '   Aprenda Python  '
    frase.strip() == 'Aprenda Python' <- 'remove espacos inuteis na frente e no final da str.'
    frase.rstrip() == '   Aprenda Python' <- 'remove os ultimos espacos.'
    frase.lstrip() == 'Aprenda Python  ' <- 'remove os primeiros espacos.'

-----------------------------------------------------------------------    
- Divisao:
    frase.split() == 'Curso' 'em' 'Video' 'Python' <- 'a cada espaco divide e recebe uma indexacao nova.'
                      [0:4]  [0:2] [0:4]    [0:5]
                        0      1     2        3     <- 'cada palavra um numero dentro da lista agora == 'splitador'.'

-----------------------------------------------------------------------
- Juncao:
    '-'.join(frase) == 'Curso-em-Video-Python' <- 'junta as str com o separador que foi escolhido == '-'.'

-----------------------------------------------------------------------    
- Imprimindo Texto:
    print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join()""") # As aspas podem ser simples ou duplas.

'''

"""
-----------------------------------------------------------------------
Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiusculas.
    - O nome com todas minusculas.
    - Quantas letras ao todo (sem consdiderar espacos).
    - Quantas letras tem o primeiro nome."""
nome = input('\nDigite seu nome completo: ')
print(f'Nome maiusculo: {nome.upper()}, nome minusculo: {nome.lower()}, letras ao todo: {len(nome) - nome.count(" ")} letras e primeira letra do nome: {nome[0]}')
