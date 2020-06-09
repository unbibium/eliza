import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()


setuptools.setup(
    name="example-pkg-unbibium", # Replace with your own username
    version="0.0.1",
    author="Nick Bensema",
    description="A rudimentary chatbot powered by wit.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'snowboy',
        'speech-recognition',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS X",
    ],
    python_requires='>=3.6',
)
