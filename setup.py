import os
from os.path import abspath, dirname, join, isfile
from setuptools import find_packages, setup

__copyright__ = ("Flensburg University of Applied Sciences, "
                 "Europa-Universität Flensburg, "
                 "Centre for Sustainable Energy Systems")
__license__ = "GNU Affero General Public License Version 3 (AGPL-3.0)"
__author__ = "wolf_bunke, maltesc"


# files
README_MD = "README.md"
README_RST = "README.rst"

cur_dir = abspath(dirname(__file__))
readme_md = join(cur_dir, README_MD)
readme_rst = join(cur_dir, README_RST)

long_description = ""
using_rst = False
try:
    with open(readme_rst, 'r') as f:
        long_description = f.read()
        using_rst = True
except IOError:
    with open(readme_md, 'r') as f:
        long_description = f.read()




setup(name='eGo',
      version='0.3.0',
      author='wolfbunke, maltesc',
      author_email='',
      description=("A python package for distribution and transmission"
                   "grid analysis and optimization based eDisGo and eTraGo"),
      long_description=long_description,
      long_description_content_type="text/x-rst",
      url='https://github.com/openego/eGo',
      license="GNU Affero General Public License Version 3 (AGPL-3.0)",
      packages=find_packages(),
      package_dir={'ego': 'ego'},
      include_package_data=True,
      install_requires=['egoio==0.4.5',
                        'eDisGo==v0.0.6',
                        'eTraGo==0.7.0',
                        'pandas==0.20.3',
                        'pypsa==0.11.0fork',
                        'geoalchemy2>= 0.3.0, <=0.4.0',
                        'pyproj==1.9.5.1',
                        'geopandas',
                        'matplotlib>= 1.5.3, <=1.5.3',
                        'Rtree',
                        'descartes',
                        'plotly==2.2.3',
                        'Pyomo==5.5.0',
                        'oedialect',
                        'multiprocess',
                        'folium'
                        ],
      dependency_links=[('git+https://git@github.com/openego/PyPSA.git'
                         '@master#egg=pypsa-0.11.0fork')],
      extras_require={
          'doc': [
              'sphinx >= 1.4',
              'sphinx_rtd_theme',
              'sphinxcontrib-httpdomain']},
      package_data={
          'ego': [os.path.join('tools', '*.csv')],
          'ego': [os.path.join('tools', '*.json')],
          'ego': [os.path.join('', '*.json')],
          'ego.data': ['*.csv']
      },
      )
