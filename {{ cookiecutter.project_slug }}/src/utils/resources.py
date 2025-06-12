import os
import sys
from pathlib import Path


def get_resources_dir():
    """
    Returns the absolute path of the resources directory.

    When the application is frozen with pyinstaller, it returns the absolute
    path of the resources directory inside the bundle.
    Otherwise, it returns the absolute path of the resources directory in the
    current working directory.

    :return: The absolute path of the resources directory
    :rtype: Path
    """

    if getattr(sys, "frozen", False):

        bundle_dir = os.path.dirname(sys.executable)
    else:
        bundle_dir = os.getcwd()

    return Path(bundle_dir).joinpath("resources").resolve()


def get_resource_path(filename: str) -> Path:
    """
    Returns the absolute path of a resource file.

    :param filename: The name of the resource file
    :type filename: str
    :return: The absolute path of the resource file
    :rtype: Path
    """

    return get_resources_dir().joinpath(filename)
