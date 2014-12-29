import os
import subprocess
import datetime
import shutil



# Thumbnail size
size = 250




# Grab a list of galleries
galleries = os.listdir("site/content/portfolio/")

for i in galleries :
	if i.startswith(".") :
		galleries.remove(i)


# Generate a list of images
images = {}
for gallery in galleries :
	images[gallery] = os.listdir("site/content/portfolio/%s" % gallery)

	for image in images[gallery] :
		if image.startswith(".") :
			images[gallery].remove(image)







# Generate a front page 
today = datetime.date.today()
with open("site/content/pages/photography.md", "w") as fout :

	# Generate clean image directory
	if os.path.exists("images/portfolio") :
		shutil.rmtree("images/portfolio")
	os.mkdir("images/portfolio")

	# Preamble / metadata
	fout.write("Title: Photography\n")
	fout.write("Date: %d-%d-%d\n" % (today.year, today.month, today.day))
	fout.write("Summary: Photography\n")
	fout.write("save_as: photography.html\n")
	fout.write("slug: photography\n\n")

	
	for gallery in galleries :

		# Generate link to gallery
		fout.write("<a href=\"photo_%s.html\"><img src=\"images/thumb_%s.jpg\" style=\"padding: 30px;\"/></a><br />\n" % (gallery, gallery))

		# Copy the gallery thumbnail over
		shutil.copyfile("site/content/portfolio_thumbs/%s.jpg" % gallery, "images/thumb_%s.jpg" % gallery)







# Generate galleries
for gallery in galleries :

	# For every image in the gallery, generate a thumbnail and move both the thumbnail and the original to upload directory
	os.mkdir("images/portfolio/%s" % gallery)
	commands = ["convert", "-thumbnail", "%dx%d^" % (size, size), "-gravity", "center", "-extent", "%dx%d" % (size, size)]

	for image in images[gallery] :
		title = image.split("_")[1].split(".jpg")[0]
		thiscommand = commands[:]
		thiscommand.append("site/content/portfolio/%s/%s" % (gallery, image))
		thiscommand.append("images/portfolio/%s/thumb_%s" % (gallery, image))
		subprocess.call(thiscommand)
		shutil.copyfile("site/content/portfolio/%s/%s" % (gallery, image), "images/portfolio/%s/%s" % (gallery, image))



	

	# Generate the gallery HTML
	with open("site/content/pages/photo_%s.md" % gallery, "w") as fout :
		fout.write("Title: %s\n" % gallery)
		fout.write("Date: %d-%d-%d\n" % (today.year, today.month, today.day))
		fout.write("Summary: %s\n" % gallery)
		fout.write("save_as: photo_%s.html\n" % gallery)
		fout.write("slug: %s\n\n" % gallery)

		for image in images[gallery] :
			title = image.split("_")[1].split(".jpg")[0]
			fout.write("<a href=\"images/portfolio/%s/%s\" class=\"swipebox\" title=\"%s\">\n" % (gallery, image, title))
			fout.write("\t<img src=\"images/portfolio/%s/thumb_%s\" alt=\"%s\"/>\n" % (gallery, image, title))
			fout.write("</a>\n\n")

		fout.write("\n\n<script type=\"text/javascript\">\n")
		fout.write("\t;( function( $ ) {\n")
		fout.write("\t$( \".swipebox\" ).swipebox();\n")
		fout.write("\t} )( jQuery );\n")
		fout.write("</script>\n\n")












