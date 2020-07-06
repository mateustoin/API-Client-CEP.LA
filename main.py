from CepControl import CepControl

if __name__ == '__main__':
    control = CepControl()
    #control.search_by_cep(input('Insira um CEP: '))
    control.search_by_neighborhood(uf='pe', city='recife')