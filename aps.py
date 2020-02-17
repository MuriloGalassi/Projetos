import os
os.system("cls")
import json
def exibirMenu():
    print("1 - Cadastro")
    print("2 - Excluir Cadastro")
    print("3 - Verificar Cadastro")
    print("4 - Sair")
    opcao = input("Ecolha uma opcao:")
    return opcao
def inserircadastro():
    nome = input("Nome: ")
    if nome in data:
        print("Cadastro já existe")
    else:
        data[nome] = []
        data[nome].append({
            'idade' : input("digite sua idade: "),
            'cidade' : input("cidade aonde mora: "),
            'rua' : input("Rua onde mora: "),
            'numero' : input("numero da casa: "),
            'cep' : input("digite seu cep: "),
            'sexo' : input("digite seu sexo: "),
            'Email' : input("digite seu Email: "),
            'Cpf' : input("digite seu Cpf: "),
            'Estado' : input("Estado aonde mora: "),
         }) 
        brea = input()  
def verificarcadastro():
    i = len(data)
    if i != 0:
        print(sorted(data))
        print("Qual Cadastro deseja ver")
        nome = input()
        if nome in sorted(data):
            for item in data[nome]:
                print("Nome: ", nome)
                print("Idade :", item['idade'])
                print("Cidade :", item['cidade'])
                print("Rua :", item['rua'])
                print("Numero :", item['numero'])
                print("Cep :", item['cep'])
                print("Sexo :", item['sexo'])
                print("Email :", item['Email'])
                print("Cpf :", item['Cpf'])
                print("Estado :", item['Estado'])
                brea = input()
        else:
            print("Não existe o cadastro ",nome)
            brea = input()
    else:
        print("Não há cadastros salvos")
        brea = input()
def excluirCadastro():
    i = len(data)
    if i != 0:
        print(sorted(data))
        indice = input("Nome do Cadastro que deseja excluir:")
        if indice in data:
            del data[indice]
            print("Cadastro excluido")
        else:
            print("Cadastro ",indice," não existe")
    else:
        print("Não há cadastros para excluir")
try:
    with open("data.json", "r" ) as load:
        data = json.load(load)
except Exception:
    data = {}
    i = 0
while True:
    i = len(data)
    opcao = exibirMenu()
    if opcao == "4":
        break
    elif opcao == "3": 
        verificarcadastro()
    elif opcao == "1":
        inserircadastro()
    elif opcao == "2":
        excluirCadastro()
    else:
        print("--------Erro--------")
with open("data.json","w") as cadastrosalvar:
    json.dump(data, cadastrosalvar)


