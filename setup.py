from setuptools import setup, find_packages


VERSION = __import__("lists").__version__

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]

install_requires = [
    'Django>=1.4.2',
]

setup(
    name="django-lists",
    description="Django lists app",
    version=VERSION,
    author="Informatika Mihelac",
    author_email="bmihelac@mihelac.org",
    url="https://github.com/bmihelac/django-lists",
    packages=find_packages(exclude=["tests"]),
    package_data={},
    install_requires=install_requires,
)
