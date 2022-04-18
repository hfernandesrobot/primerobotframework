# Automação WEB

<img src="https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white" />

A finalidade deste documento é a de passar informações como, ferramentas, configurações, arquitetura e tecnologias envolvidas.

É de suma importância que as instruções sejam aqui presentes sejam seguidas para que possam ser adotados padrões aqui presentes para facilitar questões de manutenabilidade.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.


```bash
# Clone o projeto para sua máquina
$ git clone <URL Projeto>

# Acessar a branch ui
$ git checkout origin ui
```

## 📋 Pré-requisitos

Quais ferramentas serão necessárias para poder executar os testes localmente?

-   **[Download do Python](https://www.python.org/downloads/)**
-   **[Downlaod do VsCode](https://code.visualstudio.com/download)**
-   **[Downlaod do ChromeDriver](https://chromedriver.chromium.org/downloads)**
-   **[Downlaod do CMDER](https://cmder.net/)**



## 🔧 Instalação

Agora que temos o projeto disponível em nossa máquina e todas as ferramentas, vamos mostrar aqui como instalar alguns recursos e ferramentas que poderão nos ajudar no processo de automação.

Dentro do **VSCode**, instale as seguintes extensões:

- **Robot Framework Intellisense**
- **Robot Framework Formatter**
- **RobotF Extension**
- **Python**
- **Material Icon Theme**
- **GitLens — Git supercharged**  


### Instalando as Libraries do nosso projeto.

Dentro do nosso projeto de automação, temos um arquivo requirements.txt. Dentro desse arquivos estão presentes todas as libraries que serão necessárias para podermos executar nossos testes sem problemas. 

Uma vez que temos todas as libs dentro do requirements, precisamos apenas instala-las e para isso execute o comenado a seguir:


```bash
# Comando para instalar todas as libraries
$ pip install -r requirements.txt
```

## 📦 Arquitetura

Aqui iremos apresentar a arquitetura padrão do nosso projeto. A arquitetura de forma geral foi criada pensando na fácil compreensão de todos que trabalharem com a automação. Focados em uma arquitetura limpa e que exigisse uma curva de aprendizado menor, chegamos a seguinte arquitetura:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/KbWm9pJ/Captura-de-Tela-2021-08-24-a-s-23-46-20.png" alt="Captura-de-Tela-2021-08-24-a-s-23-46-20" border="0"></a>

* Segue descrição das pastas que fazem parte do projeto:

   - **src:** A pasta source será a pasta responsável por armazenar todo o core do projeto como, configurações, massa e keywords do projeto como um todo.
	- **auto:** Pasta responsável por armazenar a arquitetura de dados, elementos mapeados e keywords de todas as features.
	- **data:** Nesta pasta será possível administrar toda arquitetura de massa e mensageria dos testes como, credenciais de acesso ou validação de mensagens de erro ou sucesso.
	- **elements:** A pasta elements será responsável por armazenar os elementos e componentes com seus identificadores unicos para serem usados tantos em testes de Android quanto de iOS.
	- **keywords:** Todas as keywords do projeto estarão presentes nessa pasta, porém, separadas por features.
	- **config:** Todas as configurações de execução e capabilities serão definidos no arquivo hooks.yml dentro da pasta config.
	- **utils:** Teremos aqui todas as keywords ou libraries que podem ser utilizadas indepentende dos cenários ou clientes em questão.
	- **test:** Pasta responsável por armazenar todos os logs pós execução e as features/BDD's de execução.
	- **features:** As funcionalidades a serem testadas serão armazenadas dentro desta pasta.
	- **logs:** Pasta responsável por armazenar todos os logs pós execução e evidências.


    ## ⚙️ Executando os testes

Para executarmos os testes, precisamos abrir o terminal integrado na pasta raiz do projeto.

Neste caso a raiz é a pasta digitalchannel-qa-automation.


#### Primeiro passo:

Vamos abrir o cmder e navegar até a pasta do projeto.

#### Segundo passo:

Para executarmos todos os testes existentes no projeto, devemos executar o seguinte comando:

```bash
# Comando para executar todos os testes do projeto
$ robot -d ./tests/logs tests/features/
```

Já para executarmos uma feature específica, devemos informar qual .robot querermos executar.
Neste caso, vamos executar os testes de login como Exemplo:

```bash
# Comando para executar features específicas
$ robot -d ./tests/logs tests/features/login.robot
```

Também podemos executar cenários específicos, desde que os mesmos possuam sua Tag única. 
Como exemplo, podemos utilizar os testes de account. 

Cada cenário possui sua Tag unica e neste caso vamos executar o cenário de Inclusão de endereço.
Para isso, inserímos o comando -i e logo a frente a tag que desejamos executar. Veja no exemplo:

```bash
# Comando para executar um teste específico através de sua tag.
$ robot -d ./tests/logs -i SMOKE tests/features/login.robot
```

Caso queira alterar o locals onde os logs são salvos, basta ajustar o caminho após o -d.
Exemplo: Iremos passar no comando que os tests/logs serão salvos na pasta reports:

```bash
# Alterar o caminho após o -d
$ robot -d tests/logs tests/login.robot
```

### Configurações de execução.
As configurações de execução podem ser editadas dentro do arquivo hooks.yml.

- **NOME:** Define qual browser a execução irá acontecer (Para execução em headless usar "chromeheadless")
- **URL:** Define a url do sistema que será testado
- **IMPLICITY_WAIT:** Define o timeout do SeleniumWebdriver


### Configurações Gerais 
Temos um arquivo chamado package.robot que se encontra na seguinte hierarquia:

	- src
		- config
			- package.robot

Esse arquivo serve para concentrar todas as Libraries e Rosources que serão importados e utilizados no projeto.
Sendo assim, qualquer recurso ou Library nova, devem ser passandos apenas neste arquivo.

## 🛠️ Tecnologias Envolvidas
Mencione as ferramentas que você usou para criar seu projeto

* [Robot Framework](https://robotframework.org/) - O framework usado
* [Python](https://www.python.org/) - Linguagem predominante
* [GitLab Pipelines](https://docs.gitlab.com/ee/ci/pipelines/) - Tecnologia CI/CD

## ℹ️ Boas Práticas

Pensando em boas práticas e padrões de desenvolvimento, levantamos alguns itens que devem ser seguidos a risca para que possamos ter êxito na questão de Design Patterns.

**Essas praticas consistem em:**

- **BDD:** Usar as features sempre em terceira pessoa [Advérbio + sujeito + verbo (Quando for ação)].
- **Variáveis:** Sempre criar dicionários e variáveis com letrás maiusculas.
- **Keywords:** Todo texto validado não deve ser adicionado direto nas keywords. É esperado que o texto ou mensagem a serem validadas sejam armazenadas em variáveis.
- **Git:** É esperado que ao concluirmos o desenvolvimento, seja realizado um pull request para a branch mobile. Após a aprovação do pull request, a branch de trabalho deverá ser excluída.

## 📌 Versão

Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto)


## ✒️ Autores

Seguem abaixo todos os responsáveis pela elaboração, criação e aplicação do projeto apresentado neste repositório.

* **Helder Fernandes** - *Trabalho Inicial/Documentação*








