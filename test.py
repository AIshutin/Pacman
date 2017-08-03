#Test module
import subprocess
cmd = 'helper.bat'
PIPE = subprocess.PIPE
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
