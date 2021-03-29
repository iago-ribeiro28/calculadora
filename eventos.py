from layout import layout
from variavel import *


layout, window = layout()
var, front, back = variavel()


# -----FUNÇÕES AUXILIARES
def formatar_numero() -> float:
    """ Essa função retorna o valor formatado da operação """

    numero_formatado = float(''.join(var['sinal']) + ''.join(front) +
                             '.' + ''.join(back))

    if var['apagar']:
        numero_formatado = numero_formatado // 10

    return numero_formatado


def atualizar_display(display_valor: str):
    """ Essa função é responsável por atualizar o display da calculadora """

    window['_DISPLAY_'].update(value=display_valor)


# -----EVENTOS
def numberos(evento: str):
    """ Essa função serve para decidir se irá jogar o número na variável
        'front' ou se irá jogar na 'back' """

    global var
    if var['decimal']:
        back.append(evento)
    else:
        front.append(evento)
    formatar_numero()
    atualizar_display(formatar_numero())


def limpar():
    """ Limpa as variáveis """

    global var
    front.clear()
    back.clear()
    var['decimal'] = False
    var['sinal'] = ''


def limpar_digito():
    """Limpa o último dígito colocado"""

    global var

    try:
        var['apagar'] = True
        if not var['decimal']:
            front.pop()
        else:
            back.pop()
        formatar_numero()
        var['apagar'] = False

        atualizar_display(formatar_numero())
        formatar_numero()

    except:
        limpar()
        atualizar_display(0.0)
        var['result'] = 0.0


# ------ funções de operação ------
def operatores(evento: str):
    """ Salva o operator"""

    global var
    var['operator'] = evento
    try:
        var['x_val'] = formatar_numero()
    except:
        var['x_val'] = var['result']

    limpar()


def porcentagem():
    global var

    try:

        digito1 = front.pop()
        digito2 = front.pop()

        if digito2 != 0 or digito1 != 0:
            back.append(digito2)
            if digito1 != 0:
                back.append(digito1)

        formatar_numero()
        atualizar_display(formatar_numero())

    except:
        var['result'] = var['result'] / 100

        atualizar_display(var['result'])

    operatores('*')


def mudar_sinal(contador: int):
    global var

    try:
        if contador % 2 == 1:
            var['sinal'] = '-'
        else:
            var['sinal'] = ''

        atualizar_display(formatar_numero())

    except:
        var['result'] = -var['result']

        atualizar_display(var['result'])


# --------- Resultado -------------
def calcular():
    global var

    var['y_val'] = formatar_numero()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        atualizar_display(var['result'])
        limpar()

    except:
        atualizar_display("ERROR!")
        limpar()
