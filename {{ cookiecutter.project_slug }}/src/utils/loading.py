# pylint: disable=E0401
import importlib
import os


def start_loading():
    if getattr(sys, "frozen", False):
        import pyi_splash

        pyi_splash.update_text("Desenvovido por {{ cookiecutter.author_name }}.")
        pyi_splash.close()
