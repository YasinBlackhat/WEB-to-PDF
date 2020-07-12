# Follow me ** https://github.com/YasinBlackhat **
import requests
import json
# import library

in_url = str(input('Enter Your URl Address : ')) # Address => https:\\www.google.com
loc = str(input('Enter Your Address Location : ')) # Location => C:\\

 while in_url == '' and loc == '': # Check the empty values
      print('Humm    + Fill in the blanks +')
      in_url = str(input('Enter Your URl Address : ')) # URL
      loc = str(input('Enter Your Address Location : ')) # Location
      
def getting(in_url): # Function Convert web to PDF
    print('Loading...')

    url = 'https://restpack.io/api/html2pdf/v6/convert' # API url
   
    headers = { # Header Api
      'Content-Type': 'application/json',
      'x-access-token': 'hHc5xxoTEc5x4EBAjunfG8gQk6g6MEMF7PmB78qjJHYpieLB' # Token or Key 
    }
    payload = { # Payload Api
      'url': in_url, # URL For cinvert to Pdf
      'json': 'true'
    }

    response = requests.post(url, headers = headers, params = {}, data = json.dumps(payload)) # (get) request
    response.raise_for_status()
    k = response.json() # get response Json
    file_loc = k['file'] 
    r = requests.get(file_loc)
    return r
  
r = geting(in_url) # get file url for Download
loc = loc+'/blachat.pdf'
with open(loc, 'wb') as f:
    f.write(r.content)
    
print('Done !! ): ') # Down Thank You..
