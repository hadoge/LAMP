from maya import cmds

def showUI():

    if cmds.window("mainWindow", exists=True):

        cmds.deleteUI("mainWindow")

    mW = cmds.window("mainWindow", title="LAMP", sizeable=False, widthHeight=(300, 400))
    cmds.flowLayout()
    b1 = cmds.button("Test Setup", command=B1)
    b2 = cmds.button("Sunset", command=B2)
    b3 = cmds.button("Cold", command=B3)
    b4 = cmds.button("Clean", command=B4)
    cmds.showWindow("mainWindow")


def B1(*args):

    # TEST SET UP

    ball = cmds.polySphere(name="Sphere", radius=75, sa=8, sh=8 )
    bG = cmds.polyPlane(name="Plane", width=800, height=600, sh=6, sw=1)
    mC = cmds.camera(name="RenderCam", position=[-53.976, 135.55, 275.601], rotation=[-12, -12, 0])

    cmds.move(0, 100, 0,("Sphere"))
    cmds.move(0, 0, -75, ("Plane"))

    # Select AllDagObjects minus Original Sphere and Plane

    cmds.select(allDagObjects=True)
    cmds.select("RenderCam1", deselect=True)
    cmds.select("Sphere", deselect=True)
    cmds.select("Plane", deselect=True)

    # Plane Modeling

    cmds.move(400, ("Plane.e[18]"), moveY=True)
    cmds.move(-60, ("Plane.e[18]"), moveZ=True)
    cmds.move(265, ("Plane.e[15]"), moveY=True)
    cmds.move(-175, ("Plane.e[15]"), moveZ=True)
    cmds.move(75, ("Plane.e[12]"), moveY=True)

    s = cmds.ls(selection=True)
    if s != []:

        cmds.delete() # DELETE selected objects if LIST is not EMPTY

def B2(*args):

    cmds.ambientLight(name="SunsetLight01", position=[50, 150, 0])
    cmds.ambientLight(name="SunsetLight02", position=[50, 150, 0])

def B3(*args):

    cmds.shadingNode("areaLight", name="ColdLight01", asLight=True)
    cmds.shadingNode("areaLight", name="ColdLight02", asLight=True)

def B4(*args):

    cmds.select(allDagObjects=True)
    s = cmds.ls(selection=True)
    if s != []:

        cmds.delete() # DELETE selected objects if LIST is not EMPTY

showUI()

