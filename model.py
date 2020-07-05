'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
import requests
import cep_exceptions as cpex

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
            raise cpex.CepDoesNotExist('Cep number {} doesn\'t exist!'.format(str(cep)))
        if (status.status_code != 200):
            raise cpex.BadRequestError('Status code {}: Bad Request Error'.format(status.status_code))
        else:
            return status.json(), status.status_code
