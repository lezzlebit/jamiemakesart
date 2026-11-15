import urllib.request
import time



def get_image_url(input):

	dict = {}
	input_contents = input.split('"')
	for c in input_contents:
		if "wp-content" in c:
			dict["content"] = c
		if "halo-head.com/comic" in c:
			dict["next"] = c

	return dict
image_urls = ["https://halo-head.com/wp-content/uploads/2020/06/hh-1.png"]

next_page = "https://halo-head.com/comic/2"

def save_image_urls():
	to_save = "["
	for s in image_urls:
		to_save += '"' + s + '",'

	to_save = to_save[:-1]
	to_save += "]"
	with open("pages.txt", "w") as f:
		f.write(to_save)


for g in range(2, 600):
	page = urllib.request.urlopen(next_page)
	contents = page.read().decode("utf-8").split("\n")


	

	scan_indices = 0
	for i in contents:
		if 'id="comic"' in i:
			scan_indices = 5
		scan_indices -= 1
		if scan_indices > 0:
			if "wp-content" in i:
				dict = get_image_url(i)
				print(dict["content"])
				image_urls.append(dict["content"])
				next_page = dict["next"]

	

	save_image_urls()
	time.sleep(1)