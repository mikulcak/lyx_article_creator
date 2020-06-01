import shutil
import os
import sys

if len(sys.argv) < 4:
	print("Not enough arguments, expected script path, article name, and article author")
	sys.exit()

current_working_directory = sys.argv[1]
article_name = sys.argv[2]
article_author = sys.argv[3]

# print(current_working_directory)

# article_name = "cool_conference_paper"
# article_author = "The Author"

bib_location = "/Users/marcus/Nextcloud/bibliography_zotero_export/bibliography"
paper_base_folder = "/Users/marcus/Desktop"


destination_folder = os.path.join(paper_base_folder, article_name)

template_folder = os.path.join(current_working_directory, "template_files")
template_biblatex_files = ["add_letter_bib_type.tex", "english-letter.lbx", "letter.dbx"]
template_lyx_file = "lyx_template.lyx"

def append_extension(filename, extension):
	if not filename.endswith(extension):
		return filename + "." + extension




if os.path.exists(destination_folder):
	print("For safety reasons, let's not overwrite existing directories")
	sys.exit()
else:
	os.mkdir(destination_folder)
	os.mkdir(os.path.join(destination_folder, "figures"))


# copy BibLaTeX template files
for file in template_biblatex_files:
	shutil.copyfile(os.path.join(template_folder, file), os.path.join(destination_folder, file))


# copy and edit lyx template
with open(os.path.join(template_folder, template_lyx_file), 'r') as content_file:
    content = content_file.read()
    with open(os.path.join(destination_folder, append_extension(article_name, "lyx")), 'w') as destination_lyx_file:
	    for line in content.split('\n'):
	    	if "my_author" in line:
	    		line = line.replace("my_author", article_author)
	    	if "my_title" in line:
	    		line = line.replace("my_title", article_name)
	    	if "my_bib_location" in line:
	    		line = line.replace("my_bib_location", bib_location)
	    	destination_lyx_file.write(line + '\n')

print("Done. I have created your paper %s in %s" % (article_name, destination_folder))