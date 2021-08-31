from setuptools import setup, find_packages


setup(
    name='mkdocs-multisite',
    version='0.0.1',
    description='A MkDocs plugin to switch between multiple versions of your site',
    long_description='A MkDocs plugin to switch between multiple versions of your site\n\n# Overview\n\nFIXME',
    keywords='mkdocs',
    url='',
    author='Zach White',
    author_email='skullydazed@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'multisite = mkdocs_multisite.plugin:MultiSite'
        ]
    }
)
