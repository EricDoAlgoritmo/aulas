nome = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")
while nome == senha:
    print("O nome deve ser diferente da senha!")
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
if nome != senha:
    print("Cadastrado com sucesso!")