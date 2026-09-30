"""Sistema para realização de CRUD de pessoas."""
# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem


def exibir_menu():
    """Função para exibição do menu, retornando um int para opção escolhida."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrar_pessoa():
    """Função para o cadastro de pessoas, adicionando as entradas às variaveis de array para nome, idade e email.""" # pylint: disable=line-too-long
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

def buscar_pessoa(nome):
    """Função para buscar uma pessoa pelo nome."""
    i = 0
    while i < len(nomes):
        if nome == nomes[i].lower():
            return i
        i = i + 1
    return -1
def exibir_pessoa(nome, idade, email):
    """função para exibir uma pessoa com dados especificados."""
    print("Os dados da pessoa são:")
    print("nome: " + nome)
    print("idade: " + str(idade))
    print("emails: " + email)

def consultar_pessoa():
    """Função de consulta para redirecionamento
    do código às funções buscar_pessoa() e exibir_pessoa()"""
    posicao = buscar_pessoa(input("Digite o nome para consultar: ").lower())
    if posicao >= 0:
        exibir_pessoa(nomes[posicao], idades[posicao], emails[posicao])
    else:
        print("Pessoa não encontrada!")

def alterar_pessoa():
    """Altera os dados de uma pessoa especificada pelo nome."""
    posicao = buscar_pessoa(input("Digite o nome para consultar: ").lower())
    if posicao >= 0:
        nomes[posicao] = input("Alterar o nome de " + nomes[posicao] + " para...: ")
        idades[posicao] = int(input("Alterar idade de "+ str(idades[posicao]) + " para...: "))
        emails[posicao] = input("Alterar email de " + emails[posicao] + " para...: ")
    else:
        print("Pessoa não encontrada!")

def listar_pessoas():
    """lista todas as pessoas cadastradas no sistema."""
    pos = 0
    while pos < len(nomes):
        print("====== Pessoa de número " + str(pos) + " ======")
        exibir_pessoa(nomes[pos], idades[pos], emails[pos])
        pos = pos + 1
        return
    print("Nenhuma pessoa cadastrada.")

def classificar_faixa_etaria(idade):
    """classifica a faixa etária de acordo com a idade informada."""    
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

def avaliar_email(email):
    """avalia a formatação e existência de e-mail no cadastro."""
    if email == "":
        print("Cadastro incompleto: e-mail não registrado.")
        return
    if "@" not in email:
        print("E-mail inválido")
        return
    identificar_provedor(email)

def identificar_provedor(email):
    """identifica o provedor do email com a função built-in endswith"""
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

def definir_condicao_de_contato(idade, email):
    """define a condição de contato de acordo com a idade (int) e email (string)"""
    if idade >= 18:
        if email != "":
            print("Cadastro apto para contato")
        else:
            print("Maior de idade sem contato")
    else:
        if email != "":
            print("Maior de idade sem contato")
        else:
            print("Menor de idade sem contato")

def analisar_pessoa():
    """Realiza uma análise completa de pessoa, de nome, classificação
    etária e condições de contato. Recebe um nome (string)""" # pylint: disable=trailing-whitespace
    procurado = input("Nome para anaisar: ")
    pos = buscar_pessoa(procurado)
    if pos == -1:
        print("Pessoa nao encontrada")
        return
    idade = idades[pos]
    email = emails[pos]
    classificar_faixa_etaria(idade)
    avaliar_email(email)
    definir_condicao_de_contato(idade, email)

nomes = []
idades = []
emails = []
qtd = 0
op = 0
while op != 5:
    op = exibir_menu()
    if op == 1:
        cadastrar_pessoa()
        qtd = qtd + 1
    elif op == 2:
        consultar_pessoa()
    elif op == 3:
        alterar_pessoa()
    elif op == 4:
        listar_pessoas()
    elif op == 5:
        print("Saindo...")
    else:
        print("Opcao invalida")
    print("Voltando ao menu...\n")
print("Fim do programa")
