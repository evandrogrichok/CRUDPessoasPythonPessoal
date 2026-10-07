"""Sistema para realização de CRUD de pessoas."""
# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

from cadastro import CadastroPessoas

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

def cadastrar_pessoa(cadastro):
    """Função para o cadastro de pessoas, adicionando as entradas às variaveis de array para nome, idade e email.""" # pylint: disable=line-too-long
    nome = input("Informe o nome: ")
    idade = input("Informe a idade: ")
    email = input("Informe o email: ")
    cadastro.cadastrar(nome, idade, email)
    if int(idade) >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(pessoa):
    """função para exibir uma pessoa com dados especificados."""
    print("Os dados da pessoa são:")
    print("nome: " + pessoa.getNome)
    print("idade: " + str(pessoa.getIdade))
    print("emails: " + pessoa.getEmail)

def consultar_pessoa(cadastro):
    """Função de consulta para redirecionamento
    do código às funções buscar_pessoa() e exibir_pessoa()"""
    procurado = input("Nome para consultar:")
    pessoa = cadastro.buscarPorNome(procurado)
    if pessoa is None:
        print("Não encontrado.")
    else:
        novo_nome = input("Insira o novo nome: ")
        nova_idade = int(input("Insira o novo nome: "))
        novo_email = input("Insira o novo nome: ")
        cadastro.alterar(procurado,
                        novo_nome,
                        nova_idade,
                        novo_email)
        print("Pessoa alterada!")

        exibir_pessoa(pessoa)
        
def alterar_pessoa(cadastro):
    """Altera os dados de uma pessoa especificada pelo nome."""
    procurado = input("Nome para alterar: ")
    pessoa = cadastro.buscarPorNome(procurado)
    if pessoa is None:
        print("Não encontrado   ")

def listar_pessoas(cadastro):
    """lista todas as pessoas cadastradas no sistema."""
    pessoas = cadastro.listar
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
        return
    for pessoa in pessoas:
        exibir_pessoa(pessoa)
    print("---------------------------------")
    print("Total de cadastros: " + str(len(pessoas)))

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

def analisar_pessoa(cadastro):
    """Realiza uma análise completa de pessoa, de nome, classificação
    etária e condições de contato. Recebe um nome (string)""" # pylint: disable=trailing-whitespace
    procurado = input("Nome para alterar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Não encontrado")
    else:
        classificar_faixa_etaria(pessoa)
        avaliar_email(pessoa.getEmail)
        definir_condicao_de_contato(pessoa.getIdade, pessoa.getEmail)



def executar():

    cadastro = CadastroPessoas()
    op = 0 
    while op != 5:
        op = exibir_menu()
        if op == 1:
            cadastrar_pessoa(cadastro)
        elif op == 2:
            consultar_pessoa(cadastro)
        elif op == 3:
            alterar_pessoa(cadastro)
        elif op == 4:
            listar_pessoas(cadastro)
        elif op == 5:
            print("Saindo...")
        else:
            print("Opcao invalida")
        print("Voltando ao menu...\n")
    print("Fim do programa")

if __name__ == "__main__":
    executar()