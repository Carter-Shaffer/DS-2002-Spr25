#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import os

HOMETOWN = input('What is your Hometown?: ')
MAJOR = input('What is your major?: ')
FAVORITE_HOBBY = input('What is your favorite hobby?: ')

os.environ["HOMETOWN"] = HOMETOWN
os.environ["MAJOR"] = MAJOR
os.environ["FAVORITE_HOBBY"] = FAVORITE_HOBBY

print(os.getenv("HOMETOWN"))
print(os.getenv("MAJOR"))
print(os.getenv("FAVORITE_HOBBY"))
