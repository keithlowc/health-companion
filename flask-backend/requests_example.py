import requests

API_ENDPOINT = 'http://127.0.0.1:5000/data'

def send_post():
	data = {
		'bpm': 124.2,
		'bodyTemp': 45.23,
	}

	r = requests.post(url = API_ENDPOINT, json = data)

	response = r.text
	print("This is the response: " + str(response))

def send_get():
	r = requests.get(url = API_ENDPOINT)
	data = r.json()
	print(data)


if __name__ == '__main__':
	send_post()