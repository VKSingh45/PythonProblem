from cx_Freeze import setup, Executable
base = None
executables = [Executable("S.py",base=base)]
packages = ["idna"]
options = {
    'build_exe':{
        'packages':packages,
        },
    }
setup(
    name = "Billing System ",
    options = options,
    version = "2.0",
    description = 'Billing System Project Work',
    executables = executables
    )
