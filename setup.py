from setuptools import setup

setup(name='pyedimax',
      version='0.1',
      description='Interface with Edimax Smart Plugs',
      url='https://github.com/rkabadi/pyedimax',
      author='Rohit Kabadi',
      author_email='rkabadi06@gmail.com',
      license='MIT',
      install_requires=['requests>=2.0'],
      packages=['pyedimax'],
      zip_safe=False)