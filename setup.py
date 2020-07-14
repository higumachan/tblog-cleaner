from setuptools import setup

setup(
    name="tblog-cleaner",
    url="https://github.com/higumachan/tblog-cleaner",
    description="This is tensorboard log cleaner",
    install_requires=["tbparser", "click"],
    dependency_links=['https://github.com/velikodniy/tbparser.git#egg=tbparser'],
    entry_points={
        "console_scripts": [
            "tblog-cleaner = main:main"
        ]
    }
)