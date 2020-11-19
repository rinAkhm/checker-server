import requests

r = requests.get('https://api.github.com/user', auth=('rinAkhm ', 'Marko@321'))
print (r.status_code)
