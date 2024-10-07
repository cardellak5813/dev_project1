import xml.etree.ElementTree as ET
import re
import json
import yaml

# This section parses xml data #
xml = ET.parse("data.xml")
root = xml.getroot()
ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))

# This section parses json data #
with open('data.json','r') as json_file:
    jsondata = json.load(json_file)
print(jsondata)

# This section parses yaml data #
with open('data.yaml', 'r') as yaml_file:
    yamldata = yaml.load(yaml_file)
print(yamldata)


