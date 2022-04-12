import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyworker",
    version="1.0.0",
    author="Jay Lux Ferro",
    author_email="jay@sperixlabs.org",
    description="A simple implementation of a worker-pool process",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jayluxferro/PyWorker",
    project_urls={
        "Bug Tracker": "https://github.com/jayluxferro/PyWorker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
