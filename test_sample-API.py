import pytest
import requests
import json

def test_api_req():
	supply_url = "https://www.usplworld.com"
	url = supply_url + "/wishlist"
	resp = requests.get(url)
	r = resp.status_code	
	assert resp.status_code == 200
	

#if __name__ == '__main__':
#	test_api_req("https://www.usplworld.com")
	


