import PySimpleGUI as Sg
from layout import layout
from variavel import *
layout = layout()


window: object = Sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(800, 500),
                           return_keyboard_events=True, resizable=True)

var = variavel()


# -----FUNÇÕES AUXILIARES
def formatar_numero() -> float:
    """ Essa função retorna o valor formatado da operação """
    return float(''.join(var['front']) + '.' + ''.join(var['back']))


def atualizar_display(display_valor: str):
    """ Essa função é responsável por atualizar o display da calculadora """
    try:
        window['_DISPLAY_'].update(value=f'{display_valor}')

    except:
        window['_DISPLAY_'].update(value=display_valor)


# -----EVENTOS
def numberos(evento: str):
    """ Essa função serve para decidir se irá jogar o número na variável
        'front' ou se irá jogar na 'back' """
    global var
    if var['decimal']:
        var['back'].append(evento)
    else:
        var['front'].append(evento)
    atualizar_display(formatar_numero())


def limpar():
    """ Limpa as variáveis """
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False


def operatores(evento: str):
    """ Salva o operator"""
    global var
    var['operator'] = evento
    try:
        var['x_val'] = formatar_numero()
    except:
        var['x_val'] = var['result']
    limpar()
    return evento


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
