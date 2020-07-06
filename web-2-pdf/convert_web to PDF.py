# Follow we ** https://github.com/YasinBlackhat **
# @ !
import requests
import json

in_url = str(input('Enter Your URl Address : ')) # Address => https:\\www.google.com
loc = str(input('Enter Your Address Location : ')) # Location => C:\\
print('Loading...')

url = 'https://restpack.io/api/html2pdf/v6/convert'
headers = {
  'Content-Type': 'application/json',
  'x-access-token': 'hHc5xxoTEc5x4EBAjunfG8gQk6g6MEMF7PmB78qjJHYpieLB' # Token or Key 
}
payload = {
  'url': in_url, # URL For cinvert to Pdf
  'json': 'true'
}

response = requests.post(url, headers = headers, params = {}, data = json.dumps(payload))

response.raise_for_status()

k = response.json()

file_loc = k['file']
r = requests.get(file_loc)

l = loc+'/blachat.pdf'
with open(l, 'wb') as f:
    f.write(r.content)
print('Done !!')