try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
        'description': 'Command line tools for scaffolding a Rest.li project',
        'author': 'Christopher Harris',
        'url': '',
        'author_email': 'cbrentharris@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['restli'],
        'scripts':[],
        'name': 'restli'
}

setup(**config)
