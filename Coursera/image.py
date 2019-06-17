import random
import urllib.request
def download_image(url):
	name = random.randrange(1,10)
	full_name = str(name)+ '.jpg'
	urllib.request.urlretrieve(url, full_name)
	
#download_image("https://www.plantronics.com/content/dam/plantronics/images/billboard/open-office-space-gradient.jpg")
download_image("https://scontent-sin6-1.xx.fbcdn.net/v/t1.0-9/21231231_273016429879415_6094889234350344832_n.jpg?_nc_cat=105&_nc_ht=scontent-sin6-1.xx&oh=620137a6cd3483fd4c899a16e632271b&oe=5CCCDEF2")
