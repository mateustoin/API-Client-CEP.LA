'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
import requests

class CepModel(object):

    def __init__(self):
        self.__urlBase = 'http://cep.la/'
        self.__headersJson = {'Accept': 'application/json'}
        self.__headersText = {'Accept': 'text/plain'}

    def request_by_cep(self, cep):
        urlRequest = self.__urlBase + cep
        status = requests.get(urlRequest, headers=self.__headersJson)
        return status.json(), status.status_code
