from setuptools import setup, find_packages

setup(
    name='Carboncalc',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib'
    ],
    description='Un package pour calculer les émissions de CO2 basées sur les données de consommation utilisateur',
    author='MEBARKA Sheima',
    author_email='sheima.meb@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
