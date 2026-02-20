from setuptools import setup, find_packages

setup(
    name='kenosms',                     # jina la package kwenye PyPI
    version='0.1.0',                    # version ya release
    packages=find_packages(),            # automatic discover sub-packages
    install_requires=[
        'requests',                     # dependencies
    ],
    description='Python SDK for KenoSMS API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fortunatus Chrispin Rwekiti',
    author_email='your_email@example.com',
    url='https://github.com/phortkid/kenosms_python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)