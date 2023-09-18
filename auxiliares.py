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
    
    Esta função auxiliar pega uma string e converte ela no formato ISO 8601 para se calcular a distância entre
    duas datas.
    """
    
    # Transforma o input numa lista de strings
    date_input_list = date_input.split(maxsplit=11)
    
    months_dict = {'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04', 'Maio': '05', 'Junho': '06', 
                   'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'}
    
    # Cria duas listas de cada data
    date_1_list = [date_input_list[0], date_input_list[2], date_input_list[4]]
    date_2_list = [date_input_list[6], date_input_list[8], date_input_list[10]]
    
    # Coloca as datas no formato ISO 8601
    date_1_str =  date_1_list[2] + '-' + months_dict[date_1_list[1]] + '-' + date_1_list[0]
    date_2_str =  date_2_list[2] + '-' + months_dict[date_2_list[1]] + '-' + date_2_list[0]
    
    return (date_1_str, date_2_str)


def data_diferenca(datas):
    """
    Parameters
    ----------
    (datas) : string tuple
        Datas inicial e final

    Returns
    -------
    TYPE: int
        Diferença das datas

    -------
    
    Esta função calcula a diferença entre duas datas dadas como tuplas
    no formato ISO 8601 (YYYY-MM-DD)
    
    Exemplos:
        
        >>> data_diferenca(('2023-09-08', '2023-10-20'))
        42
        
    """
    
    d_data_1 = date.fromisoformat(datas[0])
    d_data_2 = date.fromisoformat(datas[1])
    
    diff = d_data_2 - d_data_1
    
    return (abs(diff.days))