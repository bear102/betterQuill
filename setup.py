from setuptools import setup, find_packages

setup(
    name='betterQuill',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pynput',
        'pyperclip',
        'requests'
    ],
)
