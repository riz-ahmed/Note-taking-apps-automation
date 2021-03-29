import zipfile
import glob
import os
import shutil
import sys

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

file_title = "Habits of rich people that non-rich don't have"								# title of the file to rename

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
target_dir = '/Users/rizwanahmed/Desktop/Google Drive 2/Obsidian Notes/Obsidian Notes/Para - Notes/Learning/Permanent Notes'

file_names = os.listdir(source_dir)					# list all files in the dir

### cycle through the list and move all files to 'target_dir'
for file_name in file_names:
	shutil.move(os.path.join(source_dir, file_name), target_dir)

# delete the zip file downloaded form notion
for file in zip_file:
	os.remove(file)