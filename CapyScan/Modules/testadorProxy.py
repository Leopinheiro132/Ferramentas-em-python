#testador de proxy 1.0.5
import requests
import os
url = 'https://www.google.com'
input_file = 'proxy.txt'
output_file = 'proxysFuncionando.txt'

with open(input_file, 'r') as file:
    proxy_list = [line.strip() for line in file.readlines()]

working_proxies = []

for proxy in proxy_list:
    print('Testando proxy:', proxy)
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        print('Proxy funcionando!')
        working_proxies.append(proxy)
    except:
        print('Proxy offline, pulando...')
os.system("clear")
print("testes terminado")
print("escrevendo o arquivo")
# Escrevendo os proxies funcionando no arquivoc
with open(output_file, 'w') as file:
    for proxy in working_proxies:
        file.write(f"{proxy}\n")
