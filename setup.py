import setuptools


with open('readme.md', encoding='utf8') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='liber',
    version='0.0.1',
    author='RimoChan',
    author_email='the@librian.it',
    description='A library to compile liber.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/librian-center/liber-language',
    packages=['liber'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
