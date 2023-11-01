from No_Fila import NoFila

class FilaEncadeada:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.frente is None

    def quantidade(self): 
        return self.tamanho

    def inserir_elemento(self, dado):
        novo_no = NoFila(dado)
        if self.final is None:
            self.frente = self.final = novo_no
        else:
            self.final.proximo = novo_no
            self.final = novo_no
        self.tamanho += 1

    def pesquisar_elemento(self, elemento):
        atual = self.frente
        while atual:
            if atual.dado == elemento:
                return True
            atual = atual.proximo
        return False

    def imprimir_fila(self):
        elementos = []
        atual = self.frente
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos

    def ver_inicio_fila(self):
        if self.esta_vazia():
            return None
        return self.frente.dado

    def ver_fim_fila(self):
        if self.esta_vazia():
            return None
        return self.final.dado

    def remover_elemento(self):
        if self.esta_vazia():
            return None
        dado = self.frente.dado
        self.frente = self.frente.proximo
        if self.frente is None:
            self.final = None
        self.tamanho -= 1
        return dado