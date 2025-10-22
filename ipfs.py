import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
    # Convert dict to JSON and upload to IPFS
	files = {
		'file': json.dumps(data)
	}

	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
	response.raise_for_status() 
	cid = response.json()['Hash'] 

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://ipfs.io/ipfs/{cid}"
	response = requests.get(url)
	response.raise_for_status()

	if content_type == "json":
		data = response.json()
	else:
		data = response.text

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
