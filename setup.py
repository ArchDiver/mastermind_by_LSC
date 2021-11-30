from distutils.core import setup

setup(
    name="mastermind",
    version="0.1.0",
    py_modules=["mastermind"],
    install_requires=open("requirements.txt").readlines(),
    entry_points={
        "console_scripts": [
            "mastermind-terminal = mastermind.mastermind_terminalUI:main",
        ]
    },
)