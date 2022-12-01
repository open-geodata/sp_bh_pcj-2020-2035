"""
Setup
"""

from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

requirements = []
for line in open('requirements.txt', encoding='utf-8'):
    li = line.strip()
    if not li.startswith('#'):
        requirements.append(line.rstrip())

VERSION = (0, 0, 6)
__version__ = '.'.join(map(str, VERSION))

setup(
    name='sp_bh_pcj_2020_2035',
    version=__version__,
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='Dados Espaciais da Agência das Bacias PCJ, com informações apresentadas no Plano de Bacias 2020-2035',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/open-geodata/sp_bh_pcj-2020-2035',
    keywords='python, dados espaciais, geoprocessamento',
    # Python and Packages
    python_requires='>=3',
    install_requires=requirements,
    # Classificação
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
    # Entry
    # package_dir={'': 'sp_bh_pcj_2020_2035'},  # Our packages live under src but src is not a package itself
    # Quando são diversos módulos...
    packages=find_packages(),
    # Dados
    include_package_data=True,
    package_data={'': ['data/output/zips/*.7z']},
)
