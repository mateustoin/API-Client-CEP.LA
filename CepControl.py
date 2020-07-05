'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
from CepModel import CepModel
from CepView import CepView
import cep_exceptions as cpex

class CepControl(object):

    def __init__(self):
        self.model = CepModel()

    def search_by_cep(self, cep):
        """
        Summary: With a brazilian CEP user can retrieve information about that place.

        Args:
            cep ([int] or [str]): Information about brazilian CEP.

        Returns:
            [int]: Returns 1 if the request was successful, 0 if there was any problem.
        """
        try:
            response, code = self.model.request_by_cep(cep)
            CepView.view_by_cep(response)
            return 1
        except cpex.BadRequestError as e:
            CepView.display_bad_request_error(e)
            return 0
        except cpex.CepDoesNotExist as e:
            CepView.display_problem_error(e)
            return 0
        except cpex.CepBadFormat as e:
            CepView.display_problem_error(e)
            return 0

    def search_by_neighborhood(self, uf: str, city: str):
        """
        Summary: With a brazilian uf State and City user can retrieve information about all of the neighborhoods of that city.

        Args:
            uf (str): State of Brazil that you are looking for.
            city (str): City of the State that you put in 'uf'

        Returns:
            [int]: Returns 1 if the request was successful, 0 if there was any problem.
        """
        try:
            response, code = self.model.request_by_neighborhood(uf, city)
            CepView.display_neighborhood(response)
            return 1
        except cpex.UfBadFormat as e:
            CepView.display_problem_error(e)
            return 0
        except cpex.DoesNotExist as e:
            CepView.display_problem_error(e)
            return 0