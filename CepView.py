'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''

class CepView(object):

    @staticmethod
    def view_by_cep(info_cep):
        print('\n*************Informações do CEP*************')
        print('Cep: ' + info_cep["cep"])
        print('UF: ' + info_cep["uf"])
        print('Cidade: ' + info_cep["cidade"])
        print('Bairro: ' + info_cep["bairro"])
        print('Logradouro: ' + info_cep["logradouro"])
        print('********************************************\n')

    @staticmethod
    def display_bad_request_error(error):
        """
        Summary: Display error about bad requests from the API.

        Args:
            error ([exception]): Contains the error string made in CepModel.
        """
        print('\n********************************************')
        print(error.args[0])
        print('Try again later!')
        print('********************************************')

    @staticmethod
    def display_problem_error(error):
        """
        Summary: Display error about bad format or if anything is wrong.

        Args:
            error ([exception]): Contains the error string made in CepModel
        """

        print('\n********************************************')
        print(error.args[0])
        print('********************************************')

    @staticmethod
    def display_neighborhood(info_city):
        print('\n*************Bairros da Cidade*************')
        for item in info_city:
            print('Bairro: {}'.format(item["nome"]))
        print('********************************************\n')