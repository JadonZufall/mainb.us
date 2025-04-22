src = "\\".join(__file__.split("\\")[:-1]) + "\\iso.csv"
fp = "\\".join(__file__.split("\\")[:-1]) + "\\cur.yaml"
with open(src, "r") as file:
	data = file.read()
data = data.split("\n")
_ = data.pop(0)
with open(fp, "w") as file:
	for i, line in enumerate(data):
		sym, name = line.split(",")
		file.write("- model: apps.location.Currency\n")
		file.write(f"  pk: {i+1}\n")
		file.write("  fields:\n")
		file.write(f"    name: {name}\n")
		file.write(f"    iso: {sym}\n")
		file.write("\n")