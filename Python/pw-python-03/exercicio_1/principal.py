import analisa_ficheiro
import json

def main():
    f = open(nome.split(".")[0] + "_resultados" + ".txt", "a")
    f.write("linhas " + str(analisa_ficheiro.calcula_linhas(nome))+ "\n")
    f.write("calcula_carateres " + str(analisa_ficheiro.calcula_carateres(nome))+ "\n")
    f.write("calcula_palavra_comprida " + str(calcula_palavra_comprida = analisa_ficheiro.calcula_palavra_comprida(nome))+ "\n")
    f.write("calcula_ocorrencia_de_letras" + str(calcula_ocorrencia_de_letras = analisa_ficheiro.calcula_ocorrencia_de_letras(f))+ "\n")
    f.close()
    analisa_ficheiro.gera_nome(analisa_ficheiro.pede_nome(nome.split(".")[0] + "_resultados" + ".txt"))


if __name__ == "__main__": 
    main("teste.txt")