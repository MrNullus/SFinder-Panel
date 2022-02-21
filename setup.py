from ensurepip import version
from http.server import executable
from ssl import Options
from unicodedata import name
from cx_Freeze import setup, Executable


dependencies = {"packages": ["requests"], "includes": ["colorama"], "includes": ["time"], "includes": ["os"], "includes": ["platform"]}

setup(
    name = "Admin Stark",
    version = "1.0",
    description = "GitHub:https://github.com/SrStark666",
    options = {"build_exe": dependencies},
    executables = [Executable("admin.py")]
)