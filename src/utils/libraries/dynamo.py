import boto3


#####################################################################
#                             Cartões                               #
#####################################################################

def delete_card(holderid):
    nametable = 'Barigui.Services.Cards_V2_Accounts'
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(nametable)
    response = table.delete_item(
        Key={
            "Id": '{}'.format(holderid)
        }
    )
    print(response)
    return response


#####################################################################
#                          Investimentos                            #
#####################################################################

def delete_pending_earlywithdraw(cpf): 
    nameTable = 'Barigui.Services.Investment_EarlyWithdrawRequest'
    nameAttribute = 'CustomerId'
    value = f'{cpf}'
    print("Attempting a conditional delete...")
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.delete_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response)
    return response

def delete_remove_suitability(cpf): 
    nameTable = 'Barigui.Services.Investment_CustomerSuitability'
    nameAttribute = 'CustomerId'
    value = f'{cpf}'
    print("Attempting a conditional delete...")
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.delete_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response)
    return response

def delete_remove_suitability_history(cpf): 
    nameTable = 'Barigui.Services.Investment_CustomerSuitabilityHistory'
    nameAttribute = 'CustomerId'
    value = f'{cpf}'
    print("Attempting a conditional delete...")
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.delete_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response)
    return response

def update_window_transaction(id, initial, final):
    nameTable = 'Barigui.Services.Investment_Parameters'
    nameAttribute = 'Id'
    value = f'{id}'
    start_time = f'{initial}'
    final_time = f'{final}'
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.get_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response.get('Item'))
    item = response['Item']
    item['TransactionWindows'] = {'L': [{'M': {'FactsheetType': {'S': 'Primary'}, 'FinalTransactionHour': {'S': final_time}, 'InitialTransactionHour': {'S': start_time}, 'TransactionWindowMessage': {'S': 'Este investimento está disponível em dias úteis entre às 09:00 e 14:30.\n\nPor favor, volte neste horário para realizar sua aplicação'}, 'Vendor': {'S': 'Virtual'}}},
                                 {'M': {'FactsheetType': {'S': 'Secondary'}, 'FinalTransactionHour': {'S': final_time}, 'InitialTransactionHour': {'S': start_time}, 'TransactionWindowMessage': {'S': 'Este investimento está disponível em dias úteis entre às 09:00 e 15:30.\n\nPor favor, volte neste horário para realizar sua aplicação'}, 'Vendor': {'S': 'Virtual'}}},
                                 {'M': {'InitialTransactionHour': {'S': start_time}, 'FinalTransactionHour': {'S': final_time}, 'TransactionWindowMessage': {'S': 'Este investimento está disponível em dias úteis entre às 09:00 e 22:00.\n\nPor favor, volte neste horário para realizar sua aplicação'}, 'Vendor': {'S': 'Lydians'}}},
                                 {'M': {'InitialTransactionHour': {'S': start_time}, 'FinalTransactionHour': {'S': final_time}, 'TransactionWindowMessage': {'S': ''}, 'Vendor': {'S': 'FakerAsset'}}}]}
    response = client.put_item(TableName=nameTable, Item=item)
    print(response)
    return response

def update_withdrawal_windowhour(id, hour):
    nameTable = 'Barigui.Services.Investment_Parameters'
    nameAttribute = 'Id'
    value = f'{id}'
    value_hour = f'{hour}'
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.get_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response.get('Item'))
    item = response['Item']
    item['FinalWithdrawalWindowHour'] = {"S": value_hour}
    response = client.put_item(TableName=nameTable, Item=item)
    print(response)
    return response


#####################################################################
#                   Ativar/desativar feature flag                   #
#####################################################################

def update_flag_active(code):
    nameTable = 'Barigui.Services.FeatureFlag_GlobalScopes'
    nameAttribute = 'Code'
    value = f'{code}'
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.get_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response.get('Item'))
    item = response['Item']
    item['isActive'] = {'BOOL': True}
    print(item)
    response = client.put_item(TableName=nameTable, Item=item)
    print(response)
    return response

def update_flag_inative(code):
    nameTable = 'Barigui.Services.FeatureFlag_GlobalScopes'
    nameAttribute = 'Code'
    value = f'{code}'
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.get_item(TableName=nameTable, Key={nameAttribute: {"S": value}}) 
    print(response.get('Item'))
    item = response['Item']
    item['isActive'] = {'BOOL': False}
    print(item)
    response = client.put_item(TableName=nameTable, Item=item)
    print(response)
    return response

#####################################################################
#                   CRÉDITO IMOBILIÁRIO                             #
#####################################################################

def update_serie_installment(id, status, due_date, bar_code):
    nameTable = 'Barigui.Services.RealEstate.Installments.SerieInstallment'
    nameAttribute = 'Id'
    value = f'{id}'
    status = f'{status}'
    due_date = f'{due_date}'
    bar_code = f'{bar_code}'
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.get_item(TableName=nameTable, Key={nameAttribute: {"S": value}})
    print(response.get('Item'))
    item = response['Item']
    item['Status'] = {'S': status}
    item['DueDate'] = {'S': due_date}
    item['BarCode'] = {'S': bar_code}
    print(item)
    response = client.put_item(TableName=nameTable, Item=item)
    print(response)
    return response

def update_serie_installment_reset(id, status, due_date, bar_code):
    nameTable = 'Barigui.Services.RealEstate.Installments.SerieInstallment'
    nameAttribute = 'Id'
    value = f'{id}'
    status = f'{status}'
    due_date = f'{due_date}'
    bar_code = f'{bar_code}'
    is_consolidate = f'{"false"}'
    consolidate_parcels = f'{""}'
    reference_date = f'{"0001-01-01T00:00:00"}'
    confirmation_since = f'{""}'
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.get_item(TableName=nameTable, Key={nameAttribute: {"S": value}})
    print(response.get('Item'))
    item = response['Item']
    item['Status'] = {'S': status}
    item['DueDate'] = {'S': due_date}
    item['BarCode'] = {'S': bar_code}
    item['IsConsolidatedParcel'] = {'S': is_consolidate}
    item['ConsolidatedParcels'] = {'S': consolidate_parcels}
    item['UsedReferenceDate'] = {'S': reference_date}
    item['WaitingConfirmationSince'] = {'S': confirmation_since}
    print(item)
    response = client.put_item(TableName=nameTable, Item=item)
    print(response)
    return response