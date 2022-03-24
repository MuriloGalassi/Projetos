#imports
import os
import os.path as Path
import json

#functions
def exibirMenu() -> None:
    print("""
1 - Cadastro
2 - Excluir Cadastro
3 - Verificar Cadastro
4 - Sair
""")

def inserircadastro() -> None:
    name = input("Nome: ")

    if name in data:
        print("Cadastro já existe")
    else:
        data[name] = []
        data[name].append({
            'idade': input("Digite sua idade: "),
            'cidade': input("Cidade onde mora: "),
            'rua': input("Rua onde mora: "),
            'numero': input("Número da casa: "),
            'cep': input("Digite seu CEP: "),
            'sexo': input("Digite seu sexo: "),
            'email': input("Digite seu Email: "),
            'cpf': input("Digite seu CPF: "),
            'estado': input("Estado onde mora: ")
        })

        input()  

def verificarcadastro() -> None:
    if len(data) != 0:
        print(sorted(data))
        name = input("Qual Cadastro deseja ver\n")
        if name in sorted(data):
            for item in data[name]:
                print("Nome: ", name)
                print("Idade :", item['idade'])
                print("Cidade :", item['cidade'])
                print("Rua :", item['rua'])
                print("Numero :", item['numero'])
                print("CEP :", item['cep'])
                print("Sexo :", item['sexo'])
                print("Email :", item['email'])
                print("CPF :", item['cpf'])
                print("Estado :", item['estado'])
                
                input()
        else:
            print("Não existe o cadastro ", name)

            input()
    else:
        print("Não há cadastros salvos")

        input()
    
def excluirCadastro() -> None:
    if len(data) != 0:
        print(sorted(data))
        index = input("Nome do Cadastro que deseja excluir:")
        if index in data:
            del data[index]
            print("Cadastro excluido")
        else:
            print(f"Cadastro {index} não existe")
    else:
        print("Não há cadastros para excluir")

#main
try:
    with open(Path.join(Path.dirname(__file__), "data.json"), "r" ) as loadData:
        data = json.load(loadData)
except Exception as e:
    data = {}
    print(e)

os.system("cls")

while True:
    exibirMenu()
    match input("Ecolha uma opcao:"):
        case "1":
            inserircadastro()
        case "2":
            excluirCadastro()
        case "3":
            verificarcadastro()
        case "4":
            break
        case _:
            print("--------Erro--------")

try:
    with open(Path.join(Path.dirname(__file__), "data.json"),"w") as saveData:
        json.dump(data, saveData)
except Exception as e:
    print(e)
