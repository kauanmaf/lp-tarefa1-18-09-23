import auxiliares as aux
import calcula_diferenca as cd
import doctest
from datetime import date

if __name__ == '__main__':
    doctest.testmod(aux)
    doctest.testmod(cd)

def input():
    nome = input("Digite o nome do arquivo: ")

    if ".txt" in nome:
        data = aux.le_arquivo(nome) # caso de arquivo
    else:
        data = nome # caso de input
        
    data_convertida = aux.return_date(data) # data no formato ("YYYY - MM - DD", "YYYY - MM - DD")

    dias = cd.data_diferenca(data_convertida) # número de dias entre as duas datas

    print()
    print(f"O número de dias entre as datas mencionadas é {dias}.")

    return dias
