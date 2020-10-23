import os.path
import os
from os.path import expanduser
import re
from shutil import copyfile


SAVED_FILE = './saved_id'
UNIX_FOLDER_PREFIX = '/.mozilla/firefox/'
UNIX_FOLDER_POSTFIX = '.default/'
WINDOWS_FOLDER_PREFIX = '%APPDATA%/Mozilla/Firefox/Profiles/'
WINDOWS_FOLDER_POSTFIX = '.default/'


def pre_exist():
    if os.path.isfile(SAVED_FILE):
        with open(SAVED_FILE, 'r') as f:
            return f.read()
    else:
        return


def store_id(pid):
    with open(SAVED_FILE, 'w') as f:
        f.write(pid)


# Step 1: check if profile ID exists.
pid = pre_exist()
if pid:
    pass
else:
    print('Enter your firefox profile id:')
    pid = input()
    store_id(pid)
folder = expanduser('~')+UNIX_FOLDER_PREFIX+pid+UNIX_FOLDER_POSTFIX if os.name == 'posix' else \
    WINDOWS_FOLDER_PREFIX+pid+WINDOWS_FOLDER_POSTFIX if os.name == 'nt' else None

# Step 2: choose color scheme
color_schemes = next(os.walk('.'))[1]
non_hidden_check = re.compile(r'^[^\.].*')
color_schemes = [x for x in color_schemes if non_hidden_check.match(x)]
print('Choose your scheme:')
for i, cs in enumerate(color_schemes):
    print(i, cs)
i = int(input())
scheme_folder = color_schemes[i]


# Step 3: Copy and paste to the target folder
print('Chosen scheme: '+scheme_folder)
print('Copying to" '+folder)
# Create chrome folder
if not os.path.exists(folder+'chrome'):
    os.makedirs(folder+'chrome')
copyfile('./'+scheme_folder+'/userContent.css', folder+'chrome/userContent.css')
copyfile('./'+scheme_folder+'/user.js', folder+'user.js')
print('Done')