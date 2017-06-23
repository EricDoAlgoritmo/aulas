usuario = input("Usuario: ")
senha = input("Senha: ")
while usuario == senha:
    print("Sua senha não pode ser igual ao usuario!")
    usuario = input("Usuario: ")
    senha = input("Senha: ")
print("Cadastrado com sucesso!")
