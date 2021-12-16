from setuptools import setup


with open('README.md') as file:
    long_description = file.read()


# TODO - replace with details of your project
setup(
    name='munna',
    description='Pokemon Showdown MatchUp Neural Network Analysis',
    version='0.0.1',
    author='Caedon Hsieh',
    author_email='caedonhsieh@gmail.com',
    url='https://github.com/caedonhsieh/ps-munna',
    install_requires=['pytorch-lightning'],
    packages=['munna'],
    package_data={'munna': ['assets/*']},
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[],
    classifiers=['License :: OSI Approved :: MIT License'],
    license='MIT')
