import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site do YT não está acessível!')
else:
    print('Tá bom todo, pode usar!')