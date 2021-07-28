def show_menu():
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('1- Inserir dados de n usuários\n')
    print('2- Listar as pessoas cadastradas\n')
    print('3- Apresentar quantidade total dos funcionários\n')
    print('4- Apresentar por genêro MASCULINO o total de funcionários \n')
    print('5- Apresentar por genêro FEMININO o total de funcionários \n')
    print('6- Apresentar MÉDIA da idade sobre o total de funcionários \n')
    print('7- Apresentar MÉDIA  da idade dos HOMENS sobre o total de funcionários \n')
    print('8- Apresentar MÉDIA da idade das MULHERES sobre o total de funcionários \n')
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
def register(user):
    x = 0
    count = int(input('Quantas pessoas gostaria de cadastrar?\n'))

    while x < count:
        nome = str(input('Insira o nome:\n'))
        idade = int(input('Insira a idade:\n'))
        dataNasc = str(input('Insira a data de nascimento:\n'))
        genero = str(input('Insira o gênero (usar M para masculino e F para feminino): \n'))
        user.append((nome, idade, dataNasc, genero))
        x += 1
        if x == count:
            break
def list(user):
    for users in user:
        nome, idade, dataNasc, genero = users
        print(f'Nome: {nome}, idade: {idade}, Data nascimento: {dataNasc}, Gênero: {genero}\n')
        #print(user)
def show_many(user):
    qntdPessoa = len(user)
    print(f'A quantia de pessoas cadastradas na empresa é de: {qntdPessoa}')
def show_byGenderMale(user):
    l = user
    code = [t for t in l if t[3].endswith('M')]
    qntdHomem = len(code)
    media = (qntdHomem/len(l)) * 100
    print(f'Quantia de pessoas que são HOMENS: {qntdHomem}')
    print(f'Quantia em PORCENTAGEM de pessoas na empresa que são HOMENS:{media}%')
def show_byGenderFemale(user):
    l = user
    code = [t for t in l if t[3].endswith('F')]
    qntdMulher = len(code)
    media = (qntdMulher / len(l)) * 100
    print(f'Quantia de pessoas que são MULHERES: {qntdMulher}')
    print(f'Quantia em PORCENTAGEM de pessoas na empresa que são MULHERES:{media}%')
def average_age(user):
    l = user
    tuple = [x[1] for x in l]
    soma = sum(tuple)
    mediaIdade = soma/len(l)
    print(f'A idade média das pessoas dessa empresa é de: {mediaIdade}')
def average_male(user):
    l = user
    code = [t for t in l if t[3].endswith('M')]
    tuple = [x[1] for x in code]
    idadeHomem = sum(tuple)
    mediaHomem = idadeHomem/len(l)
    print(f'A idade média dos HOMENS nessa empresa é de: {mediaHomem}')
def average_female(user):
    l = user
    code = [t for t in l if t[3].endswith('F')]
    tuple = [x[1] for x in code]
    idadeMulher = sum(tuple)
    mediaMulher = idadeMulher/len(l)
    print(f'A idade média das MULHERES nessa empresa é de: {mediaMulher}')
def main():
    user = []

    while True:
        show_menu()
        op = int(input('Escolha alguma das opções acima: \n'))
        if op == 1:
            register(user)
        elif op == 2:
            list(user)
        elif op == 3:
            show_many(user)
        elif op == 4:
            show_byGenderMale(user)
        elif op == 5:
            show_byGenderFemale(user)
        elif op == 6:
            average_age(user)
        elif op == 7:
            average_male(user)
        elif op == 8:
            average_female(user)
        else:
            print('Opção inválida')
main()