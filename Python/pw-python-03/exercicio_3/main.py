import os

def pede_pasta():
    caminho = input("Insira um caminho para a pasta: ")
    while os.path.exists(caminho) == False:
        caminho = input("Insira um caminho para a pasta: ")
    return caminho

def calcula_tamanho_pasta(pasta):
    soma = 0
    lista = os.listdir(pasta)
    for i in lista:
        if os.path.isfile(os.path.join(pasta,i)):
            soma += os.path.getsize(os.path.join(pasta,i))/ 2**10
        if os.path.isdir(os.path.join(pasta,i)): 
            soma += calcula_tamanho_pasta(os.path.join(pasta,i)) 
    return soma

def main():
    print(calcula_tamanho_pasta(pede_pasta()))


if __name__ == "__main__": 
    main()
