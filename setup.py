from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='mplbrowser',
    version='dev',
    description='Display matplotlib image in browser',
    author='Yanze Wu',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        'matplotlib >= 3.0.0',
        'flask >= 1.1'
    ],
)
