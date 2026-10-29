import sys
from cx_Freeze import setup , Executable
setup(name = "calculator",
      version = '0.5',
      description = "You Can Used This Calculator",
      executables = [Executable(r"C:\test\project cal.py")]
      )
