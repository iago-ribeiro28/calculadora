def variavel():

    front = []
    back = []
    var: dict = {'sinal': '', 'operator': '', 'x_val': 0.0,
                 'y_val': 0.0, 'result': 0.0, 'decimal': False,
                 'apagar': False, 'porcentagem': False}

    return var, front, back


# -------Significado de cada variável----------------

# front = é uma lista que armazena os números colocados na calculadora,
# O 'front' é responsável peles números antes da vígurla

# back = ele tem a mesma função que o 'front'
# A diferença é que o 'back' se encarrega pelos números depois da vírgula

# 'sinal' usada para mudar o sinal da operação

# 'x_val' é encarregada de armazenar o número depois de colocado a operação

# 'y_val' é encarregado de armazenar o segundo número colocado

# 'result' é o resultado da operação

# 'operator' é responsável por pegar qual operação será realizada
