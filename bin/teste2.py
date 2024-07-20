class Estado:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.tabela = [None] * self.tamanho

    def inserir(self, estado):
        posicao = self.funcaoHash(estado.sigla)
        if self.tabela[posicao] is None:
            self.tabela[posicao] = estado
        else:
            estado.proximo = self.tabela[posicao]
            self.tabela[posicao] = estado

    def imprimir(self):
        for i, estado in enumerate(self.tabela):
            print(f"{i}: ", end="")
            while estado:
                print(f"{estado.sigla}", end=" -> ")
                estado = estado.proximo
            print("None")

    def funcaoHash(self, sigla):
        if sigla == "DF":
            return 7
        char1, char2 = ord(sigla[0]), ord(sigla[1])
        return (char1 + char2) % self.tamanho


tabelaDeEstados = TabelaHash()

#Exigência 1/3
tabelaDeEstados.imprimir()
print()

#Exigência 2/3
estados = [
    Estado("AC", "ACRE"), Estado("AL", "ALAGOAS"), Estado("AP", "AMAPÁ"), Estado("AM", "AMAZONAS"), Estado("BA", "BAHIA"), Estado("CE", "CEARÁ"),
    Estado("DF", "DISTRITO FEDERAL"), Estado("ES", "ESPÍRITO SANTO"), Estado("GO", "GOIÁS"), Estado("MA", "MARANHÃO"), Estado("MT", "MATO GROSSO"), Estado("MS", "MATO GROSSO DO SUL"),
    Estado("MG", "MINAS GERAIS"), Estado("PA", "PARÁ"), Estado("PB", "PARAÍBA"), Estado("PR", "PARANÁ"), Estado("PE", "PERNAMBUCO"), Estado("PI", "PIAUÍ"),
    Estado("RJ", "RIO DE JANEIRO"), Estado("RN", "RIO GRANDE DO NORTE"), Estado("RS", "RIO GRANDE DO SUL"), Estado("RO", "RONDÔNIA"), Estado("RR", "RORAIMA"), Estado("SC", "SANTA CATARINA"),
    Estado("SP", "SÃO PAULO"), Estado("SE", "SERGIPE"), Estado("TO", "TOCANTINS")]

for estado in estados:
    tabelaDeEstados.inserir(estado)

tabelaDeEstados.imprimir()
print()

#Exigência 3/3
novoEstado = Estado("RT", "RONNEY TORRES")
tabelaDeEstados.inserir(novoEstado)

tabelaDeEstados.imprimir()
print()