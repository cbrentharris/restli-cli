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
        'name': 'restli',
        'test_suite': 'nose.collector',
        'tests_require': ['nose', 'mock'],
        'entry_points': { 'console_scripts' : ['restli=restli.command_line:main']}
}

setup(**config)
