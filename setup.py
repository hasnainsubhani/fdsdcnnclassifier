import setuptools

with open ("README.md","r",encoding="utf-8") as f:
    long_descriptions = f.read()


__version__ = "0.0.0"

REPO_NAME = "fdsdcnnclassifier"
AUTHOR_USER_NAME ="HasnainSubhani"
SRC_REPO = "cnnclassifier"
AUTHOR_EMAIL="hasnainsubhani@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description = "A python package for CNN app",
    long_description = long_descriptions,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug TRacker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)