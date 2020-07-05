'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
from model import CepModel
from view import CepView

class CepControl(object):

    def __init__(self):
        self.model = CepModel()

    def search_by_cep(self, cep):
        response, code = self.model.request_by_cep(cep)
        CepView.view_by_cep(response)
   
if __name__ == '__main__':
    control = CepControl()
    control.search_by_cep('58052284')