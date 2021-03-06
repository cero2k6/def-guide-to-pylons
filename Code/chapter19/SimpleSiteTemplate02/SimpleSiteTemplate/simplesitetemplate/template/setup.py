try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='SimpleSite',
    version='0.3.0',
    description='''A simple website application written as a demonstration of Pylons for the Definitive Guide to Pylons''',
    author='James Gardner',
    author_email='feeback@pylonsbook.com',
    url='http://pylonsbook.com',
    long_description='''\
++++++++++
SimpleSite
++++++++++

A simple website application allowing WYSIWYG editing, sections and
subsections and full navigation widgets. The idea is that the application can
form a starting point for your own website projects.

Installation
============

First install Easy Install if you don't have it already by downloading
``ez_setup.py`` from http://peak.telecommunity.com/dist/ez_setup.py and
installing it like this::

    python ez_setup.py

Install SimpleSite like this specifying either MySQL, SQLite or PostgreSQL
as the word within the square brackets depending on the database you intend to
use::

    easy_install SimpleSite["MySQL"]
    paster make-config simplesite.ini

Configure the application by editing ``simplesite.ini`` to specify a database
to use using the format described at
http://www.sqlalchemy.org/docs/05/dbengine.html#dbengine_supported ::

    paster setup-app simplesite.ini
    paster serve simplesite.ini

The running application will now be available at http://localhost/

Files
=====
    ''',
    keywords='pylons simple site book example',
    license='BSD, YUI licensed separately at http://developer.yahoo.com/yui/license.html',
    install_requires=[
        "Pylons>=0.9.7,<=0.9.7.99",
        "SQLAlchemy>=0.5,<=0.5.99",
        "Mako>=0.2.2,<=0.2.99",
        "FormBuild>=2.0.1,<=2.0.99",
        "AuthKit>=0.4.3,<=0.4.99",
    ],
    setup_requires=["PasteScript==dev,>=1.6.3dev-r7326"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'simplesite': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'simplesite': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = simplesite.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [paste.filter_app_factory]
    gzip = simplesite.lib.middleware:make_gzip_middleware

    [paste.filter_factory]
    gzip = simplesite.lib.middleware:make_gzip_middleware_filter
    """,
    extras_require = {
        'MySQL': ["mysql-python>=1.2"],
        'PostgreSQL': ["psycopg2"],
    },
)
