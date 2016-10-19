# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Description: Hello World!
#  - vs 3 - Facilitando a execução do código passando parâmetros no momento
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

    str_nome = lstArgs.str_recebe_nome
    print_debug = lstArgs.flag_imprimir
    dbl_raio = lstArgs.dbl_raio

    print("Olá " + str_nome + ", seja bem-vindo!")

    print("Dado o raio " + str(dbl_raio) + " o comprimento da circunferência = " + str(2*math.pi))
    print("Dado o raio " + str(dbl_raio) + " a área da circunferência = " + str(math.pi * dbl_raio**2 ))

    if print_debug:
        print("Foi definido que era para imprimir o Debug!")


##------------------------------------------------------------------------------
## @@ Inicializa o Escritor de Log
##------------------------------------------------------------------------------
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
      prog = 'hello_03.py',
      description = '''Minicurso Aprendendo Python - XXVIII SEMAT - Versao 1.0
        Este programa recebe 3 parametros de entrada no momento da execucao.
        Sao eles: O Nome da pessoa, o raio de uma circunferencia e a flag
        mostrar detalhes (debug).
        \n exemplo de execução:
            $ python hello_03.py -debug 1 -raio 2 -nome "Marcelo Palin"
        ''',
      epilog = 'Para consultar o Help digite:  python hello_03.py -h '
      )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s vs. 1.0')
    parser.add_argument('-raio', action='store', dest='dbl_raio', type=float, default=1.0)
    parser.add_argument('-debug', action='store', dest='flag_imprimir', type=int, default=0) #0 = false, 1 = true
    parser.add_argument('-nome', action='store', dest='str_recebe_nome', default="Palin" )

    # Pega a lista de parametros passada no prompt de comando e armazena em uma lista
    # Ex de execucao: python hello_03 -debug 0 -nome "Marcelo Palin"
    lstArgs = parser.parse_args()

    return lstArgs

  ##@fim do metodo
  ##----------------------------------------------------------------------------

# Quando executo o codigo, qual funcao devo chamar primeiro?
if __name__ == '__main__':
    main()
