import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	pinata_api_key = "a1e4fe819b94778b51f2"
	pinata_secret_api_key = "6c1e037457d6bb60378b9b1828b6e783756486379b09cd1940b9d773afe5f6e9"
	
	files = {
		'file': json.dumps(data)
	}

	response = requests.post('https://gateway.pinata.cloud/ipfs', 
							 files=files,
							 auth=(pinata_api_key, pinata_secret_api_key))
	response.raise_for_status() 
	cid = response.json()['Hash'] 

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)
	response.raise_for_status()

	if content_type == "json":
		data = response.json()
	else:
		data = response.text

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
