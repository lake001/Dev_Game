from direct.showbase.ShowBase import ShowBase
from math import sin,cos,pi
from direct.task import Task

class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setPos(-4,8,0)
        self.environ.setScale(0.25,0.25,0.25)

        self.taskMgr.add(self.spinCameraTask, "spinCameraTask")

    def spinCameraTask(self,task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * ( pi / 180.0)

        self.camera.setPos(sin(angleRadians) * 20.0, -cos(angleRadians)*20.0 ,100)
        self.camera.setHpr(angleDegrees,-60,0)
        return Task.cont

myApp().run()
