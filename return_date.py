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
    date_1_list = [int(date_input_list[0]), date_input_list[2], int(date_input_list[4])]
    date_2_list = [int(date_input_list[6]), date_input_list[8], int(date_input_list[10])]
    
    # Coloca as datas no formato ISO 8601
    date_1_str =  str(date_1_list[2]) + '-' + months_dict[date_1_list[1]] + '-' + str(date_1_list[0])
    date_2_str =  str(date_2_list[2]) + '-' + months_dict[date_2_list[1]] + '-' + str(date_2_list[0])
    
    return (date_1_str, date_2_str)