import csv
import os
from matplotlib import pyplot as plt


dic_info = {}
caminho = ""

def pede_pasta():
    global caminho
    caminho = input("Insira um caminho para a pasta: ")
    os.path.exists(caminho)
    return caminho

def faz_calculos():
    global caminho
    lista = []
    lista1 = []
    lista_ficheiros = os.listdir(caminho)
    global dic_info
    for i in lista_ficheiros:
        if os.path.isfile(os.path.join(caminho,i)):
            lista.append(i.split(".")[1])
            lista1.append((i.split(".")[1], os.path.getsize(os.path.join(caminho,i))/2**10))
            dic_info = {item[0]:{"Quantidade": lista.count(item[0]),"Volume": sum(val for key, val in lista1 if key == item[0])}for item in lista1}
    print(dic_info)
    return dic_info
    

def guarda_resultados():
    global dic_info
    print(f"Os resultados foram guardados no ficheiro {os.path.basename(caminho)}")
    with open(caminho + ".csv", 'w', newline = '') as ficheiro:
        campos = ['Extensão', 'Quantidade', 'Volume']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for key, val in dic_info.items():
            linha = {'Extensão': key}
            linha.update(val)
            writer.writerow(linha)


def faz_grafico_queijos():
    volume = []
    quantidade = []
    lista_chaves = dic_info.keys()
    for key, val in dic_info.items():
        for k in val:
            if k == "Quantidade":
                quantidade.append(val[k])
            if k == "Volume":
                volume.append(val[k])

    plt.pie(quantidade, labels=lista_chaves, autopct='%1.0f%%')
    plt.title("Quantidade")
    plt.show()

    plt.pie(volume, labels=lista_chaves, autopct='%1.0f%%')
    plt.title("Volume")
    plt.show()
    
def faz_grafico_barras():
    volume = []
    quantidade = []
    lista_chaves = dic_info.keys()
    for key, val in dic_info.items():
        for k in val:
            if k == "Quantidade":
                quantidade.append(val[k])
            if k == "Volume":
                volume.append(val[k])
    
    plt.bar(lista_chaves, quantidade)
    plt.title("Quantidade")
    plt.show()

    plt.bar(lista_chaves, volume)
    plt.title("Volume")
    plt.show()
     
        
