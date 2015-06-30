import os



# Grab a list of galleries
galleries = os.listdir("site/content/portfolio/")

for i in galleries :
	if not i.startswith(".") :
		with open("%s.html" % i.lower(), "r") as fin :
			lines = fin.readlines()
		with open("%s.html" % i.lower(), "w") as fout :
			for line in lines :
				fout.write(line.replace("<p><a href", "<a href").replace("</a></p>", "</a>").replace("<div class=\"content\"", "<div class=\"content\" style=\"text-align: left;\""))
