from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'Adafruit_MotorHAT',
      version           = '1.0.0',
      author            = 'Limor Fried',
      author_email      = 'support@adafruit.com',
      description       = 'Library for Adafruit Motor HAT',
      license           = 'MIT',
      url               = 'https://github.com/adafruit/Adafruit_Python_MotorHAT/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.7'],
      install_requires  = ['Adafruit-GPIO>=0.7'],
      packages          = find_packages())
