import os
import sys
import subprocess

local, remote = sys.argv[1:]
for d in os.listdir(local):
    f = os.path.join(local,d)
    if (os.path.isfile(f)):
        print f
        subprocess.check_call('adb push "'+f+'" "'+remote+'"', shell=True)
        subprocess.check_call('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard')
