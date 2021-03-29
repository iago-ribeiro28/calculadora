import PySimpleGUI as sg


botao_numeros: dict = {'size': (7, 1), 'font': ('Franklin Gothic Book', 24),
                       'button_color': ("#FFFFFF", "#363636")}
botao_apagar: dict = {'size': (7, 1), 'font': ('Franklin Gothic Book', 24),
                      'button_color': ("#FF8C00", "#363636")}
botao_operacoes: dict = {'size': (7, 1), 'font': ('Franklin Gothic Book', 24),
                         'button_color': ("#00FF00", "#363636")}
botao_igual: dict = {'size': (7, 1), 'font': ('Franklin Gothic Book', 24),
                     'button_color': ("#FFFFFF", "#00FF00"), 'focus': True}


def layout():
    layout: list = [
        [sg.Text('PyDataMath-II', size=(50, 1), justification='right', background_color="#272533",
                 text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
        [sg.Text('0.0', size=(21, 1), justification='right', background_color='black', text_color='red',
                 font=('Digital-7', 48), relief='sunken', key="_DISPLAY_")],
        [sg.Button('C', **botao_apagar), sg.Button('Ce', **botao_operacoes),
         sg.Button('%', **botao_operacoes), sg.Button("/", **botao_operacoes)],
        [sg.Button('7', **botao_numeros), sg.Button('8', **botao_numeros),
         sg.Button('9', **botao_numeros), sg.Button("*", **botao_operacoes)],
        [sg.Button('4', **botao_numeros), sg.Button('5', **botao_numeros),
         sg.Button('6', **botao_numeros), sg.Button("-", **botao_operacoes)],
        [sg.Button('1', **botao_numeros), sg.Button('2', **botao_numeros),
         sg.Button('3', **botao_numeros), sg.Button("+", **botao_operacoes)],
        [sg.Button('+/-', **botao_numeros), sg.Button('0', **botao_numeros),
         sg.Button('.', **botao_numeros), sg.Button('=', **botao_igual, bind_return_key=True)]
    ]

    window: object = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(800, 500),
                               return_keyboard_events=True, resizable=True)
    return layout, window
