'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
import requests
import cep_exceptions as cpex
import string

class CepModel(object):

    def __init__(self):
        """
        Constructor method

        Summary: Specifying the base URL to do GET Requests to the API CEP.LA
                 Also storing the basic headers, for JSON data and Text data.
        """
        self.__urlBase = 'http://cep.la/'
        self.__headersJson = {'Accept': 'application/json'}
        self.__headersText = {'Accept': 'text/plain'}

    def request_by_cep(self, cep):
        """
        Summary: Make request to cep.la API and retrieve information about
                 UF, City, Neighborhood and Street.

        Args:
            cep ([str] or [int]): Information about brazilian CEP (can be written with dots and hyphen).

        Raises:
            cpex.CepBadFormat: Raise Bad Format if the CEP is written wrong.
            cpex.CepDoesNotExist: Raise if the API return nothing.
            cpex.BadRequestError: Raise if the response from the API is different than 200, which means good request. 

        Returns:
            [json, int]: Returns JSON response from the API with the CEP informations and the status code from the requisition.
        """
        # Treating CEP if it's written with dot and/or hyphen
        cep = str(cep)
        cep = cep.replace(".", "")
        cep = cep.replace("-", "")

        # CEP must have 8 numbers, brazilian pattern
        if (len(cep) != 8):
            raise cpex.CepBadFormat('Cep Bad Format Error, must have 8 numbers!')

        # Requisition of the API with Json return format
        urlRequest = self.__urlBase + cep
        status = requests.get(urlRequest, headers=self.__headersJson)

        # Verifying if it was a good requisition and if the CEP returns something
        if (not len(status.json())):
            raise cpex.DoesNotExist('Cep number {} doesn\'t exist!'.format(str(cep)))
        if (status.status_code != 200):
            raise cpex.BadRequestError('Status code {}: Bad Request Error'.format(status.status_code))
        else:
            return status.json(), status.status_code


    def request_by_neighborhood(self, uf: str, city: str):
        # Requisition of the API with Json return format
        if (len(uf) != 2):
            raise cpex.UfBadFormat('UF Bad Format Error. Must have 2 characters.')
        
        # Help user to put city and uf in a good format
        city = string.capwords(city)
        city = city.replace(" ", "-")
        uf = uf.upper()

        urlRequest = self.__urlBase + uf + '/' + city
        status = requests.get(urlRequest, headers=self.__headersJson)

        if (not len(status.json()) or (len(status.json()[0]) > 2)):
            raise cpex.DoesNotExist('The City or UF that you are looking for doesn\'t correspond to the search about neighborhoods. Try a different format.')
        
        list_response = status.json()
        pag = 2
        while (len(status.json()) != 0):
            status = requests.get(urlRequest + '/' + str(pag), headers=self.__headersJson)
            list_response += (status.json())
            pag += 1
        
        # Removing the first element of the list, that is useless
        list_response = list_response[1:]
        
        return list_response, status.status_code