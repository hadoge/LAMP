from maya import cmds
import mtoa.utils

def showUI():

    if cmds.window("mainWindow", exists=True):

        cmds.deleteUI("mainWindow")

    mW = cmds.window("mainWindow", title="LAMP", sizeable=False, widthHeight=(300, 400), bgc=(0.6, 0.5, 0.3))
    mainCL = cmds.columnLayout(adj=True)

    logoP = cmds.internalVar(usd=True) + "/lamp_sources/banner/logolamp_03.jpg"
    cmds.image(width=300, height=110, image=logoP)

    cmds.text("IMPORT")

    mainRL = cmds.rowLayout(numberOfColumns=2)
    cmds.button("Mercury", bgc=(0.3, 0.3, 0.3), command=B5)
    cmds.textField(bgc=(0.6, 0.5, 0.3))
    cmds.setParent(mainCL)
    cmds.columnLayout(columnOffset=('left', 10))
    cmds.text("ENVIRONMENT")


    cmds.rowLayout(numberOfColumns=3)
    b1 = cmds.button("Test Setup",bgc=(0.3, 0.3, 0.3), command=B1)
    b1point2 = cmds.button("User Environment")
    b1point3 = cmds.button("Simply")
    cmds.setParent(mainCL)

    cmds.columnLayout()
    cmds.text("Arnold   LIGHTS")

    cmds.rowLayout(numberOfColumns=2)
    b2 = cmds.button("Sunset", bgc=(0.3, 0.3, 0.3), command=B2)
    b2point1 = cmds.button("Cold", bgc=(0.3, 0.3, 0.3), command=B3)
    cmds.setParent(mainCL)

    cmds.columnLayout()
    cmds.text("Arnold MATERIALS")

    cmds.rowLayout(numberOfColumns=2)
    b3point1 = cmds.button("Wood")
    b3point2 = cmds.button("Wax")
    cmds.setParent(mainCL)

    cmds.separator(height=10,style="in")
    cmds.columnLayout()
    b4 = cmds.button("Clean", bgc=(0.3, 0.3, 0.3), command=B4)

    cmds.showWindow("mainWindow")


def B1(*args):

    # TEST SET UP

    ball = cmds.polySphere(name="Sphere", radius=75, sa=8, sh=8 )
    bG = cmds.polyPlane(name="Plane", width=800, height=600, sh=6, sw=1)
    mC = cmds.camera(name="RenderCam", position=[-55.950, 137.560, 284.860], rotation=[-12, -12, 0])

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
    cmds.displaySmoothness(bG,polygonObject=3)

    s = cmds.ls(selection=True)
    if s != []:

        cmds.delete() # DELETE selected objects if LIST is not EMPTY

def B2(*args):

    cmds.ambientLight(name="SunsetLight01", position=[50, 150, 0])
    cmds.ambientLight(name="SunsetLight02", position=[50, 150, 0])

def B3(*args):

    # cmds.shadingNode("areaLight", name="ColdLight01", asLight=True)
    # cmds.shadingNode("areaLight", name="ColdLight02", asLight=True)
    mtoa.utils.createLocator("aiAreaLight", asLight=True)

def B4(*args):

    cmds.select(allDagObjects=True)
    s = cmds.ls(selection=True)
    if s != []:

        cmds.delete() # DELETE selected objects if LIST is not EMPTY
def B5(*args):

    mercuryPath = cmds.internalVar(usd=True) + "/lamp_sources/models/mercury.obj"
    cmds.file(mercuryPath, i=True)

showUI()
