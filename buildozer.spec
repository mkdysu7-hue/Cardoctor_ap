[app]
source.dir = .
version = 0.1
# (str) Title of your application
title = Car Doctor

# (str) Package name
package.name = cardoctor

# (str) Package domain (needed for android packaging)
package.domain = org.cardoc

# (list) Source files to include (let it include python files and text files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) Application requirements
# Specify requirements using python recipe names
requirements = python3,kivy,charset-normalizer,urllib3,idna,certifi,requests

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
