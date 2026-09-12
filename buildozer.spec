[app]

# (str) Title of your application
title = Car Doctor

# (str) Package name
package.name = cardoctor

# (str) Package domain (needed for android packaging)
package.domain = org.cardoc

# (list) Source files to include (let it include python files and text files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) Application requirements
requirements = python3,kivy,charset-normalizer,urllib3,idna,certifi,requests

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

source.dir = .
version = 0.1
