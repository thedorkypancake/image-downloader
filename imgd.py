from re import fullmatch
import urllib.request

def dl_img(url,file_path,file_name):
    full_path=file_path+file_name+'.jpg'
    urllib.request.urlretrieve(url,full_path)

url=input("Enter image url to download:")
file_name=input("Enter file name to save as:")

dl_img(url,'images/',file_name)
