import os
import subprocess
import random


subprocess.call("git add *")
print("커밋 메시지를 입력해주세요")
message=input()
subprocess.call('git commit -m'+'"'+message+'"')
subprocess.call("git push origin master")



