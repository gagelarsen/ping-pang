import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'argparse >= 1.4.0',
    'requests >= 2.24.0'
]

setuptools.setup(
    name='ping-pang',
    version='1.0.0',
    description='Ping a URL and output the status code and latency. Save to a log or CSV on an interval.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/ping-pang',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pylint >= 2.5.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'ping-pang=pingpang.ping_logic:main'
        ]
    },
    python_requires='>=3.6',
)