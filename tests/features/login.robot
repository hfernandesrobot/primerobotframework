*** Settings ***
Documentation        Aqui neste arquivo estarão presentes todos os testes
...                  Web automatizados com suas Keywords.

Resource             ../../src/config/package.robot

Test Setup           Abrir navegador
Test Teardown        Fechar navegador

*** Test Cases ***
Cenario: Login com sucesso
    Dado que o cliente tenha cadastro
    Quando informar suas credenciais de acesso
    Então o login será realizado com sucesso