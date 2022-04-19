*** Settings ***
Documentation        Aqui neste arquivo estarão presentes todos os testes
...                  API automatizados com suas Keywords.

Resource             ../../src/config/package.robot

Suite Setup          Conectar a minha API


*** Test Cases ***
Cenario: Consultando livro com sucesso
    [Tags]            GET
    Dado que eu tenha acesso ao Endpoint de Books
    Quando executar a requisição GET
    Então o status code deverá ser         200
    E a Reason deverá ser                  OK

Cenario: Cadastrando livro com sucesso
    [Tags]            POST
    Dado que eu tenha acesso ao Endpoint de Books
    Quando executar a requisição POST
    Então o status code deverá ser         200
    E a Reason deverá ser                  OK
    E as informações do livro devem ser apresentadas no response body