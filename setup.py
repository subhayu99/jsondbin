from setuptools import setup, find_packages

setup(
    name='jsondbin',
    version='0.1.2',
    description='Unified Interface for JSON Database with jsonbin.io',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Subhayu Kumar Bala',
    author_email='balasubhayu99@gmail.com',
    url='https://github.com/subhayu99/jsondbin',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
