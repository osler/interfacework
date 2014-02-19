import urllib.request
import shutil
import os

locale = input("Please enter your locale (enGB, deDE, ruRU...): ")

print ("Downloading AccountLogin.xml...")
data = urllib.request.urlretrieve("https://raw2.github.com/osler/interfacework/master/GlueXML/AccountLogin.xml", "AccountLogin.xml")

print ("Downloading AccountLogin.lua...")
data = urllib.request.urlretrieve("https://raw2.github.com/osler/interfacework/master/GlueXML/AccountLogin.lua", "AccountLogin.lua")

print ("Downloading file.html...")
data = urllib.request.urlretrieve("https://raw2.github.com/osler/interfacework/master/GlueXML/file.html", "file.html")

if not os.path.exists("interface/GlueXML"):
	print("Creating interface directory...")
	os.makedirs("interface/GlueXML")

if not os.path.exists("data/"+locale):
	print("Creating locale directory...")
	os.makedirs("data/"+locale)

print ("Moving AccountLogin.xml...")
shutil.move("AccountLogin.xml", "interface/GlueXML/AccountLogin.xml")

print ("Moving AccountLogin.lua...")
shutil.move("AccountLogin.lua", "interface/GlueXML/AccountLogin.lua")

print ("Moving file.html...")
shutil.move("file.html", "data/" + locale + "/file.html")

print ("Installation completed!")
input("Press enter to exit")