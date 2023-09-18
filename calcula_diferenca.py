from datetime import date
import doctest


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
        
        >>>data_diferença( ('2023-09-08', '2023-10-20'))
        
    """
    
    d_data_1 = date.fromisoformat(datas[0])
    d_data_2 = date.fromisoformat(datas[1])
    
    diff = d_data_2 - d_data_1
    
    return (abs(diff.days))