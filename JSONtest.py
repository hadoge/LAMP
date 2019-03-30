from maya import cmds
import mtoa.utils
import json
import os

def showUI():

    if cmds.window("JSONTEST", exists=True):

        cmds.deleteUI("JSONTEST")

    cmds.window("JSONTEST", width=200, height=100)
    cmds.columnLayout()
    cmds.button("CREATE JSON FILE", command=B)
    cmds.button("Create Arnold Area Light", command=B2)
    cmds.button("Create Slot", command=renameS)
    cmds.showWindow()

def B(*args):

    createF()

def B2(*args):

    mtoa.utils.createLocator("aiAreaLight", asLight=True)
    cmds.select("aiAreaLight1", r=True)
    cmds.rename("ColdLight01")

class slotRenamer():

    def renameS(*args):

        if cmds.window("JSONTEST", exists=True):

            cmds.deleteUI("JSONTEST")

        cmds.window("Rename Window", width=200, height=100)
        cmds.columnLayout()
        cmds.text("Please rename slot and hit enter")
        name = cmds.textField("setUp01", enterCommand=True)
        cmds.showWindow()

    def createS():

        cmds.button(name, command=)

    def createF():

        lightsData = {}
        lightsData["ColdLight01"] = []
        lightsData["ColdLight02"] = []
        lightsData['ColdLight01'].append({
            'Position.x': -90.4,
            'Position.y': 128.3,
            'Position.z': 150.8
        })

        fPath = os.path.expanduser(r"~/maya")
        with open(fPath + "/goodone.json", "w+") as ofile:
            json.dump(lightsData, ofile)

showUI()