# coding: utf-8

__author__ = "et1m"

#imports
#python-requests
#python-bs4
#python-sys

import requests
from bs4 import BeautifulSoup
import sys

import requesocks



reload(sys)
sys.setdefaultencoding('utf-8') #codifica pra utf-8

print("\033[36m"+"""\
                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  	APINFO      | |             
|:______B:|      | |                | |             
|:______B:|      | |  Et1m owned    | |             
|         |      | |  you ;)        | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:    
  """+'\033[0;0m')
print 'C0D3D BY ET1M ---> GITHUB :'+'\033[0;0m'+' https://github.com/3t1n/'
print '\n'


n_pag = int(input('\033[34m'+'Digite o número de páginas que deseja listar:  '+'\033[0;0m')) #quantas pags o user quer que liste]
print '\n'
#famosa gamb pq o range conta o zero entao sempre vai ficar faltando a ultima, logo adcionando 1 a mais resolve
num = n_pag + 1 
for pagina  in range(1,num): 
	print '\n'
	print 'pagina: ',pagina #conta em que pag esta
	print '\n'
	url = 'http://www.apinfo2.com/apinfo/inc/pesq9a.cfm'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'} #declara o user agent
	payload = {'pkey' : 'vhYZxqhZhZZqlvYkZwZqKYY', 'tcv' : '149352','estado': 'SP','pag' : pagina }
	pagina = +1
	r = requests.post(url,verify=False,headers=headers,data=payload,allow_redirects=False) #requests post permite mudar a página
	r.encoding = 'utf-8'	
	html = r.text #criando o objeto html
	soup =  BeautifulSoup(r.content, 'html.parser') #pega o html da page e coloca na soup

	for conteudo in soup.find_all(class_="info m-tb"): #vai puxar as divs com essa classe		
		

		headers2 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
		href = conteudo.a['href']
		url2 = 'http://www.apinfo2.com/apinfo/inc/'+href
		cookie = {'kukpesqcv1': '191.188.61.102', 'PHPSESSID' :'dn6202ao6elhaj1feltr67ggg1'}
		req = requests.get(url2,headers=headers2,verify=False,allow_redirects=False,cookies=cookie)
		print (req.text)
	

