import inquirer
import os
import re
from pprint import pprint


def select():
    profiles = [re.findall(r'\[(.*?)\]',line) for line in open(os.path.expanduser("~/.aws/credentials"))]
    profile_list = [item for sublist in profiles for item in sublist]
    selection = inquire("profile", "Select profile", profile_list)
    selected = selection['profile']

    return selected


def inquire(name, desc, choice):
    questions = [
        inquirer.List(
            name,
            message=desc,
            choices=choice,
        ),
    ]
    selection = inquirer.prompt(questions)

    return selection
