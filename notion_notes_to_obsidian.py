import zipfile
import glob
import os
import shutil
import sys

################################################################
# Relationships: 1
# Health and fitness: 2
# Learning: 3
# Finances: 4
# Hobbies: 5
# Professional Development: 6
# Prductivity: 7
# Personal Development: 8

location = 4
file_title = "Analysing Stocks"								# title of the file to rename
################################################################

def find_target_dir(loc):
	switcher={
		4:'/Users/rizwanahmed/Desktop/Google Drive 2/Obsidian Notes/Obsidian Notes/Para - Notes/Finances',
		3:'/Users/rizwanahmed/Desktop/Google Drive 2/Obsidian Notes/Obsidian Notes/Para - Notes/Learning/Permanent Notes'
	}
	return switcher.get(loc,"Invalid destination to Para-Notes folder")

path_to_zip_folder = "/Users/rizwanahmed/Desktop/notion_notes_to_obsidian"
os.chdir(path_to_zip_folder)			# cd to workspace folder
zip_file = glob.glob('*.zip')			# use glob to add file with .zip extension

if zip_file == []:
	sys.exit('No zip file')

# unzip and add the extract to the 'unzipped' folder
for file in zip_file:
	with zipfile.ZipFile(path_to_zip_folder + '/' + file, 'r') as zip_ref:
	    zip_ref.extractall(path_to_zip_folder + "/unzipped")	# extract all thet zip contents to 'unzipped' folder

# rename '.md' file before moving

os.chdir(path_to_zip_folder + "/unzipped")
files_in_unzipped = os.listdir(os.getcwd())
for file in files_in_unzipped:
	f_name, f_ext = os.path.splitext(file)
	if f_ext == '.md':
		new_name = '{}{}'.format(file_title, f_ext)
		os.rename(file, new_name)

# move the contents of the extract to obsidian notes
os.chdir(path_to_zip_folder)
## move to area - learning by renaming the path
source_dir = path_to_zip_folder + "/unzipped"
target_dir = find_target_dir(location)				# target directoty is found using location switcher func 'find_target_dir(location)'


file_names = os.listdir(source_dir)					# list all files in the dir

### cycle through the list and move all files to 'target_dir'
for file_name in file_names:
	shutil.move(os.path.join(source_dir, file_name), target_dir)

# delete the zip file downloaded form notion
for file in zip_file:
	os.remove(file)