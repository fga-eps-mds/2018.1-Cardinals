from django.test import TestCase
import pdfcrowd
from .views import config_convert_img, convert_html2image
from .views import create_pdf_paragraph, create_pdf_space
from .views import create_pdf_img


class ReportTests(TestCase):


   def setUp(self):
      self.path_html = 'static/images/charts/chart_commit.html'
      self.path_jpg = 'static/images/charts/chart_commit.jpg'
      self.text = "Cardinals"
      self.size = 12
      self.Story = []
      self.test_list = []
      self.test_img_obj = config_convert_img()

   def test_config_convert_img(self):
      self.img_test = config_convert_img()
      self.assertNotEqual(config_convert_img(), self.img_test)

   def test_create_pdf_space(self):
      create_pdf_space(self.Story, self.size)
      create_pdf_space(self.test_list, self.size)
      self.assertNotEqual(self.Story, self.test_list)

   def test_convert_html2image(self):
      self.img_test = config_convert_img()
      self.assertEqual(convert_html2image(self.img_test, self.path_html, self.path_jpg), self.path_jpg)
      self.assertNotEqual(convert_html2image(self.img_test, self.path_html, self.path_jpg), self.img_test)

   def test_create_pdf_paragraph(self):
      create_pdf_paragraph(self.Story, self.text, self.size)
      create_pdf_paragraph(self.test_list, self.text, self.size)
      self.assertNotEqual(self.Story, self.test_list)

   def test_create_pdf_img(self):
      create_pdf_img(self.Story, self.test_img_obj, self.path_html)
      create_pdf_img(self.test_list, self.test_img_obj, self.path_html)
      self.assertNotEqual(self.Story, self.test_list)