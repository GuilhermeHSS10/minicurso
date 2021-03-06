# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Description: Dado um numero retorna se ele é par o impar
#  da execução
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
    import matplotlib

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
# Sempre documente o código
# Os comentários servem depois para gerar um HTML da documentação.
# Em geral a documentação do código é gerada pelo pacote Sphinx
#
# Objetivo: pegar o nome passado pelo prompt de comando
#
# ----------------------
def main():

    # recebendo os parametros
    # Se nada foi alterado - vieram os parametros padrao (default)!
    lstArgs = parametros_prompt()

    int_num = lstArgs.num_fornecido
    print_debug = lstArgs.flag_imprimir

    print(":"*80)
    print(" Programa identifica se é par ou ímpar o número fornecido.")
    print(":"*80)

    # Minha funcao que testa se o número é par
    resp = is_par(int_num)

    if resp == True:
        print("O número " + str(int_num) + " é par!")
    else:
        print("O número " + str(int_num) + " é ímpar!")

    if print_debug:
        print("Foi definido que era para imprimir o Debug!")


# ------------------------------------------------------------------------------
#  @ Método que identifica se o número é Par
# ------------------------------------------------------------------------------
def is_par(int_num):
    if (int_num % 2) == 0:
        return True


# ------------------------------------------------------------------------------
#  @@ Inicializa o Escritor de Log
# ------------------------------------------------------------------------------
def parametros_prompt():
  # --------------------------------------------------------------------------
  #  Utiliza o pacote argparse
  #  Recebe os PARAMETROS DE ENTRADA passados pelo usuario na EXECUCAO do
  # --------------------------------------------------------------------------

    """ Objetivo:
        - Capturar os parametros do prompt e retorna-los em uma lista.

    :Date: 10/2016
    :Version: 1.0
    :Authors: @Palin
    :copyright: @Marcelo Palin
    """
##    parser = argparse.ArgumentParser(
##      prog = 'hello_03.py',
##      description = "Minicurso Aprendendo Python - XXVIII SEMAT - Versao 1.0"
##      + " Este programa recebe 2 parametros de entrada no momento da execucao."
##      + " S",
##      epilog = 'Para consultar o Help digite:  python hello_03.py -h '
##      )

    # String em várias linhas utilize ''' ''' para envolver.
    parser = argparse.ArgumentParser(
      prog = 'par_ou_impar.py',
      description = '''Minicurso Aprendendo Python - XXVIII SEMAT - Versao 1.0
        Este programa pode receber os parametros de entrada no momento da execucao.
        Sao eles: um numero inteiro para identificar se ele é par ou ímpar e a flag
        mostrar detalhes (debug).
        \n exemplo de execução:
            $ python par_ou_impar.py -debug 1 -numero 3
        ''',
      epilog = 'Para consultar o Help digite:  python par_ou_impar.py -h '
      )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s vs. 1.0')
    parser.add_argument('-numero', action='store', dest='num_fornecido', type=int, default=0)
    parser.add_argument('-debug', action='store', dest='flag_imprimir', type=int, default=0) #0 = false, 1 = true

    # Retorna a lista de parametros
    lstArgs = parser.parse_args()

    return lstArgs

  ##@fim do metodo
  ##----------------------------------------------------------------------------

# Quando executo o codigo, qual funcao devo chamar primeiro?
if __name__ == '__main__':
    main()
