import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(
	name='portalksp',
	version='0.1',
	author="Muhammad Hasannudin Yusa",
	author_email="emhayusa@gmail.com",
	description="A Portalksp package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/emhayusa/portalksp",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		],
	install_requires=[
        'Click',
    ],
	entry_points={
        "console_scripts": ['portalksp=portalksp.main:welcome']
    },
 )