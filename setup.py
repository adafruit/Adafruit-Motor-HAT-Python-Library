try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']


setup(name              = 'Adafruit_MotorHAT',
      version           = '1.4.0',
      author            = 'Limor Fried',
      author_email      = 'support@adafruit.com',
      description       = 'Library for Adafruit Motor HAT',
      license           = 'MIT',
      url               = 'https://github.com/adafruit/Adafruit_Python_MotorHAT/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.7'],
      install_requires  = ['Adafruit-GPIO>=0.7'],
      packages          = find_packages())
