*** Settings ***
Documentation        Aqui estarão presentes todas as keywords dos testes de cadastro
...                  do site automationpractice.com

Resource            ../../config/package.robot

*** Keywords ***
Acessar a página home do site
    Acessar a página home do site Automation Practice

Clicar em "${BUTTON}"
    Wait Until Element Is Visible    xpath=//*[contains(text(), '${BUTTON}')]
    Click Element                    xpath=//*[contains(text(), '${BUTTON}')]
    
Clicar em Create an account
    Wait Until Element Is Visible    id=SubmitCreate
    Click Element                    id=SubmitCreate
    
Informar um e-mail válido
    ${FAKE_EMAIL}                    FakerLibrary.Free Email
    Wait Until Element Is Visible    email_create
    Input Text                       email_create    ${FAKE_EMAIL}
    
Preencher os dados obrigatórios
    ${FAKE_NAME}                     FakerLibrary.Name
    ${FAKE_LASTNAME}                 FakerLibrary.Last Name
    ${FAKE_ADDRESS}                  FakerLibrary.Street Address
    ${FAKE_COMPANY}                  FakerLibrary.Company
    ${FAKE_CITY}                     FakerLibrary.City
    ${FAKE_STATE}                    FakerLibrary.State
    ${FAKE_POSTCODE}                 FakerLibrary.Postcode
    ${FAKE_PHONE}                    FakerLibrary.Phone Number
    ${FAKE_ALIAS}                    FakerLibrary.User Name

    Wait Until Element Is Visible    ${REGISTER.form_register}
    Click Element                    ${REGISTER.check_mr}

    Input Text                       ${REGISTER.first_name}        ${FAKE_NAME}
    Input Text                       ${REGISTER.last_name}         ${FAKE_LASTNAME}
    Input Text                       ${REGISTER.password}          ${CADASTRO.SENHA}
    Select From List By Value        ${REGISTER.select_days}       ${CADASTRO.DIA}
    Select From List By Value        ${REGISTER.select_months}     ${CADASTRO.MES}
    Select From List By Value        ${REGISTER.select_year}       ${CADASTRO.ANO}

    Input Text                       ${REGISTER.company}           ${FAKE_COMPANY}
    Input Text                       ${REGISTER.address1}          ${FAKE_ADDRESS}
    Input Text                       ${REGISTER.city}              ${FAKE_CITY}
    
    Select From List By Value        ${REGISTER.state}             3                                
    Input Text                       ${REGISTER.postcode}          ${FAKE_POSTCODE}
    Input Text                       ${REGISTER.mobile}            +5511959966645 
    Input Text                       ${REGISTER.alias}             ${FAKE_ALIAS}

    Click Element                    ${REGISTER.btn_register}       

Submeter cadastro
    Click Element    locator
    
Conferir se o cadastro foi efetuado com sucesso
    Wait Until Page Contains    text
    
