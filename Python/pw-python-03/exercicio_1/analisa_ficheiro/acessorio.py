import json

def pede_nome (nome):
    verificar = nome.split(".")[1]
    if (verificar == "txt"):
        try:
            f=open(nome, 'r')
            f.close()
            return nome
        except OSError:
            print("Não conseguiu ler o ficheiro")

    else: 
        print ("O ficheiro tem de ser txt")
   
   def gera_nome (nome):
       f=open(nome, 'r')
       texto = f.readlines()
       f.close

       dict content = {}

       for linha in texto:
           key,value = linha.split()
           content[key] = eval(value)
        with open(nome + "json", 'w') as json_file:
        json.dump(content, json_file, indent = 4)
   