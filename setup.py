from setuptools import setup

from torch_pruner import __version__

setup(
    name='pytorch_pruner',
    version=__version__,
    url='https://github.com/MingxuanZhangPurdue/pytorch_pruner',
    author='Mingxuan Zhang',
    author_email='zhan3692@purdue.edu',
    py_modules=['torch_pruner'],
)