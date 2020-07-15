from setuptools import setup

setup(
    name="tblog-cleaner",
    version="0.1.0",
    url="https://github.com/higumachan/tblog-cleaner",
    description="This is tensorboard log cleaner",
    install_requires=["tbparser @ git+https://github.com/velikodniy/tbparser.git", "click"],
    packages=["tblog_cleaner"],
    entry_points={
        "console_scripts": [
            "tblog-cleaner = tblog_cleaner.cli:main"
        ]
    }
)