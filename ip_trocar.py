# coding: utf-8


__author__ = "et1m"


from urllib2 import Request
from urllib2 import urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8') #codifica pra utf-8

ua = UserAgent() #setando user agent
proxies = []

def random_proxy():
  return random.randint(0, len(proxies) - 1)

def proxy():
	header_proxy = {'User-Agent' : ua.random}
	proxy_req = requests.get('https://www.sslproxies.org/', headers = header_proxy)
	proxy_req.encoding = 'utf-8'
	html = proxy_req.text
	soup =  BeautifulSoup(proxy_req.content, 'html.parser')
	proxies_table = soup.find(id='proxylisttable')
	  # salvando os proxy no array
	for row in proxies_table.tbody.find_all('tr'):
	    proxies.append({
	      'ip':   row.find_all('td')[0].string,
	      'port': row.find_all('td')[1].string
	    })

	  # escolhendo um proxy aleatório
	proxy_index = random_proxy()
	proxy = proxies[proxy_index]

	for n in range(1, 20):
	    req = Request('http://icanhazip.com')
	    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
	    # a cada 1 request, gerar um novo proxy
	    if n % 1 == 0:
	      proxy_index = random_proxy()
	      proxy = proxies[proxy_index]

	    # fazendo a chamada
	    try:
	      my_ip = urlopen(req).read().decode('utf8')
	      print('#' + str(n) + ': ' + my_ip)
	    except: # se errar delete meu proxy e ache outro
	      del proxies[proxy_index]
	      print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
	      proxy_index = random_proxy()
	      proxy = proxies[proxy_index]


if __name__ == '__main__':
  proxy()

