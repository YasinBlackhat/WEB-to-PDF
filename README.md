# WEB-to-PDF
#### Convert web page (url) to pdf (.pdf) File

This program is written with the help of **Python** and is used to convert **WEB** pages to **PDF**

![alt text](https://raw.githubusercontent.com/YasinBlackhat/WEB-to-PDF/master/web-2-pdf/pic.png)

### Please install the required libraries before running this program
1. pip install PyQt5
2. pip install requests

### Library
```python
import PyQt5
import requests
import json
```
--------------------------------------------------------------------
# How does it work ?

#### With API (REST)

before you start working, you need to open an account on the [restpack](https://restpack.io/) site and use your **key**

# Features

- [x] Fast and easy
- [x] Free
- [x] GUI (Graphic User Interface)
- [x] API (api key)


# Demo
```python
import PyQt5
import requests
import json

url = 'https://restpack.io/api/html2pdf/v6/convert'
headers = {
  'Content-Type': 'application/json',
  'x-access-token': 'Your Token'
}
payload = {
  'url': 'https://github.com/YasinBlackhat', # URL For cinvert to Pdf
  'json': 'true'
}

response = requests.post(url, headers = headers, params = {}, data = json.dumps(payload))
response.raise_for_status()
k = response.json()

file_loc = k['file']
r = requests.get(file_loc)

with open('blackhat.pdf', 'wb') as f:
    f.write(r.content)
```

#### Thank You.
