from setuptools import setup, find_packages

setup(
    name="lab_2",
    version="1.1",
    packages=find_packages(),
    install_requires=["pytest", "pytest-cov", "coverage"],
    url="https://t.me",
    license="Мб какая-нибудь есть",
    author="Vlad Kuzma",
    description="Обычная вторая лаба",
    extras_require={
        "tests": ["python-dotenv"],
        "dev": [
            "pytest",
            "pytest-cov",
            "coverage",
           ],
    },
)
