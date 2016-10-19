# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Description: Dado uma Função Contínua e definida no intervalo [a,b] encontra
# a raiz (f(x)=0) utilizando o método da Bissecção (Teorema de Bolzano)
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
    import numpy
    import logging

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
# Funcao que sera calculada
# ----------------------
def f(x):
    y = x - math.cos(x)
    return y



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

    # --------------------------------------------------------------------------
    #  Cria um arquivo de Log que serao impressas
    #  Mensagens de Debug
    ##--------------------------------------------------------------------------
    strFileName_Log = dic_param_valor['arq_log'] ## Lido Nome do Arquivo no XML
    logger = init_log(strFileName_Log)
    if printDebug == 1:
      logger.info(" **** Rodando Check VE ****")

    strDirEntrada = "Entrada"
    strDirSaida = "Saida"
    init_dirs(strDirEntrada, strDirSaida)


    int_num = lstArgs.num_fornecido
    print_debug = lstArgs.flag_imprimir

    if print_debug:
        print(":"*80)
        print(" Calcula a raiz da função x - cos(x) no intervalo [0,1.5]:")
        print(":"*80)

        print("Finding roots of this equation by bisection method")
        print('f(2) is -ve and f(3) is +ve so root lies between 2 and 3')
        l = 1.5
        m = 3.0

        for i in range(1,20):
            k = 1.0/2.*(l+m)
            if(f(k)<0):
                l = k
            else:
                m = k
        print("The root is: ", k)


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

    # String em várias linhas utilize ''' ''' para envolver.
    parser = argparse.ArgumentParser(
      prog = 'met_bissec.py',
      description = '''Minicurso Aprendendo Python - XXVIII SEMAT - Versao 1.0

        Parâmetros de Entrada: Intervalo [a,b] e função a ser avaliada.

        \n Ex: $python met_bissec.py -a 0 -b 1.5 -func "x - math.cos(x)"

        Este programa também pode receber o parametro (debug). Caso deseje que detalhes
        das informações sejam impressas na tela.

        ''',
      epilog = 'Para consultar o Help digite:  python met_bissec.py -h '
      )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s vs. 1.0')
    parser.add_argument('-debug', action='store', dest='flag_imprimir', type=int, default=0) #0 = false, 1 = true
    parser.add_argument('-a', action='store', dest='dbl_a', type=float, default=0) # Inicio do Intervalo [a,b]
    parser.add_argument('-b', action='store', dest='dbl_b', type=float, default=0) # Final do Intervalo [a,b]
    parser.add_argument('-func', action='store', dest='str_func', type=string, default="x**") # Funcao

    # Retorna a lista de parametros
    lstArgs = parser.parse_args()

    return lstArgs

  ##@fim do metodo
  ##----------------------------------------------------------------------------


##------------------------------------------------------------------------------
## @@ Inicializa o Escritor de Log
##------------------------------------------------------------------------------
def init_log(strLogFileName):
  logger = logging.getLogger("bissec")
  logger.setLevel(logging.INFO)
  fh = logging.FileHandler(strLogFileName)
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  fh.setFormatter(formatter)
  logger.addHandler(fh)
  logger.info("Iniciando o Projeto")
  return logger
  ##Exemplo de como usar o Log
  ##  logger.debug('debug message')
  ##  logger.info('info message')
  ##  logger.warn('warn message')
  ##  logger.error('error message')
  ##  logger.critical('critical message')
  ##  logging.debug('This message should go to the log file')
  ##  logging.info('So should this')
  ##  logging.warning('And this, too')
  ##@fim do metodo
  ##----------------------------------------------------------------------------

# Quando executo o codigo, qual funcao devo chamar primeiro?
if __name__ == '__main__':
    main()
