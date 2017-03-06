from direct.showbase.ShowBase import ShowBase
class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setPos(-8,42,0)
        self.environ.setScale(0.2,0.2,0.2)

myApp().run()
