import requests

print ('#######################')
print ('#### consulta CEP #####')
print ('#######################')
print ('')

cep_input = input ('Digite o Cep para consulta: ')

if len (cep_input) != 8:
    print ('Quantidade de digitos inválida!!')
    exit

print('Resultados')

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

print (request.json())

address_data = request.json()

if 'erro' not in address_data:
    print(request.json())
else:
    print('CEP invalido')


