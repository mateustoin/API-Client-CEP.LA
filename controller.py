'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
from model import CepModel
from view import CepView
import cep_exceptions as cpex

class CepControl(object):

    def __init__(self):
        self.model = CepModel()

    def search_by_cep(self, cep):
        try:
            response, code = self.model.request_by_cep(cep)
            CepView.view_by_cep(response)
        except cpex.BadRequestError as e:
            CepView.display_bad_request_error(e)
        except cpex.CepDoesNotExist as e:
            CepView.display_wrong_cep_error(e)
            tentative = input('Want to try other CEP? [y/n]')
            if tentative == 'y':
                self.search_by_cep(input('Insert other CEP: '))
            else:
                pass

if __name__ == '__main__':
    control = CepControl()
    control.search_by_cep(51052284)