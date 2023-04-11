#%%
import requests
from pprint import pprint
from PIL import Image
import os
import datetime

#api url as str
url = 'https://randomuser.me/api/'
#call api, return json file
data= requests.get(url).json()

#parse key:value data to define users
user = data['results'][0]

#scrape json file for desired data
print(f"Name: {user['name']['first']}" ", " f"{user['name']['last']}")
print(f"Gender: {user['gender']}")
print(f"DOB: {user['dob']['date']}")
print(f"Age: {user['dob']['age']}")

#uncomment below to print key:value pairs
#pprint(data)

#save photo value
photo = user['picture']['large']
#convert photo variable to str for call
image_url = str(photo)
#call image_url
image_request = requests.get(image_url)

#before content can be viewed, content must be saved as image variable
path=os.path.join(os.getcwd(),'image.png')
path

#file 'path' is opened in wb -> 'write binary'
with open(path,'wb') as f:
    f.write(image_request.content)
#display image from url variable
Image.open(path)
# %%
