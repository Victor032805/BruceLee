TITLE = "Let\'s kick!"
WIDTH = 640
HEIGHT = 360

idleAnim = ["idle0", "idle1", "idle2", "idle3"] # image filenames, png omitted
idleDuration = [12, 8, 12, 8] # in frames, i.e., 1/60 sec
idleLoops = True

hkAnim = ["hk0", "hk1", "hk2", "hk3", "hk4", "hk5"]
hkDuration = [4, 4, 10, 4, 4, 4]
hkLoops = False
mkAnim = ["mk0", "mk1", "mk2", "mk3", "mk4", "mk5"]
mkDuration = [4, 4, 10, 4, 4, 4]
mkLoops = False
lkAnim = ["lk0", "lk1", "lk2", "lk3", "lk4"]
lkDuration = [4, 4, 10, 4, 4]
lkLoops = False

# Do not modify this paragraph.
bruce = Actor("idle0")
bruce.x = 320
bruce.y = 270
bruce.isIdle = True # Bruce can only respond to keyboard input when idle.
bruce.anim = idleAnim         # image sequence
bruce.duration = idleDuration # duration sequence
bruce.index = 0
bruce.timer = bruce.duration[bruce.index]
bruce.loops = idleLoops

keyUP = False
keyDOWN = False
keySPACE = False

def animateBruce():
    global bruce
    bruce.timer -= 1
    if bruce.timer <= 0:
        bruce.index += 1
        if bruce.index >= len(bruce.anim) and bruce.loops: # end of animation and then loop
            bruce.index = 0
            bruce.image = bruce.anim[bruce.index]
            bruce.timer = bruce.duration[bruce.index]
        elif bruce.index >= len(bruce.anim) and not bruce.loops: # end of animation and then not loop
            setBruce(idleAnim, idleDuration, idleLoops, True)
        else: # not end of animation, forward to next image
            bruce.image = bruce.anim[bruce.index]
            bruce.timer = bruce.duration[bruce.index]

"Define setBruce() function here. It shall take 4 parameters."

def setBruce(anim, duration, loops, isIdle):
    global bruce
    bruce.anim = anim
    bruce.duration = duration
    bruce.loops = loops
    bruce.isIdle = isIdle
    bruce.index = 0
    bruce.image = bruce.anim[bruce.index]
    bruce.timer = bruce.duration[bruce.index]

def update():
    "Put more code here to respond to keyboard input."
    global keyUP
    global keyDOWN
    global keySPACE
    global bruce
    if keyUP == True and keySPACE == True and bruce.isIdle == True:
        setBruce(hkAnim, hkDuration, hkLoops, False)
    elif keyDOWN == True and keySPACE == True and bruce.isIdle == True:
        setBruce(mkAnim, mkDuration, mkLoops, False)
    elif keySPACE == True and bruce.isIdle == True:
        setBruce(lkAnim, lkDuration, lkLoops, False)
    animateBruce()

def on_key_down(key):
    "Put your code here."
    global keyUP
    global keyDOWN
    global keySPACE
    if key == keys.UP:
        keyUP = True
    elif key == keys.DOWN:
        keyDOWN = True
    elif key == keys.SPACE:
        keySPACE = True


def on_key_up(key):
    "Put your code here."
    global keyUP
    global keyDOWN
    global keySPACE
    if key == keys.UP:
        keyUP = False
    elif key == keys.DOWN:
        keyDOWN = False
    elif key == keys.SPACE:
        keySPACE = False

def draw():
    screen.clear()
    screen.blit("bgd.png", (0,0)) # static non-interactive background
    message = "Press UP+SPACE for high kick.\nPress SPACE for middle kick.\nPress DOWN+SPACE for low kick."
    screen.draw.text(message, topleft=(360,20), fontsize=24, owidth=1.5, ocolor=(0,0,0), color=(255,255,255))
    bruce.draw()
