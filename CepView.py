'''
    Creado em 04 de Julho de 2020

    @author: mateustoin
'''
from rich.console import Console
from rich.table import Column, Table

console = Console()

class CepView(object):

    @staticmethod
    def view_by_cep(info_cep):
        table = Table(show_header=True, header_style="black on green")
        table.add_column("", justify="center", style="dim")
        table.add_column("Informações do CEP", justify="left")
        table.add_row('CEP:', info_cep["cep"], style='green')
        table.add_row('UF:', info_cep["uf"], style='green')
        table.add_row('Cidade:', info_cep["cidade"], style='green')
        table.add_row('Bairro:', info_cep["bairro"], style='green')
        table.add_row('Logradouro:', info_cep["logradouro"], style='green')
        console.print(table)

    @staticmethod
    def display_bad_request_error(error):
        """
        Summary: Display error about bad requests from the API.

        Args:
            error ([exception]): Contains the error string made in CepModel.
        """
        print('\n********************************************')
        console.print(error.args[0], style='red on white')
        console.print('Try again later!', style='red on white')
        #print('********************************************')

    @staticmethod
    def display_problem_error(error):
        """
        Summary: Display error about bad format or if anything is wrong.

        Args:
            error ([exception]): Contains the error string made in CepModel
        """

        #print('\n********************************************')
        console.print(error.args[0], style='white on red')
        #print('********************************************')

    @staticmethod
    def display_neighborhood(info_city):
        table = Table(show_header=True, header_style="black on green")
        table.add_column("Bairros da cidade", justify="center")
        for item in info_city:
            table.add_row(item["nome"], style='green')
        console.print(table)