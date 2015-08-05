import glob
import os
from distutils.core import setup

setup(name='spearmint',
      description="Practical Bayesian Optimization of Machine Learning Algorithms",
      author="Jasper Snoek, Hugo Larochelle, Ryan P. Adams",
      url="https://github.com/JasperSnoek/spearmint",
      version='1.0',
      license='GPLv3',
      scripts=['bin/spearmint', 'bin/cleanup'],
      packages=['spearmint', 'spearmint/driver', 'spearmint/chooser',
                'spearmint/web'],
     )
