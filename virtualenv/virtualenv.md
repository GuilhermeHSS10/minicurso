[Voltar Início](../README.md)<a name="indice"></a>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css">


<img src="http://www.cartoonaday.com/images/cartoons/2012/08/big-bang-theory-cartoon-598x401.jpg" width = 350>


# Virtualenv

** O que vamos aprender? **

- [x] [Contextualização](#contexto)
- [x] [O que é um Ambiente Virtual Python?](#oquee)
- [x] [O que é o Virtualwrapper?](#obj_virtualwrapper)
- [x] [Instalando o Virtualenv e Virtualwrapper no Linux](#instalando)
- [x] [Criando um Ambiente chamado Flask](#criando)
- [x] [Ativando e Desativando os Ambientes Virtuais](#ativando)

#### Referências

<a href="http://docs.python-guide.org/en/latest/dev/virtualenvs/" target="_blank">**Documentation Virtualenv**</a>


<br/> 
<hr>

## Contextualização <a name="contexto"></a>

Quando você escolheu aprender a programar em Python você teve que optar
entre o Python 2.x ou Python 3.x (recomendada) e além disso você escolheu
como instalar o python na sua máquina:

- [-] Minimalista - apenas o interpretador - sem os pacotes (aprox. 27.9Mb) <a href="https://www.python.org/downloads/" target="_blank">**Download Python**</a>
- [-] ou uma versão que já contivesse vários pacotes juntos:

  * Distribuição Científica Anaconda
  * Distribuição Científica WinPython

Portanto, ficou na sua mente que você tem UM computador com UMA versão de Python 
instalada e dentro vários pacotes instalados.

### Pergunta:
**Será que é possível ter em UM computador com VÁRIAS versões de Python 
onde CADA Python tenha o seu conjunto de pacotes específicos?**

**R:** Sim. Através do pacote **virtualenv**.

### Problema comum:
Uma vez que você tenha aprendido a desenvolver projetos em Python fica claro
que para cada projeto temos os **pacotes** necessários para aquele projeto.
E que cada pacote tem sua versão dependendo da versão do python
que foi desenvolvido (ex: python 2.7, python 3.4, ...).

**Problema**: você deseja passar seu projeto para outra pessoa, ou para outro computador.
Qual é a melhor maneira de se fazer isso sem **estragar** as configurações do python
daquele computador, daquela pessoa?

Em geral, a pessoa fica com receio de que você coloque o seu projeto na máquina
dela, uma vez que ela tem o Python 2.7 instalado, e o seu projeto exige o 
Python 3.x (mais novo). 

Como convencer a outra pessoa a instalar o seu projeto na máquina dela? Simples
explique que você **ISOLARÁ** o python 3.x com o **virtualenv** e todos
os pacotes do seu projeto ficarão encapsulados dentro do ambiente virtual
que você criará.

### Então, como faço isso?
Primeiro entenda o que é um ambiente virtual python (virtualenv) e logo
em seguida explico como criar seu ambiente virtual, e você poderá repetir
a ação criando quantos ambientes virtuais achar necessário.

<br/> 
<hr>

## O que é um Ambiente Virtual Python? <a name="oquee"></a>

**Virtualenv** é uma ferramenta para criar ambientes **isolados** de **Python**, ou seja,
você poderá ter na mesma máquina quantos pythons quiser, cada um de uma determinada versão (python 2.7
python 3.4, python 3.5, ...) e em cada ambiente você terá seus pacotes específicos.

Isso permitirá que você teste várias combinações de versões, e isole aquela que melhor
atente o seu projeto.


O que isto significa?
**R:** isto significa que você poderá ter diversas versões de python instaladas 
no seu sistema operacional sem que um ambiente interfira no outro.  Imagine que
você esteja desenvolvendo um Projeto Web em Python e precise apenas dos pacotes
relacionados a Web (Django, Flask...), e em outro projeto você esteja desenvolvendo
um projeto que exige pacotes de análise científica. Isolando os projetos dentro do 
ambiente, você estará isolando as versões de pacotes já testadas para aquele
projeto funcionar. E no momento de instalar em outra máquina você somente
terá que instalar "estes" pacotes.


#### Por quê utilizar o Virtualenv?

Imagine que você **Virtualenv** é um software que permite a criação de ambientes 
virtuais com total independência dos outros ambientes criados no Virtualenv. 
Isso permite que cada ambiente tenha sua própria autonomia para 
instalar seus pacotes de forma que a configuração de 
um ambiente não interfira nos demais ambientes de outros projetos.

Porém, criar **virtualenvs** manualmente em Python é uma tarefa que pode ser tediosa. Para facilitar vamos utilizar o **virtualenvwrapper** que facilitam significativamente a gestão de um grande número de ambientes virtuais. Primeiro, precisamos instalar o pacote mencionado no sistema.


* É importante que CADA projeto tenha seu próprio AMBIENTE VIRTUAL, ou seja, sua versão de PYTHON e seus PACOTES necessários para ele.

[Voltar para Índice](#indice)
<hr>
<br/>


## O que é o Virtualenvwrapper? <a name="obj_virtualwrapper"></a>

O objetivo dele é fornecer um conjunto de comandos que facilitam trabalhar 
com vários ambientes virtuais. O VirtualenvWrapper também centraliza
todos os ambientes virtuais em um único diretório.

Vamos detalhar como instalá-lo no Linux e Windows nas seções abaixo.

[Voltar para Índice](#indice)
<hr>
<br/>


### Instalando o Virtualenv e Virtualenvwrapper no Linux<a name="instalando"></a>

A melhor maneira de configurarmos no Linux é mostrada em 3 passos:

**Passos:**

**1)** Instale através do apt-get os seguintes pacotes:

~~~bash
$sudo aptitude install virtualenv python3-virtualenv virtualenvwrapper python3-pip

ou

$sudo apt-get install virtualenv python3-virtualenv virtualenvwrapper python3-pip

~~~

**2)** Crie o diretório que conterá todos os ambientes virtuais:

~~~bash
/home/user$ mkdir .venvs
~~~


**3)**  Configure o **.bashrc** para o Linux

#### Ubuntu
~~~bash
export WORKON_HOME=$HOME/.venvs 
export PROJECT_HOME=$HOME/projs_python 
export VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.s
source /usr/share/virtualenvwrapper/virtualenvwrapper_lazy.sh
export PYTHONPATH="$HOME/amperelib:$HOME:$PYTHONPATH"
~~~

#### Debian
~~~bash
export WORKON_HOME=$HOME/.venvs 
export PROJECT_HOME=$HOME/projs_python 
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh 
source /usr/local/bin/virtualenvwrapper_lazy.sh 
export PYTHONPATH="$HOME/amperelib:$HOME:$PYTHONPATH"
~~~

#### Windows

Instale o Virutualenv:

~~~bash
c:/> pip install virtualenv
~~~

Depois instale o virtualenvwrapper.

Qual o objetivo de utilizar o virtualenvwrapper? 
**R:** Ele force um conjunto de comandos que facilitam trabalhar 
com vários ambientes virtuais. O VirtualenvWrapper também centraliza
todos os ambientes virtuais em um único diretório.

Para instalar no Windows faça:

~~~bash
c:\> pip install virtualenvwrapper-win
~~~


#### Comandos Básicos com o virtualenvwrapper instalado

##### 1)Para criar um ambiente virtual:

Sintaxe: **mkvirtualenv** \<nome do ambiente que deseja criar\>

**Exemplo:**
~~~bash
$ mkvirtualenv proj01_py3
~~~

Este comando criará um ambiente virtual chamado **proj01_py3** com a versão
padrão do python instalado dentro do diretório:

* **$HOME/.venvs**  no Linux (conforme configurado acima no .bashrc);
* **C:\Users\<nome do usuario windows>\Envs** no Windows;

~~~bash
$ mkvirtualenv -python=python3 proj01_py3

ou coloque o caminho completo onde está o executável do python:

$ mkvirtualenv -python=/usr/bin/python3 proj01_py3
~~~

##### 2)Para ativar o ambiente virtual:

Para listar todos os ambientes virtuais que existem na máquina execute:
~~~bash
$ workon
~~~

Para ativar o ambientes virtual específico (ex: proj01_py3)
~~~bash
$ workon proj01_py3
~~~


##### 3)Para desativar o ambiente virtual: 

Você sabe que o Ambiente Virtual está ativo pois o comando de prompt (ou terminal)
mostra o nome do ambiente antes do cursor. Para desativá-lo faça:
~~~bash
(proj01_py3) c:\> deactivate
~~~


##### 4)Para deletar o ambiente virtual: 

Supondo que você já entregou o projeto, e acha que não mais será necessário
aquele ambiente com o Python 3.x e seus pacotes, faça :
~~~bash
c:\> rmvirtualenv proj01_py3
~~~


[Voltar para Índice](#indice)
<hr>
<br/>



### Criando um Ambiente chamado Flask<a name="criando"></a>

Uma vez com o **virtualenv** e **virtualwrapper** instalados na sua 
máquina e o diretório **.venvs** no seu diretório **HOME** vamos 
agora **CRIAR** um ambiente virtual que conterá o **python 3.x** e 
todos os pacotes necessários para rodarmos o projeto em **Flask**.


**Passos:**

**1)** Provavelmente seu linux já tenha o Python 3.x instalado, porém, o 
Python 2.7 ainda é a versão padrão. Verifique com o comando:

~~~bash
mpi@mpi-pc:~$ python --version
Python 2.7.12
~~~

Verifique se seu python 3.x está instalado no diretório **/usr/bin** ou 
**/usr/local/bin**:

~~~
mpi@mpi-pc:/usr/bin$ ls python*
python            python2.7-pyrexc  python3.5          python3-config
python2           python2-config    python3.5-config   python3m
python2.7         python2-pbr       python3.5m         python3m-config
python2.7-config  python3           python3.5m-config  python-config
~~~

Neste caso temo o **python 3.5** instalado no diretório **/usr/bin**, 
vamos então criar um **Ambiente Virtual** chamado **flask** 
que utilizará o **Python 3.5** como padrão.

Sintaxe: mkvirtualenv \<versão do python para o ambiente\> \<**nome** do ambiente\>

No Ubuntu verifiquei que o Python 3 está instalado no diretório **/usr/bin**:

> mpi@mpi-pc:~$ **mkvirtualenv** --python=/usr/bin/python3  *flask*


Se você observar agora no diretório:

~~~
mpi@mpi-pc:~$ cd .venvs/
mpi@mpi-pc:~/.venvs$ ls
flask                initialize      postmkvirtualenv  premkproject
Flask-SocketIO       postactivate    postrmvirtualenv  premkvirtualenv
Flask-SocketIO_py27  postdeactivate  preactivate       prermvirtualenv
get_env_details      postmkproject   predeactivate
~~~

> Vamos aprender a ativar e desativar o ambiente virtual no **terminal** 
>e depois vamos aprender a instalar todos os pacotes necessários dentro dele.
 
[Voltar para Índice](#indice)
<hr>
<br/>


### Ativando e Desativando os Ambientes Virtuais<a name="ativando"></a>

Antes de ativar o ambiente virtual você pode **listar** todos os  ambientes já criados com o comando:


Comando: mpi@mpi-pc:~/projs_python/meu_proj$ **workon**

Listará todos os ambientes criados na minha máquina:

~~~bash
mpi@mpi-pc:~/projs_python/meu_proj$ workon
flask
ambiente_cientifico
ambiente_web
ambiente_django
~~~ 

A **ativação** do ambiente virtual chamado **flask** será feita através do 
seguinte comando:

> mpi@mpi-pc:~/projs_python/meu_proj$ **workon flask**

você perceberá que ele está ativo através do seu **prompt**:

> **(flask)** mpi@mpi-pc:~/projs_python/meu_proj$

**Desativação** do ambiente basta fazer:

> **(flask)** mpi@mpi-pc:~/projs_python/meu_proj$ **deactivate**

e seu prompt voltará ao normal:

> mpi@mpi-pc:~/projs_python/meu_proj$ 
 
[Voltar para Índice](#indice)
<hr>
<br/>



### Instalando pacotes python no Novo Ambiente<a name="instalando"></a>

A instalação  dos pacotes python do projeto no novo 
**ambiente virtual flask** pode ser executada de duas maneiras:


**Um pacote por vez:**

> Instale através do **pip3** do seu ambiente virtual **flask** que fica localizado
no diretório **/home/mpi/.venvs/bin/** no Linux (conforme configuramos acima):

~~~bash
(flask) mpi@mpi-pc:~/.venvs/flask/bin$ ls
activate                painter.py      python-config
activate.csh            pilconvert.py   rst2html.py
activate.fish           pildriver.py    rst2latex.py
activate_this.py        pilfile.py      rst2man.py
blockdiag               pilfont.py      rst2odt_prepstyles.py
createfontdatachunk.py  pilprint.py     rst2odt.py
dateadd                 pip             rst2pseudoxml.py
datediff                pip3            rst2s5.py
easy_install            pip3.5          rst2xetex.py
easy_install-3.5        player.py       rst2xml.py
enhancer.py             postactivate    rstpep2html.py
explode.py              postdeactivate  sphinx-apidoc
flask                   preactivate     sphinx-autogen
get_env_details         predeactivate   sphinx-build
gifmaker.py             pybabel         sphinx-quickstart
gunicorn                __pycache__     tabulate
gunicorn_django         pygmentize      thresholder.py
gunicorn_paster         python          viewer.py
mod_wsgi-apxs           python3         watchmedo
mod_wsgi-express        python3.5       wheel
~~~


> **(flask)** mpi@mpi-pc:~/projs_python/meu_proj$

~~~bash
sudo pip install -r require_flask.txt
~~~
 
[Voltar para Índice](#indice)
<hr>
<br/>

