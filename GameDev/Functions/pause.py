from ursina import *

class resume(Button):
    def __init__(self):
        super().__init__(
            icon= "Background (6).png",
            text_origin = (.5,.5),
            enabled=False,
            text = "settings",
            text_scale = 4,
            text_color = color.red,
            scale = (.8, .1),
        )
    
        self.is_clicked = False

    def on_click(self):
        print("sperm")
        
class house_box(Entity):
    def __init__(self):
        super().__init__(
            model="GameDev/low_poly_house.obj",
            collision="mesh",
            
            
        )

class house(Entity):
    def init(self):
        super().__init__(
            model="house.obj",
            enabled = True,
            scale=.6,
            rotation=Vec3(0,-50,0),
            position=Vec3(73,0,10),
            ignore=True,
            )
        

class Pause(Entity):
    def __init__(self):
        self.cursor =  Cursor(model=Mesh(vertices=[(-.5,0,0),(.5,0,0),(0,-.5,0),(0,.5,0)], triangles=[(0,1),(2,3)], mode='line', thickness=2), color=color.pink, scale=.08)
        super().__init__(
            parent=camera.ui,
            model = "quad",
            scale = (2, 1),
            opacity = (10),
            enabled=False,
            color = rgb(0,0,0,190),
        )
    
    
