from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
  name='l-converters',
  version='alfa 1.0.0',
  author='Alexandr246',
  author_email='alexandr246@vk.com',
  description='Converters from smt to smt',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Sasha246sasha/l-converters',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)