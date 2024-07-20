class ElementoDaListaSimples:
    def __init__(self, cartao, numCartao):
        self.cartao = cartao
        self.numCartao = numCartao
        self.proximo = None

    def __repr__(self):
        return self.cartao,numCartao

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(nodo.dado)
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cartao == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            nodo_atual = self.head
            while nodo_atual.proximo and nodo_atual.proximo.cartao == "A":
                nodo_atual = nodo_atual.proximo
            nodo.proximo = nodo_atual.proximo
            nodo_atual.proximo = nodo

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            nodo_atual = self.head
            while nodo_atual.proximo:
                nodo_atual = nodo_atual.proximo
            nodo_atual.proximo = nodo

    def inserir(self, cartao, numCartao):
        nodo = ElementoDaListaSimples(cartao, numCartao)
        if not self.head:
            self.head = nodo
        elif cartao == "V":
            self.inserirSemPrioridade(nodo)
        elif cartao == "A":
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        nodo_atual = self.head
        if nodo_atual:
            print(f"Lista -> [{nodo_atual.cartao},{nodo_atual.numCartao}]", end=" ")
            nodo_atual = nodo_atual.proximo
            while nodo_atual:
                print(f"[{nodo_atual.cartao},{nodo_atual.numCartao}]", end=" ")
                nodo_atual = nodo_atual.proximo
        print()

    def atenderPaciente(self):
        if not self.head:
            print("Lista de espera vazia.")
        else:
            paciente = self.head
            self.head = paciente.proximo
            print(f"Atendendo o paciente cartão cor {paciente.cartao} e número {paciente.numCartao}")

Teste = ListaEncadeadaSimples()

while True:
    print('1 - Adicionar paciente a fila.')
    print('2 - Mostrar pacientes na fila.')
    print('3 - Chamar paciente.')
    print('4 - Sair')

    op = int(input('>>'))

    if op == 1:
        cartao = str(input('Informe a cor do cartão (A/V): '))
        numCartao = int(input('Informe o numero do cartão: '))
        Teste.inserir(cartao, numCartao)
    elif op == 2:
        Teste.imprimirListaEspera()
    elif op == 3:
        Teste.atenderPaciente()
    elif op == 4:
        break
