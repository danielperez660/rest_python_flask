import requests

URL = 'http://127.0.0.1:9999/'
male_path = 'figure/male'
female_path = 'figure/female'
random_path = 'figure/'
all_path = 'all_figures/'

REST_BOOKS = 'https://www.goodreads.com/search/index.xml'
GOOD_READS_KEY = 'kasyZkeIPzsma2EBH0Lu9w'

query = "Test"
payload = {'q': query, 'key': GOOD_READS_KEY}
resp = requests.get(REST_BOOKS, params=payload)
print(resp.text)

REST_TODAY = 'http://history.muffinlabs.com/date'
resp = requests.get(REST_TODAY)
print(resp.json())

print(requests.get(URL + male_path).json())
print(requests.get(URL + female_path).json())
print(requests.get(URL + random_path).json())
print(requests.get(URL + all_path).json())
