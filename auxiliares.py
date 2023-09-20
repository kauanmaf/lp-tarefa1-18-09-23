import doctest
from datetime import date

def le_arquivo(txt):
    """
    Parameters
    ----------
    txt : _io.TextIOWrapper
        arquvo de texto contendo as datas.

    Returns
    -------
    data : str
        texto das datas.
        
    -------
    Essa função lê um arquivo de texto contendo as datas e retorna uma string das mesmas
    
    Exemplo de erro:
    
    >>> le_arquivo("nome_aleatorio.txt")
    O arquivo de texto "nome_aleatorio.txt" não foi encontrado!

    """
    
    try:
        with open(txt, 'r') as txt:
            data = txt.read() # lê o conteúdo do arquivo
            
            return data
            
    except:
        print(f'O arquivo de texto "{txt}" não foi encontrado!')

print(le_arquivo("data.csv"))


def return_date(date_input):
    """
    Parameters
    ----------
    string : str
        String contendo as datas

    Returns
    -------
    date_1_str : str
        Data inicial
    date_2_str : str
        Data final
        
    ------
    
    Esta função pega uma string e converte ela no formato ISO 8601 para se calcular a distância entre
    duas datas.
    
    Exemplo:
        
    >>> return_date("12 de dezembro de 1324 - 15 de maio de 2023")
    ('1324-12-12', '2023-05-15')
    
    >>> return_date("1 de janeiro de 2000 - 31 de dezembro de 2000")
    ('2000-01-1', '2000-12-31')
    """
    
    # Transforma o input numa lista de strings
    date_input_list = date_input.split(maxsplit=11)
    
    months_dict = {'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06', 
                   'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}
    
    # Cria duas listas de cada data
    date_1_list = [date_input_list[0], date_input_list[2].lower(), date_input_list[4]]
    date_2_list = [date_input_list[6], date_input_list[8].lower(), date_input_list[10]]
        
    
    # Coloca as datas no formato ISO 8601
    date_1_str =  date_1_list[2] + '-' + months_dict[date_1_list[1]] + '-' + date_1_list[0]
    date_2_str =  date_2_list[2] + '-' + months_dict[date_2_list[1]] + '-' + date_2_list[0]
    
    return (date_1_str, date_2_str)