from setuptools import setup

setup(
	name = "cli-ticket-manager",
	version = "0.1.0",
	packages = ["cli_ticket_manager"],
    entry_points = {
        "console_scripts": [
            "ctm=cli_ticket_manager.__main__:main"
        ]
    })