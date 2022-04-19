*** Settings ***
Documentation        Aqui estarão presentes todas as keywords dos testes de api Books

Resource            ../../config/package.robot
Library    Collections

*** Variables ***
&{JSON_BODY}
...    id=987987987
...    title=Aprendendo Robot com o Negão
...    description=Seja um automatizador fora da curva
...    pageCount=321
...    excerpt=Testando
...    publishDate=2022-10-16T11:01:21.168Z

*** Keywords ***
Dado que eu tenha acesso ao Endpoint de Books
    Log To Console        Validando o endpoint (https://fakerestapi.azurewebsites.net/api/v1/)

Quando executar a requisição GET
    ${RESPOSTA}           GET On Session          fakeAPI            Books            expected_status=200
    Log                   ${RESPOSTA.text}
    Set Suite Variable    ${RESPOSTA}

Então o status code deverá ser 
    [Arguments]                   ${STATUS_CODE}
    Should Be Equal As Strings    ${RESPOSTA.status_code}        ${STATUS_CODE}

E a Reason deverá ser 
    [Arguments]                   ${REASON}
    Should Be Equal As Strings    ${RESPOSTA.reason}             ${REASON}

#####################################################################################################
Quando executar a requisição POST
    ${RESPOSTA}             POST On Session        fakeAPI        Books
    ...                     json=${JSON_BODY}
    ...                     headers=${HEADERS}     expected_status=any
    Log To Console          ${RESPOSTA.text}
    Set Suite Variable      ${RESPOSTA}

E as informações do livro devem ser apresentadas no response body
    Dictionary Should Contain Item        ${RESPOSTA.json()}        id                    ${JSON_BODY.id}
    Dictionary Should Contain Item        ${RESPOSTA.json()}        title                 ${JSON_BODY.title}
    Dictionary Should Contain Item        ${RESPOSTA.json()}        description           ${JSON_BODY.description}
    Dictionary Should Contain Item        ${RESPOSTA.json()}        pageCount             ${JSON_BODY.pageCount}
    Dictionary Should Contain Item        ${RESPOSTA.json()}        excerpt               ${JSON_BODY.excerpt}
    Dictionary Should Contain Item        ${RESPOSTA.json()}        publishDate           ${JSON_BODY.publishDate}
                     