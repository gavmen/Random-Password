import random
senha = []
while len(senha) < 20:
    char = chr(random.randint(48, 122))
    senha.append(char)
senhastr = ''.join(senha)
print(senhastr)
