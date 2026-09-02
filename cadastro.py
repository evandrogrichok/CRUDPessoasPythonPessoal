# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

def exibirMenu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrarPessoa(nomes, idades, emails):
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = input("Informe a idade: ")
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if int(idade) >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade") 

 
nome1 = ""
idade1 = 0
email1 = ""
nome2 = ""
idade2 = 0
email2 = ""
nome3 = ""
idade3 = 0
email3 = ""

nomes = []
idades = []
emails = []
 
qtd = 0
op = 0
 
while op != 5:

    op = exibirMenu()

    if op == 1:
        cadastrarPessoa(nomes, idades, emails)
        qtd = qtd + 1

    elif op == 2:
        nomeConsulta = input("Digite o nome para consultar: ").lower()
        achou = False
        i = 0
        while i < len(nomes):
            if nomeConsulta == nomes[i].lower():
                print ("nome: " + nomes[i])
                print ("idade: " + idades[i])
                print ("emails: " + emails[i])
                achou = True
                break
            i = i + 1

        if achou == False:
            print("Pessoa não encontrada!")

    elif op == 3:
        nomeConsulta = input("Digite o nome para consultar: ").lower()
        achou = False
        i = 0
        while i < len(nomes):
            if nomeConsulta == nomes[i].lower():
                nomes[i] = input("Alterar o nome dessa pessoa de " + nomes[i] + " para: ")
                idades[i] = int(input("Alterar idade dessa pessoa de "+ str(idades[i]) + " para: "))
                emails[i] = input("Alterar email dessa pessoa de "+ emails[i] + " para: ")
                achou = True
                break
            i = i + 1

        if achou == False:
            print("Pessoa não encontrada!")


    elif op == 4:
        pos = 0
        while pos < len(nomes):
            print ("nome: " + nomes[pos])
            print ("idade: " + idades[pos])
            print ("emails: " + emails[pos])
            pos = pos + 1
    elif op == 5:
        print("Saindo...")
 
    else:
        print("Opcao invalida")
    print("Voltando ao menu...\n")

 
print("Fim do programa")