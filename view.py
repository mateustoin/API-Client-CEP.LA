'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''

class CepView(object):

    @staticmethod
    def view_by_cep(info_cep):
        print('********Informações do CEP********')
        print('Cep: ' + info_cep["cep"])
        print('UF: ' + info_cep["uf"])
        print('Cidade: ' + info_cep["cidade"])
        print('Bairro: ' + info_cep["bairro"])
        print('Logradouro: ' + info_cep["logradouro"])
        print('**********************************\n')