import requests
from bs4 import BeautifulSoup
from urllib import parse


req = requests.Session()

class DictRequest:
	def __init__(self, site=None, query=None):
		#웹통신할 사이트 및 쿼리 초기화
		self.site_url = 'https://dic.daum.net//search.do?'
		self.query = {
			'q'   : None,
			'dic'   : 'all',
			}

	def request(self, word=None):
		#쿼리에서 검색할 단어 설정
		self.query['q'] = word
		if self.query['q'] is None:
			raise ValueError('input word argument in request()')

		#검색 url 생성 및 request
		req_url = self.site_url + parse.urlencode(self.query)
		resp = req.get(req_url)
		html = resp.text

		#받은 html 가공 및 사전 내용 반환
		soup = BeautifulSoup(html, 'html.parser')
		if soup.select('.tit_info'):
			return None
		mean_list = soup.select_one('ul.list_search').select('.txt_search')

		result = []
		for mean in mean_list:
			result.append(mean.text)
		return result

if __name__ == '__main__':
	string = "asdfasdfsdf"
	d = DictRequest()
	r = d.request(string)
	print(r)
