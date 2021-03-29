# Note-taking-apps-automation


## Transfer notes from Notion to Obsidian
Automating file transfer between Notion and Obsidian on Mac

### Requirements

[x] unzip Notion files
[x] rename '.md' to specified tile
[x] move Notion files to Obsidian Para - notes
[x] delete the Notion file
[] pass file_name as arguments while running the file
[] pass destination to Para - notes as arguments while running the file


### Specifications

- search the downloads folder for '.zip' files created from Notion
- extract all contents to 'unzipped' folder
- rename '.md' file to the title of the Notion page
- move extracts and the renamed file to Obisdian 'para-notes' folder
- delete '.zip' file to clean up the downloads folder
