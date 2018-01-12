from cx_Freeze import setup, Executable

base = None


executables = [Executable("MathMaster.py", base=base, icon='icon.ico')]

packages = ["idna"]
include_files = []

options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files,
    },

}

setup(
    name="MathMaster",
    options=options,
    version="1.0.2",
    description='A program for basic and advanced mathematical calculations',
    executables=executables
)