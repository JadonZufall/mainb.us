import os
import json
from bs4.element import Tag
from bs4 import BeautifulSoup


def main():
	target_file = os.path.join(os.path.sep.join(__file__.split(os.path.sep)[:-2]), "static", "img", "vmdash_bodyclass_images", "image_overview.html")
	if not os.path.exists(target_file):
		raise Exception("Unable to locate target file...")
	try:
		with open(target_file, "r") as file:
			html_content: str = file.read()
	except Exception as e:
		print(e)
		os.abort()
	soup = BeautifulSoup(html_content, "html.parser")

	items = []
	items_by_image = {}
	for tr in soup.find_all("tr"):
		children: list[Tag] = list(filter(lambda x: x != '\n', [i for i in tr.children]))
		if len(children) == 0 or children[0].name != "td":
			continue

		id: str = children[0].text
		name: str = children[1].text
		img_tag_children: list[Tag] = list(filter(lambda x: isinstance(x, Tag), children[2].children))
		if len(img_tag_children) == 0:
			continue
		img_tag: Tag = img_tag_children[0]
		img = img_tag.attrs["src"]
		items.append({"id": id, "name": name, "img": img})
		items_by_image[img] = {"id": id, "name": name, "img": img}
	

	output_path = os.path.join(os.path.sep.join(__file__.split(os.path.sep)[:-2]), "static", "json", "vmdash_bodyclass_images_index.json")
	with open(output_path, "w") as file:
		json.dump({"data": items}, file, indent=4)

	output_path_by_image = os.path.join(os.path.sep.join(__file__.split(os.path.sep)[:-2]), "static", "json", "vmdash_bodyclass_images_by_image.json")
	with open(output_path_by_image, "w") as file:
		json.dump(items_by_image, file, indent=4)
	print("Done")

if __name__ == "__main__":
	main()