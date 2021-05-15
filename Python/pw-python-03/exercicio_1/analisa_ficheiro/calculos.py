def calcula_linhas (nome):
     f=open(nome, 'r') 
     linhas = f.readlines()
     f.close()
     return len(linhas)

def calcula_carateres (nome):
    f=open(nome, 'r') 
    linha = f.read().replace(" ", "").replace("\n", "")
    

    count = 0
    for i in linha:
        count= count + 1
    f.close()
    return count


def calcula_palavra_comprida(nome):
    with open(nome, 'r') as infile:
              palavras = infile.read().split()
    max_len = len(max(palavras, key=len))
    return [palavra for palavra in palavras if len(palavra) == max_len]


def calcula_ocorrencia_de_letras(nome):
    all_freq = {}
    f=open(nome, 'r') 
    ocorrencia = f.read().replace(" ","").replace("\n","").lower()
    res = {}

    for keys in ocorrencia:
        res[keys] = res.get(keys,0) + 1
    f.close()
    return str(res).replace(" ","")



     


