*** Settings ***
Documentation        Aqui estarão presentes todas as configurações de Setup e Teardown
...                  Essas configurações, podem ser utilizadas tanto para Suites Setup/Teardown
...                  quanto para test setup/teardown.

Resource             package.robot

*** Keywords ***
Abrir navegador
    Set Selenium Implicit Wait    ${CONFIG.IMPLICITY_WAIT}
    Open Browser                  about:blank        ${CONFIG.BROWSER_NAME}
    #Eyes Open
    Go To                         ${CONFIG.URL}
    Maximize Browser Window

Fechar navegador    
    Capture Page Screenshot
    #Eyes Close Async
    Close Browser

Conectar a minha API
    Create Session        fakeAPI                         https://fakerestapi.azurewebsites.net/api/v1/        disable_warnings=${True}
    ${HEADERS}            Create Dictionary               content-type=application/json
    Set Suite Variable    ${HEADERS}