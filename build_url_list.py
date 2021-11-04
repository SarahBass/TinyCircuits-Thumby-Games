# https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/

import os
from posixpath import dirname
print("Starting URL list builder using Python in GH Action...")

# Each game's asset is appended to the end of this, like https://raw.githubusercontent.com/TinyCircuits/TinyCircuits-Thumby-Games/master/MyGame/MyGame.py
raw_url_base = "https://raw.githubusercontent.com/TinyCircuits/TinyCircuits-Thumby-Games/master/"

# Open file that urls will be written to
f = open("url_list.txt", "w")

def addDirFilesToList(parentDir):
    items = os.listdir(parentDir)
    for item in items:
        if os.path.isdir(item):
            addDirFilesToList(item)
        else:
            f.write(raw_url_base + item)


topLevelItems = os.listdir()

# Start looping through items in the root of the repo, ignore .github,
# and add file under each directory recursively
print(topLevelItems)
for item in topLevelItems:
    if os.path.isdir(item) and item != ".github" and item != ".git":
        addDirFilesToList(item)
        f.write("\n")


# Close file that urls were written to
f.close()