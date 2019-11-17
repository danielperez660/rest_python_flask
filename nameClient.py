import requests

URL = 'http://127.0.0.1:9999/'
male_path = 'figure/male'
female_path = 'figure/female'
random_path = 'figure/'
all_path = 'all_figures/'

print(requests.get(URL+male_path).json())
print(requests.get(URL+female_path).json())
print(requests.get(URL+random_path).json())
print(requests.get(URL+all_path).json())
