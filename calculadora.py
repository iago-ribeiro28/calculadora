from eventos import *


# -----EVENTO PRINCIPAL
contador_de_operadores = 1
contador_de_sinais = 1

while True:
    evento, values = window.read()

    if evento is None:
        break

    if evento in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        numberos(evento)

    if evento in ['Escape:27', 'C']:
        limpar()
        atualizar_display(0.0)
        var['result'] = 0.0

    if evento == 'Ce':
        limpar_digito()

    if evento in ['+', '-', '*', '/']:
        if contador_de_operadores == 1:
            operatores(evento, contador_de_operadores)
        else:
            calcular()
            operatores(evento, contador_de_operadores)
        contador_de_operadores += 1

    if evento == '=':
        calcular()
        contador_de_operadores = 1

    if evento == '.':
        var['decimal'] = True

    if evento == '%':
        porcentagem()

    if evento == '+/-':
        mudar_sinal(contador_de_sinais)
        contador_de_sinais += 1
