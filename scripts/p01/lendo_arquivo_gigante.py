# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Description: Leitura de um arquivo de dados gigante, que nenhum editor consegue
# ler.
# Estratégia: abrir o arquivo e ler linha a linha
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



# METODO CONTA NUM DE LINHAS
def blocks(files, size=65536):
  while True:
    b = files.read(size)
    if not b: break
    yield b


# ----------------------
# Sempre documente o código
# Os comentários servem depois para gerar um HTML da documentação.
# Em geral a documentação do código é gerada pelo pacote Sphinx
#
# Objetivo: Leitura de um Arquivo Gigante
#
# ----------------------
def main():

    # recebendo os parametros
    # Se nada foi alterado - vieram os parametros padrao (default)!
    lstArgs = parametros_prompt()

    # Nome do Arquivo
    strFileName = lstArgs.str_recebe_nome
    print_debug = lstArgs.flag_imprimir
    extensaoFile = "txt"

    ## LISTA DE ARQUIVOS
    lstPathAndFiles = getList_NomeArq_E_Path("Entrada",extensaoFile)

    intCount = 1
    ##@@@@@
    ##@ (2.0)
    ##@ - LOOP DE INTERPRETACAO DE CADA ARQUIVO
    #######################################################################
    farqJaProc = open("Arq_Processados.log", "w")
    for i in xrange(0,len(lstPathAndFiles)):

      strFileName = lstPathAndFiles[i][0] ##Dir + Nome
      strDirAndFileName = lstPathAndFiles[i][1]## Apenas Nome

      # Se o arquivo tem a extensao .txt
      if(strFileName.find(extensaoFile) != -1): ##Encontrou a Extensao HTM

          # tem a palavra file
          if (strFileName.find("file") != -1):
            with open(strDirAndFileName, "r") as f:
                nTotalLinhas =  sum(bl.count("\n") for bl in blocks(f))
            print( "O N. Total de Linhas do ARQUIVO " + strFileName + ": " + str(nTotalLinhas))


##------------------------------------------------------------------------------
## METODO - EXTRAI CONTEUDO DE ARQUIVO - DADO EXPRESSAO REGULAR
##------------------------------------------------------------------------------
## http://stackoverflow.com/questions/7098530/repeatedly-extract-a-line-between-two-delimiters-in-a-text-file-python
def getBlockText_From_String(strTexto, strSubDir, strExpressRegular, strFileSaida, printDebug = False):
  for strConteudo in re.findall(strExpressRegular, strTexto, re.S):
    strBloco = strConteudo
    if printDebug == 1:
      try:
        f = open(os.getcwd() + '/' + strSubDir + '/' + strFileSaida, "w")
        try:
          f.writelines(strConteudo)
        finally:
          f.close()
      except IOError:
        pass

    return strBloco
##------------------------------------------------------------------------------


########################################################
## METODO : varre o diretorio dado (path)
## e retorna uma lista com todos os NOMES DE ARQUIVOS
## E TAMBEM (path+filename.extensao)
##    """
##    EXEMPLO de CHAMADA desse METODO
##    lstPathAndFiles = getList_NomeArq_E_Path(os.getcwd(),extensao)
########################################################
def getList_NomeArq_E_Path(path,extensao):
    """
    Essa funcao retorna a lista de Arquivos e Caminho
    dos arquivos de uma dada extensao
    """
    lstFileName_DirAndFileName = []
    #conta o numero de arquivos na pasta
    for raiz, diretorios, arquivos in os.walk(os.getcwd()):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                row = []
                ##Guarda o Nome do Arquivo
                row.append(arquivo)
                ##Nome do Arquivo e Diretorio
                row.append(os.path.join(raiz, arquivo))
                lstFileName_DirAndFileName.append(row)

    return lstFileName_DirAndFileName


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

    # String em várias linhas utilize ''' ''' para envolver.
    parser = argparse.ArgumentParser(
      prog = 'hello_03.py',
      description = '''Minicurso Aprendendo Python - XXVIII SEMAT - Versao 1.0
        Este programa le um arquivo impossivel de ser aberto em qualquer editor!
        \n exemplo de execução:
            $ python hello_03.py -debug 1 -raio 2 -nome "Marcelo Palin"
        ''',
      epilog = 'Para consultar o Help digite:  python hello_03.py -h '
      )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s vs. 1.0')
    parser.add_argument('-raio', action='store', dest='dbl_raio', type=float, default=1.0)
    parser.add_argument('-debug', action='store', dest='flag_imprimir', type=int, default=0) #0 = false, 1 = true
    parser.add_argument('-nome_arquivo', action='store', dest='str_recebe_nome', default="file.txt" )

    # Pega a lista de parametros passada no prompt de comando e armazena em uma lista
    # Ex de execucao: python hello_03 -debug 0 -nome "Marcelo Palin"
    lstArgs = parser.parse_args()

    return lstArgs

  ##@fim do metodo
  ##----------------------------------------------------------------------------

# Quando executo o codigo, qual funcao devo chamar primeiro?
if __name__ == '__main__':
    main()
