
import json

class Generator(object):
    def __init__(self,filter_search):
        self.filter = filter_search


    """
    Essa funcão recebe como parametro o dado que foi carregado da api contendo uma lista de informações
    do ponto pesquisado. os dados são uma lista de dicionarios contendo informações da api do google.
    Retorno da função: dados relevantes para o makoni.
    lista contendo.
        -> latitude, indice [0]
        -> longitude, indice [1]
        -> Nome da cidade, indice [2]
        -> Estado, indice [3]
        -> pais, indice [4]
        -> CEP, indice [5]
    """
    def createMyResponse(self,payload):
        adress_component = []
        geometry = []
        result = []
        for i in payload:
            for k in i:
                if k == 'address_components':
                    adress_component.append(i[k])
                elif k == 'geometry':
                    geometry.append(i[k])
                else:
                    pass

        localization_param_search = self.getLocate(geometry)
        params_adress = self.getAdressComponent(adress_component)
        result.append(localization_param_search)
        result.append(params_adress)

        return self.customizeList(result)
    
    def customizeList(self,result):
        locate = result[0]
        components = result[1]
        exitxx = []
        exitxx.append(locate[0]['lat'])
        exitxx.append(locate[0]['lng'])
        for i in components:
            exitxx.append(i)
        return exitxx

    def getAdressComponent(self,adress_component):
        adress=[]
        for i in adress_component:
            for k in i:
                for j in k:
                    if j == 'long_name':
                        adress.append(k[j])
        
        return adress

    def getLocate(self,geometry):
        locate = []
        for i in geometry:
            for k in i:
                if k == 'location':
                    locate.append(i[k])

        return locate



        
