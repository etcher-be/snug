from pathlib import Path
from setuptools import setup, find_packages

local_path = Path(__file__).parent.joinpath

metadata = {}
exec(local_path('snug/__about__.py').read_text(), metadata)

readme = local_path('README.rst').read_text()
history = local_path('HISTORY.rst').read_text()


setup(
    name='snug',
    version=metadata['__version__'],
    description='Wrap REST APIs to fit nicely into your python code',
    license='MIT',
    long_description=readme + '\n\n' + history,
    url='https://github.com/ariebovenberg/snug',

    author=metadata['__author__'],
    author_email='a.c.bovenberg@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['api', 'wrapper', 'rest', 'orm'],
    install_requires=[
        'requests>=2.13.0,<3',
        'lxml>=3.8.0,<4',
    ],
    python_requires='>=3.6',
    packages=find_packages(exclude=('tests', 'docs', 'examples'))
)
