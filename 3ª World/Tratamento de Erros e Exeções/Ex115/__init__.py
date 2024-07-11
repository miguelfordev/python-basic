from time import sleep

def cadastro(nome, idade, arquivo="listaDePessoas.txt"):
    with open(arquivo, "a") as arquivo:
        arquivo.write(f"{nome},{idade}\n")
    print(f"{nome} foi cadastrado(a) com sucesso!")


def listagem(arquivo="listaDePessoas.txt"):
    try:
        with open(arquivo, "r") as arquivo:
            listaDePessoas = arquivo.readlines()
            for pessoa in listaDePessoas:
                nome, idade = pessoa.strip().split(',')
                print(f"Nome: {nome}, Idade: {idade}")
    except FileNotFoundError:
        print("Ainda não há pessoas cadastradas.")

def traco():
    print("-="*15)

def menu():
    print("=-=- Sistema de Cadastro -=-=")
    print("1. Cadastrar Pessoa")
    print("2. Listar Pessoas")
    print("3. Sair")
    return int(input("Escolha uma opção: "))

def main():
    while True:
        opcao = menu()
        traco()
        if opcao == 1:
            sleep(0.7)
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade da pessoa: ")
            cadastro(nome, idade)
            traco()
        elif opcao == 2:
            sleep(0.7)
            print("Pessoas Cadastradas:")
            listagem()
            traco()
        elif opcao == 3:
            sleep(0.7)
            print("Encerrando o sistema...")
            break
        else:
            sleep(0.7)
            print("Opção inválida. Tente novamente.")
            traco()