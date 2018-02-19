from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='raefinder',
      version='0.1',
      description='Script to retrieve words from a dictionary that match a certain mnemonic criteria to aid in memorizing numbers',
      url='https://github.com/salvacarrion/raefinder',
      author='Salva Carrión',
      license='MIT',
      packages=find_packages(),
      install_requires=requirements,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'raefinder = raefinder:main'
          ]
      },
      )