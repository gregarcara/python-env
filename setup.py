from setuptools import setup, find_packages


def read(relative):
    with open(relative, 'r') as fin:
        contents = fin.read()
        return [l for l in contents.split('\n') if l != '']


setup(
    name='python-env',
    version='0.0.1',
    description='HP Helion Cloud Sample Python WSGI App',
    author='John Hopper',
    author_email='john.hopper@hp.com',
    url='https://github.com/hpcloud/python-env',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet',
        'Topic :: Utilities'
    ],
    tests_require=read('./requirements.txt'),
    install_requires=read('./requirements.txt'),
    test_suite='nose.collector',
    include_package_data=True,
    packages=find_packages(exclude=['*.tests']))
