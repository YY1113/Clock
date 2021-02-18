import os
import subprocess

subprocess.call("git add *")
subprocess.call('git commit -m"4test"')
subprocess.call("git push origin master")



