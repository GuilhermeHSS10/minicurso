# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Description: Exemplo do uso do pacote turtle()
#
# Author:   @Palin
#
# Last Update:  10/2016
# Created:     10/2016
# Copyright:   (c) Ampere Desenvolvimento 2016
#-------------------------------------------------------------------------------

# Sempre importe estes pacotes
import sys
import os
import math

# Tentando importar um pacote que PODE não estar instalado!
# Receita de Bolo! Use sempre o Try/Except
# Isso salva a vida do programador!
try:

    # SOMENTE MUDE AQUI! - Coloque quantos pacotes quiser importar
    import argparse
    import turtle

except ImportError as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'lineno': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__
    }
    print("#" * 80)
    print("# Descrição do Erro: " + str(e))
    print(traceback_details)
    print("#" * 80)
    sys.exit()



# ----------------------
# Fonte:
# https://panda.ime.usp.br/pensepy/static/pensepy/03-PythonTurtle/olatartaruga.html
# ----------------------
def main():

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")         # define a cor de fundo da janela

    tess = turtle.Turtle()
    tess.color("blue")               # tess fica azul
    tess.pensize(3)                  # define a espessura da caneta

    tess.forward(50)
    tess.left(120)
    tess.forward(50)

    wn.exitonclick()

if __name__ == '__main__':
    main()




