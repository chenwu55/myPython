#coding= utf-8
import unittest
from driver import *
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.dr=browser()
        self.dr.implicitly_wait(15)
        self.dr.maximize_window()
    def tearDown(self):
        self.dr.quit()

