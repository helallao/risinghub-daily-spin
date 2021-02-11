import requests
from bs4 import BeautifulSoup
import json


settings = json.load(open('settings.json', 'r'))


with requests.Session() as s:
	s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101'})
	
	soup = BeautifulSoup(s.get('https://risinghub.net/login').text, 'html.parser')
	
	s.post('https://risinghub.net/login', data={'username':settings['username'], 'password':settings['password'], '_token':soup.find('input', attrs={'name':'_token'})['value']})
	
	soup = BeautifulSoup(s.get('https://risinghub.net/roulette').text, 'html.parser')
	
	if soup.find('select', attrs={'id':'hero_select'}):
		for hero in soup.find('select', attrs={'id':'hero_select'}).find_all('option'):
			if hero.getText() == settings['hero_name']:
				hero_token = hero.get('value')
		
		response = s.post('https://risinghub.net/roulette', data={'hero':hero_token, '_token':soup.find('input', attrs={'name':'_token'})['value']})
		
		print('successful')
	else:
		print('unsuccessful')