# 每天第1次接触电脑时运行py3 GitTool.py --update
# 每天第-1次接触电脑时运行py3 GitTool.py --commit

import sys
import os
dir_list = ["~/myblog/", "~/3xp10it.github.io/",
            "~/exp10it/", "~/mytools/", "~/pic/", "~/note", "~/xag"]
if sys.argv[1] == "--update":
    for each_dir in dir_list:
        os.system("cd %s && git pull" % each_dir)
if sys.argv[1] == "--commit":
    os.system("bash ~/mytools/up.sh")
    for each_dir in dir_list:
        os.system(
            "cd %s && git add . && git commit -a -m 'up' && git push -u origin master" % each_dir)
