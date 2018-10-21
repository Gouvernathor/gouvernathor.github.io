import sys
import json

filename = "_build/_config_tpl.yml"

languages = {
	"en_US": "English",
	"fr_FR": "Français"
}

with open(filename, 'r') as f:
	current_line = None
	counter = 0
	line_buffer = []
	for line in f:
		if line.find("{{BUILD.TRANSLATIONS}}") >= 0:
			print("t:")
			for lcode, lname in languages.items():
				print("   "+lcode+":")
				with open("_build/translation_"+lcode+".json") as translationFile:
					data = json.load(translationFile)
					for tcode, tstring in data.items():
						print("      "+tcode+": \""+tstring.replace("\"", "\\\"")+"\"")
		elif line.find("{{BUILD.LANGUAGES}}") >= 0:
			for lcode, lname in languages.items():
				print("   "+lcode+":")
				print("      permalink: "+lcode+"/:name/")
				print("      title: "+lname)
				print("      output: true")
		else:
			print(line.replace("\n", ""))

