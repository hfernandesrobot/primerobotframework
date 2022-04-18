*** Settings ***
Documentation        Aqui estarão presentes todas as keywords dos testes de cadastro
...                  do site automationpractice.com

Resource            ../../config/package.robot

*** Keywords ***
Dado que o cliente tenha cadastro
Quando informar suas credenciais de acesso
Então o login será realizado com sucesso