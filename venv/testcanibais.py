#!/usr/bin/python
import unittest

MONGES = 0
CANIBAIS = 1
BARCO = 2


def estado_valido(estado):
    ret = True
    cestado = [3 - estado[MONGES], 3 - estado[CANIBAIS]]
    if estado[MONGES] < 0 or estado[MONGES] > 3:    ret = False
    if estado[CANIBAIS] < 0 or estado[CANIBAIS] > 3:  ret = False
    if cestado[MONGES] < 0 or cestado[MONGES] > 3:   ret = False
    if cestado[CANIBAIS] < 0 or cestado[CANIBAIS] > 3: ret = False
    if estado[MONGES] != 0 and estado[MONGES] < estado[CANIBAIS]:  ret = False
    if cestado[MONGES] != 0 and cestado[MONGES] < cestado[CANIBAIS]: ret = False

    return ret


def gera_filhos(estado):
    ret = []
    # 1 monge
    m1 = [estado[MONGES] - estado[BARCO], estado[CANIBAIS], estado[BARCO] * -1]
    if estado_valido(m1):
        ret.append(m1)

    # 2 monges
    m2 = [estado[MONGES] - 2 * estado[BARCO], estado[CANIBAIS], estado[BARCO] * -1]
    if estado_valido(m2):
        ret.append(m2)

    # 1 canibal
    c1 = [estado[MONGES], estado[CANIBAIS] - estado[BARCO], estado[BARCO] * -1]
    if estado_valido(c1):
        ret.append(c1)

    # 2 canibais
    c2 = [estado[MONGES], estado[CANIBAIS] - 2 * estado[BARCO], estado[BARCO] * -1]
    if estado_valido(c2):
        ret.append(c2)

    # 1 monge 1 canibal
    m1c1 = [estado[MONGES] - estado[BARCO], estado[CANIBAIS] - estado[BARCO], estado[BARCO] * -1]
    if estado_valido(m1c1):
        ret.append(m1c1)

    return ret


def vstr(v):
    return "%d %d %d" % (v[0], v[1], v[2])


def bfs(inicial, final):
    lista = [inicial]
    visitados = []
    hpais = dict()
    while (len(lista) > 0):
        pai = lista[0]
        del lista[0]
        if pai not in visitados:
            visitados.append(pai)
            filhos = gera_filhos(pai)
            for filho in filhos:
                chave_filho = vstr(filho)
                if chave_filho not in hpais:
                    hpais[chave_filho] = vstr(pai)
                    lista.append(filho)
                    print
                    pai, filho
                    if filho == final:
                        break
    sestado = vstr(final)
    while sestado != vstr(inicial):
        print
        sestado
        sestado = hpais[sestado]
    print
    sestado


class test_monges(unittest.TestCase):
    def test_gera_filhos(self):
        v = []
        v.append([[2, 2, 1], [[0, 2, -1], [1, 1, -1]]])
        v.append([[3, 2, 1], [[3, 0, -1], [2, 2, -1], [3, 1, -1]]])
        v.append([[3, 3, 1], [[3, 1, -1], [2, 2, -1], [3, 2, -1]]])
        v.append([[3, 1, 1], [[1, 1, -1], [3, 0, -1]]])
        v.append([[0, 3, 1], [[0, 1, -1], [0, 2, -1]]])
        v.append([[0, 2, 1], [[0, 0, -1], [0, 1, -1]]])
        for vtest in v:
            pai = vtest[0]
            filhos = vtest[1]
            gfilhos = gera_filhos(pai)
            for filho in gfilhos:
                self.assertTrue(filho in filhos)
            for filho in filhos:
                self.assertTrue(filho in gfilhos)

    def test_bfs(self):
        bfs([3, 3, 1], [0, 0, -1])


if __name__ == '__main__':
    unittest.main()


