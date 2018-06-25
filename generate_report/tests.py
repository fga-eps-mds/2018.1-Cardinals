from django.test import TestCase
import pdfcrowd
from .views import config_convert_img, convert_html2image


class ReportTests(TestCase):


   def setUp(self):
      self.path_html = 'static/images/charts/chart_commit.html'
      self.path_jpg = 'static/images/charts/chart_commit.jpg'

   def test_config_convert_img(self):
      self.img_test = config_convert_img()
      self.assertNotEqual(config_convert_img(), self.img_test)


   def test_convert_html2image(self):
      self.img_test = config_convert_img()
      self.assertEqual(convert_html2image(self.img_test, self.path_html, self.path_jpg), self.path_jpg)
      self.assertNotEqual(convert_html2image(self.img_test, self.path_html, self.path_jpg), self.img_test)