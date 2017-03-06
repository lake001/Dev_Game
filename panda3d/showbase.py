from direct.showbase.ShowBase import ShowBase

class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = myApp()
app.run()
