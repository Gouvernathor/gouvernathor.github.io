import sys
import json

configFn = "_build/_config_tpl.yml"
languagesFn = "_build/languages.csv"

languages = {}
with open(languagesFn, 'r') as f:
	for line in f:
		(lcode, lname, ldir) = line.split(";")
		languages[lcode] = { "name":lname, "dir":ldir }

with open(configFn, 'r') as f:
	current_line = None
	counter = 0
	line_buffer = []
	for line in f:
		if line.find("{{BUILD.TRANSLATIONS}}") >= 0:
			print("t:")
			for lcode, ldata in languages.items():
				print("   "+lcode+":")
				with open("_build/translation_"+lcode+".json") as translationFile:
					print("      wdir: "+ldata["dir"])
					
					data = json.load(translationFile)
					for tcode, tstring in data.items():
						print("      "+tcode+": \""+tstring.replace("\"", "\\\"")+"\"")
		elif line.find("{{BUILD.LANGUAGES}}") >= 0:
			for lcode, ldata in languages.items():
				print("   "+lcode+":")
				print("      permalink: "+lcode+"/:name/")
				print("      title: "+ldata["name"])
				print("      output: true")
		else:
			print(line.replace("\n", ""))

