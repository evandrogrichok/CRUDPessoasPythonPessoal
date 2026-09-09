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
    print ("idade: " + str(idade))
    print ("emails: " + email)

def consultarPessoa():
    posicao = buscarPessoa(input("Digite o nome para consultar: ").lower())

    if posicao >= 0:
        exibirPessoa(nomes[posicao], idades[posicao], emails[posicao])
    else:
        print("Pessoa não encontrada!")

def alterarPessoa():
    posicao = buscarPessoa(input("Digite o nome para consultar: ").lower())

    if posicao >= 0:
        nomes[posicao] = input("Alterar o nome dessa pessoa de " + nomes[posicao] + " para: ")
        idades[posicao] = int(input("Alterar idade dessa pessoa de "+ str(idades[posicao]) + " para: "))
        emails[posicao] = input("Alterar email dessa pessoa de "+ emails[posicao] + " para: ")
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
        alterarPessoa()

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