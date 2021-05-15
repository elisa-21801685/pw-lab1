class Automovel():
    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo
    
    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return (self.quant_comb * 100) / self.consumo

    def abastece(self, n_litros):
        if n_litros + self.quant_comb > self.cap_dep:
            print("Erro! Quantidade superior ao deposito do carro")
        else:
            self.quant_comb+= n_litros 
        return (self.quant_comb * 100) / self.consumo

    def percorre(self, n_km):
        if n_km > (self.quant_comb * 100) / self.consumo: 
            print("Erro! Distância superior à autonomia do carro")
        else:
            self.quant_comb -= (n_km * self.consumo) / 100
        return (self.quant_comb * 100) / self.consumo

def main():
        x, y, z = input("Introduza o deposito, combustivel e consumo do seu carro: ").split()
        carro = Automovel(int(x), int(y), int(z))
        print("1- Quantidade de combustivel no deposito:")
        print("2- Ver a Autonomia:")
        print("3- Abastecimento do carro:")
        print("4- Percorrer caminho:")

        opcao = ""
        while opcao!= "-1":
            opcao = input("Qual é a opção?")
            if opcao == "1":
                print(carro.combustivel())
            if opcao =="2":
                print(carro.autonomia())
            if opcao == "3":
                litros = int(input("Diga os litros:"))
                print(carro.abastece(litros))
            if opcao == "4":
                km = int(input("Diga os kms:"))
                print(carro.percorre(km))
            


        



if __name__ == "__main__": 
    main()





