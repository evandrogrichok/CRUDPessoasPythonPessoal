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


def buscarPessoa(nome):
    i = 0

    while i < len(nomes):
        if nome == nomes[i].lower():   
            return i

        i = i + 1

    return -1

def exibirPessoa(nome, idade, email):
    print("\nOs dados da pessoa são:")

    print ("nome: " + nome)
    print ("idade: " + idade)
    print ("emails: " + email)

def consultarPessoa():
    nomeConsulta = input("Digite o nome para consultar: ").lower()

    posicao = buscarPessoa(nomeConsulta)

    if posicao >= 0:
        exibirPessoa(nomes[posicao], idades[posicao], emails[posicao])
    else:
        print("Pessoa não encontrada!")

 

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
        consultarPessoa()

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