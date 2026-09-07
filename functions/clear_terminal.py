import os
import subprocess

def clear_terminal():
   if os.name == "nt":
      subprocess.run("cls", shell=True, check=False)
   else:
      subprocess.run("clear", shell=True, check=False)