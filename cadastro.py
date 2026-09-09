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
    print("Os dados da pessoa são:")

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
        
def listarPessoas():
    pos = 0
    while pos < len(nomes):
        print("====== Pessoa de número " + str(pos) + " ======")

        exibirPessoa(nomes[pos], idades[pos], emails[pos])
        pos = pos + 1
        return
    print("Nenhuma pessoa cadastrada.")

def analisarPessoa(nomes, idades, emails):
    procurado = input("Nome para anaisar: ")
    pos = buscarPessoa(procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

        if idade < 12:
            print("Faixa etaria: Criança")
        elif idade < 18:
            print("Faixa etaria: Adolescente")
        elif idade < 30:
            print("Faixa etaria: Adulto Jovem")
        elif idade < 60:
            print("Faixa etaria: Adulto")
        else:
            print("Faixa etaria: Idoso")

        
        if email == "":
            print("Cadastro incompleto: sem e-mail")
        else:
            if "@" not in email:
                print("E-mail invalido")
            else:
                if email.endswith("@gmail.com"):
                    print("Provedor: Gmail")
                elif email.endswith("@outlook.com"):
                    print("Provedor: Outlook")
                elif email.endswith("@hotmail.com"):
                    print("Provedor: Hotmail")
                elif email.endswith("@utfpr.edu.br"):
                    print("Provedor: UTFPR")
                else:
                    print("Provedor: Outro")

        if idade >= 18 and email != "":
            print("Cadastro apto para contato")
        elif idade >= 18 and email == "":
            print("Maior de idade sem contato")
        elif idade < 18 and email != "":
            print("Menor de idade com contato")
        else:
            print("Menor de idade sem contato")


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
        listarPessoas()
    elif op == 5:
        print("Saindo...")
 
    else:
        print("Opcao invalida")
    print("Voltando ao menu...\n")

 
print("Fim do programa")