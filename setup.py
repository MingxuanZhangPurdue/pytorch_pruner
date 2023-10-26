from setuptools import setup, find_packages

setup(
    name='torch_pruner',
    version="dev",
    url='https://github.com/MingxuanZhangPurdue/pytorch_pruner',
    author='Mingxuan Zhang',
    author_email='zhan3692@purdue.edu',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
    'torch',
    'numpy'
    ]
)