'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
import requests
import cep_exceptions as cpex

class CepModel(object):

    def __init__(self):
        self.__urlBase = 'http://cep.la/'
        self.__headersJson = {'Accept': 'application/json'}
        self.__headersText = {'Accept': 'text/plain'}

    def request_by_cep(self, cep):
        urlRequest = self.__urlBase + str(cep)
        status = requests.get(urlRequest, headers=self.__headersJson)

        if (not len(status.json())):
            raise cpex.CepDoesNotExist('Cep number {} doesn\'t exist!'.format(str(cep)))
        if (status.status_code != 200):
            raise cpex.BadRequestError('Status code {}: Bad Request Error'.format(status.status_code))
        else:
            return status.json(), status.status_code
