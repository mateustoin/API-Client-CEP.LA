from controller import CepControl

if __name__ == '__main__':
    control = CepControl()
    control.search_by_cep(input('Insert a brazilian CEP: '))