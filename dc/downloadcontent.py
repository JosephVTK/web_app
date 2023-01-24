import requests
import shutil

from xml.dom.minidom import parseString

URL = "https://static.sfo3.digitaloceanspaces.com"

def download_image(url):
    image_url = URL + '/' + url

    filename = url.split('/')[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

xml_list = requests.get(URL)

urls = parseString(xml_list.content.decode())

keys = urls.getElementsByTagName('Key')

url_list = []
for key in keys:
    for c in key.childNodes:
        url_list.append(c.wholeText)

url_list

for url in url_list:
    download_image(url)
