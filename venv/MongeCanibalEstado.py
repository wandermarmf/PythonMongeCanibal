import sys

class MongeCanibalEstado:
    mongeCanibal = None
    estadoAnterior = None
    monges = 0
    canibais = 0
    barco = 0
    barcoMonge = 0
    barcoCanibal = 0

    def __init__(self, mongeCanibal, estadoAnterior, * args):
        self.mongeCanibal = mongeCanibal
        self.estadoAnterior = estadoAnterior
        self.barcoMonge = 0
        self.barcoCanibal = 0

        if self.estadoAnterior is None:
            self.monges = 3
            self.canibais = 3
            self.barco = 1
        else:
            self.monges = self.estadoAnterior.monges
            self.canibais = self.estadoAnterior.canibais
            self.barco = self.estadoAnterior.barco

        if len(args) == 0:
            return

        atravMonges = args[0]
        atravCanibais = args[1]
        atravBarco = args[2]
        #print('criando filho: atravMonges: ' + str(atravMonges) + ' atravCanibais: '+ str(atravCanibais) + ' atravBarco: ' + str(atravBarco))

        if atravBarco == -1:
            self.monges = self.monges - atravMonges
            self.canibais = self.canibais - atravCanibais
        else:
            self.monges = self.monges + atravMonges
            self.canibais = self.canibais + atravCanibais

        self.barcoMonge = atravMonges
        self.barcoCanibal = atravCanibais
        self.barco = atravBarco

    def gera_filhos(self):

        direcaoBarco = self.barco * -1
        print('gera filhos direção: ' + str(direcaoBarco) + ' Monges: ' +str(self.mongesDisponiveis(self.barco)) + \
                   '(' + str(self.monges) + ') Canibais: ' + str(self.canibaisDisponiveis(self.barco)) + '('+ \
                    str(self.canibais)+ ')' )

        if self.mongesDisponiveis(self.barco) == 0:
            countMonge = 1
        elif self.mongesDisponiveis(self.barco) > 2:
            countMonge = 3
        else:
            countMonge = self.mongesDisponiveis(self.barco) + 1

        if self.canibaisDisponiveis(self.barco) == 0:
            countCanibal = 1
        elif self.canibaisDisponiveis(self.barco) > 2:
            countCanibal = 3
        else:
            countCanibal = self.canibaisDisponiveis(self.barco) + 1

        for imonge in range(0, countMonge):

            #print('monges: ' + str(imonge) + ' disp: ' + str(self.mongesDisponiveis(self.barco)))

            if imonge > self.mongesDisponiveis(self.barco):
                break

            for icanibal in range(0, countCanibal):

                #print('canibais: ' + str(icanibal) + ' disp: ' + str(self.canibaisDisponiveis(self.barco)))

                if icanibal > self.canibaisDisponiveis(self.barco):
                    break

                filho = MongeCanibalEstado(self.mongeCanibal, self, imonge, icanibal, direcaoBarco)

                if filho.isValid():
                    print('filho válido Monges: ' + str(filho.barcoMonge) + '(' + str(filho.monges) + ') canibais: ' + \
                          str(filho.barcoCanibal) + '(' + str(filho.canibais) + ') direção: ' + str(filho.barco))
                    self.mongeCanibal.addEstado(filho)

    def getEstadoInicial(self):
        if self.estadoAnterior is None:
            return self
        else:
            return self.estadoAnterior.getEstadoInicial

    def mongesDisponiveis(self, barcoDirecao):
        if barcoDirecao == 1:
            return self.monges
        else:
            return 3 - self.monges

    def canibaisDisponiveis(self, barcoDirecao):
        if barcoDirecao == 1:
            return self.canibais
        else:
            return 3 - self.canibais

    def mongesMargem(self, barcoDirecao):
        if barcoDirecao == 1:
            return self.monges
        else:
            return 3 - self.monges


    def isValid(self):
        if self.mongesDisponiveis(1) > 0 and self.canibaisDisponiveis(1) > self.mongesDisponiveis(1):
            return False

        if self.mongesDisponiveis(-1) > 0 and self.canibaisDisponiveis(-1) > self.mongesDisponiveis(-1):
            return False

        if (not self.barcoMonge + self.barcoCanibal == 2) and (not self.barcoMonge + self.barcoCanibal == 1):
            return False

        if (self.monges == self.mongeCanibal.estadoInicial.monges) and \
           (self.canibais == self.mongeCanibal.estadoInicial.canibais) and \
           (self.barco == self.mongeCanibal.estadoInicial.barco):
            return False



        return True