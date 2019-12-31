# -*- coding: utf-8 -*-

"""Post generation script"""

import os
import random
import string

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_FILES = (".dockerignore", "docker-compose.yml")


def generate_random_string(
    length=25, allowed_chars=string.ascii_letters + string.digits
):
    """
    Generate a random string.

    :param length: The length of the desired string
    :type length: int
    :param allowed_chars: The set of allowed characters
    :type allowed_chars: str
    :returns: Random string
    :rtype: str
    """
    return "".join(random.choice(allowed_chars) for i in range(length))


def remove_file(filepath):
    """
    Remove a file with the given path.

    :param str filepath: Path of the file.
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.use_docker }}".lower() in ("n", "no"):
        for filename in DOCKER_FILES:
            remove_file(filename)
