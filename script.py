import requests, json, os, sys
import urllib.request
from bs4 import BeautifulSoup

image = str(input("image url: "))
print("Request to Tomato.to...")
req = requests.get('https://tomato.to/toma.php?url=' + image)
data_json = json.loads(req.text)["data"]

req2 = requests.get(str(data_json))
data = BeautifulSoup(req2.text, 'html.parser')

images = data.find_all('img', src=True)
images_src = [x['src'] for x in images]
image_src = [x for x in images_src if 'tmp' in x]
print("Image Extracted....")

for image in image_src:
	image_url = image

opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0')
filename, headers = opener.retrieve(image_url, "image.jpg")

print("Image Saved....")

print("Image Size Convertion...")

original_path = str(os.getcwd())
path = original_path + "/image.jpg"

os.chdir('../')
print(str(os.getcwd()))
os.chdir('waifu2x-chainer')


command = f'python waifu2x.py -m noise_scale -n 3 -i "{path}" --arch VGG7 --gpu 0'
os.system(command)
