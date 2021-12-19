#https://www.youtube.com/watch?v=OMjRxfB33sw
"""para CNPJ

Ditigo verificador 1:

71.425.134/0001-xx
5,4,3,2,9,8,7,6,5,4,3 e 2

(7x5) + (1x4)+(4x3)... + (1x2) = resultado /11

-Se o resto da divisão for menor que 2, o resultado será 0

digito verificador 2:

semelhante ao primeiro mas usa para multiplicar:

10,9,8,7,6,5,4,3,2,1,0

o seu resultado divide por 11 e caso o resto da divisão seja 10 o digito verificador será 0
"""

class Cnpj():
    def __init__(self):
        #self.__NUM_DV1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        #self.__NUM_DV1 = [ 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2] AO INVÉS DISSO: (use o print para conferir)
        self.__NUM_DV1 = list(range(5, 1, -1)) + (list(range(9,1,-1)))
        self.__NUM_DV2 = list(range(6, 1, -1)) + (list(range(9,1,-1)))

    def calcula_digito_verificador(self, cnpj, digito=1):
        pesos = self.__NUM_DV1 if digito ==1 else self.__NUM_DV2
        resultado = (sum(int(digito)* peso for digito,peso in zip(cnpj, pesos))) % 11
        #print(list(zip(cnpj, pesos)))
        return 0 if  resultado < 2 else 11 - resultado

class Cpf():
    def __init__(self):
        #self.__NUM_DV1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        #self.__NUM_DV1 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] AO INVÉS DISSO: (use o print para conferir)
        self.__NUM_DV1 = list(range(10, 0, -1)) + (list(range(9,1,-1)))
        self.__NUM_DV2 = list(range(11, 0, -1)) + (list(range(9,1,-1)))
        pass

    def calcula_digito_verificador(self, cpf, digito=1):
        pesos = self.__NUM_DV1 if digito ==1 else self.__NUM_DV2
        resultado = (sum(int(digito)* peso for digito,peso in zip(cpf, pesos))) # Para sintetizar o calculo use print(list(zip(cpf, pesos)))
        resultado = (resultado * 10) % 11
        return 0 if  resultado == 10 else resultado # Resultado ser menor que 2 ou igual a 10, é a mesma coisa neste contexto

