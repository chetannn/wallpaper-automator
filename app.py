import requests
from app_key import api_key 
import os
import time
import wget
import ctypes

def get_wallpaper():
  url = f'https://api.unsplash.com/photos/random?client_id={api_key}'
  params = {
		'query': 'HD wallpapers',
		'orientation': 'landscape'
	}
  response = requests.get(url, params = params).json()
  image_src = response['urls']['full']
  image = wget.download(image_src, './tmp/wallpaper.jpg')
  return image


def set_wallpaper():
  image = get_wallpaper()
  SPI_SETDESKWALLPAPER = 20 
  abs_path = os.path.abspath(image)
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, abs_path , 0)

def main():
    set_wallpaper()

if __name__ == '__main__':
  main()