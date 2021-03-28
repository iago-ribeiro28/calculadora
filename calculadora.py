import PySimpleGUI as sg

from layout import layout
from eventos import *


# -----EVENTO PRINCIPAL
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
    if evento in ['+', '-', '*', '/', '()']:
        operatores(evento)
    if evento == '=':
        calcular()
    if evento == '.':
        var['decimal'] = True
    if evento == '%':
        atualizar_display(var['result'] / 100.0)

