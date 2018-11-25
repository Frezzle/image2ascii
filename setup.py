import setuptools

setuptools.setup(
    name="image2ascii",
    version="0.0.1",
    author="Frederico Mazzone",
    description="Convert images to ASCII art.",
    long_description="Convert images to ASCII art.",
    long_description_content_type="text/markdown",
    url="https://github.com/Frezzle/image2ascii",
    packages=setuptools.find_packages(),
    install_requires=[
        "Pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense",
        "Operating System :: OS Independent",
    ],
)
