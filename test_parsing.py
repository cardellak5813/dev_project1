import unittest
from parse_data import *

class parse_test(unittest.TestCase):
    def test_xml_data(self):
        self.assertTrue(defop.text == 'merge')
    def test_json_data(self):
        self.assertTrue(jsonKey == 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3')
    def test_yaml_data(self):
        self.assertTrue(yamlKey == 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3')
