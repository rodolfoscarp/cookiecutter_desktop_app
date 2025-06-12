# pylint: disable=E0401
import importlib
import os


def start_loading():
    if "_PYIBoot_SPLASH" in os.environ and importlib.util.find_spec("pyi_splash"):
        import pyi_splash

        pyi_splash.update_text("Desenvovido por {{ cookiecutter.author_name }}.")
        pyi_splash.close()
