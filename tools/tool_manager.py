# coding=utf-8
import os
import sys
from time import sleep

from core import HackingTools
from core import HackingToolsCollection


class UpdateTool(HackingTools):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update HackingTools", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/HackingTools/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/HackingTools/;"
                  "mkdir HackingTools;"
                  "cd HackingTools;"
                  "git clone https://github.com/logesh-works/HackingTools.git;"
                  "cd HackingTools;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(HackingTools):
    TITLE = "Uninstall HackingTools"
    DESCRIPTION = "Uninstall HackingTools"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("HackingTools started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/HackingTools/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/HackingTools/;")
        print("\nHackingTools Successfully Uninstalled... Goodbye.")
        sys.exit()


class ToolManager(HackingToolsCollection):
    TITLE = "Update or Uninstall | HackingTools"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
