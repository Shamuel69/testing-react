from ursina import *
from ursina.shaders import lit_with_shadows_shader
from Functions.pause import toggle_movement

app = Ursina()

y_val = 8
z_val = 13
# pivot = Entity(model = "CarlBot.obj", position=(70, 15, 40))
pivot = Entity(model="circle", position=(0, y_val, z_val))
DirectionalLight(parent=pivot, y=y_val, z=z_val, shadows=True)

class field(Entity):
    def __init__(self):
        super().__init__(
            model="terrain2.blend", 
            collider="mesh", 
            ignore=True, 
            shader = lit_with_shadows_shader,     
            texture = "White_full.png", 
        )
        
class field2(Entity):
    def __init__(self):
        super().__init__(
            model="dungdon.blend", 
            collider="mesh", 
            ignore=True, 
            shader=lit_with_shadows_shader,
            double_sided=True,
            color = color.white,
            texture = "dongenpaint.png"
        )

class Turtle(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,
            model="CarlBot.obj",
            origin_y = -5,
            texture = "White_full.jpg",
            color = color.blue,
            scale=.55
        )

        self.counter = 0
        self.calor = [color.color(60, 1, 1), color.color(240, 1, 1), color.color(0, 1, 1)]

    def input(self, key):
        if self.hovered: 
            if key == "left mouse down":
                self.counter += 1
                self.counter %= (len(self.calor))
                
                self.color = self.calor[self.counter]
            
            if key == "k":
                self.counter += 1
                self.counter %= (len(self.calor))
                
                Sky(color=self.calor[self.counter])



class Player(Entity):
    def __init__(self, **Kwargs):
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)
        super().__init__()

        self.speed = 15
        self.height = 1.5
        self.camera_pivot = Entity(parent=self, y=self.height)

        camera.parent = self.camera_pivot 
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 110
        mouse.locked = True
        self.mouse_sensitivity = Vec2(70,70)

        self.gravity = 1
        self.grounded = False
        self.jump_height = 2.5
        self.jump_up_duration = .5
        self.fall_after = .25 
        self.jumping = False
        self.air_time = 0
        
        self.crouching = True
        self.crouch_depth = 1
        self.paused = False

        for key, value in Kwargs.items():
            setattr(self, key, value)

        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            if ray.hit:
                self.y = ray.world_point.y
            
    def update(self):
        if self.paused:
            self.direction = Vec3(0,0,0)
            self.rotation_y += 0
            self.camera_pivot.rotation_x += 0

        else: 
            self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()

            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)
        
        feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, ignore=(self,), distance=.5, debug=False)
        head_ray = raycast(self.position+Vec3(0, self.height-.1,0), self.direction, ignore=(self,), distance=.5, debug=False)
                
        if not feet_ray.hit and not head_ray.hit:
            move_amount = self.direction * time.dt * self.speed

            if raycast(self.position+Vec3(-.0,1,0), Vec3(1,0,0), distance=.5, ignore=(self,)).hit:
                move_amount[0] = min(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(-1,0,0), distance=.5, ignore=(self,)).hit:
                move_amount[0] = max(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,1), distance=.5, ignore=(self,)).hit:
                move_amount[2] = min(move_amount[2], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,-1), distance=.5, ignore=(self,)).hit:
                move_amount[2] = max(move_amount[2], 0)
            self.position += move_amount
        
        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            
            if ray.distance <= self.height+.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                
                if ray.world_point.y - self.world_y < 12: 
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity
    
        #work on disabling the jump function while paused
        if held_keys["r"]:
            self.world_position = Vec3(0, 0, 0)

    def input(self, key):
        if key == 'space':
            if not self.paused:
                self.jump()

        if (self.crouching is False) and (key=="shift"):
            self.crouching = True
            print(f"{self.crouching} crouching")
            camera.position = Vec3(0, self.crouch_depth, 0)
        
        elif (self.crouching is True) and (key=="shift"):
            self.crouching = False
            camera.position -= Vec3(0, self.crouch_depth, 0)

        if (self.paused is False) and (key == "escape"):
            self.paused = True
            self.grounded = True
            
        elif (self.paused is True) and (key == "escape"):
            self.paused = False
            self.grounded = False

    

    def jump(self):
        if not self.grounded:
            return 
        
        self.grounded = False
        self.animate_y(self.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)

    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False 

    def land(self):
        # print('land')
        self.grounded = True
        self.air_time = 0


class Pause(Entity):
    def __init__(self, mouse, status):
        super().__init__(
            parent=camera.ui,
            model = "quad",
            scale = (2, 1),
            opacity = (10)
        )

    def update(self, status):
        if status == True:
            self.enabled = True
        
        else: 
            self.enabled = False

    


field()
Sky(color=color.red, texture="skybox.png")
Player()

coordinates = Player().position
coordinate_loc = Text(origin=(5, 18))
coordinate_loc.text = f"{coordinates}"
text = Text(origin=(-5, 18))
Text.default_resolution = 100 * Text.size
text.text = "R-reset button"

app.run()