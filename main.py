@namespace
class SpriteKind:
    glyph = SpriteKind.create()
    UI = SpriteKind.create()
def InitUI():
    global mySprite, CursorSprite, curX, curY
    mySprite = sprites.create(imageList[0], SpriteKind.UI)
    mySprite.set_position(60, 90)
    mySprite = sprites.create(imageList[1], SpriteKind.UI)
    mySprite.set_position(80, 90)
    mySprite = sprites.create(imageList[2], SpriteKind.UI)
    mySprite.set_position(100, 90)
    mySprite = sprites.create(imageList[3], SpriteKind.UI)
    mySprite.set_position(60, 108)
    mySprite = sprites.create(imageList[4], SpriteKind.UI)
    mySprite.set_position(80, 108)
    mySprite = sprites.create(imageList[5], SpriteKind.UI)
    mySprite.set_position(100, 108)
    CursorSprite = sprites.create(img("""
            . . . . . . . . . b 5 b . . . . 
                    . . . . . . . . . b 5 b . . . . 
                    . . . . . . b b b b b b . . . . 
                    . . . . . b b 5 5 5 5 5 b . . . 
                    . . . . b b 5 b c 5 5 d 4 c . . 
                    . b b b b 5 5 5 b f d d 4 4 4 b 
                    . b d 5 b 5 5 b c b 4 4 4 4 b . 
                    . . b 5 5 b 5 5 5 4 4 4 4 b . . 
                    . . b d 5 5 b 5 5 5 5 5 5 b . . 
                    . b d b 5 5 5 d 5 5 5 5 5 5 b . 
                    b d d c d 5 5 b 5 5 5 5 5 5 b . 
                    c d d d c c b 5 5 5 5 5 5 5 b . 
                    c b d d d d d 5 5 5 5 5 5 5 b . 
                    . c d d d d d d 5 5 5 5 5 d b . 
                    . . c b d d d d d 5 5 5 b b . . 
                    . . . c c c c c c c c b b . . .
        """),
        SpriteKind.UI)
    CursorSprite.set_position(60, 90)
    curX = 0
    curY = 0
def PlaySequence():
    global CurrentIndex, PlayerTurn
    index2 = 0
    while index2 <= len(CodeSequence) - 1:
        CurrentIndex = index2
        AddToSpriteList()
        pause(200)
        index2 += 1
    pause(600)
    for value2 in spriteList:
        value2.destroy()
    CurrentIndex = 0
    PlayerTurn = True

def on_up_pressed():
    global curY
    curY = max(0, curY - 1)
    UpdateCurPos()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def AddToSequence():
    CodeSequence.append(randint(0, 5))
def InitSounds2():
    global SoundList
    SoundList = [165, 175, 196, 220, 247, 262]

def on_a_pressed():
    global CursorAt, CurrentIndex
    if PlayerTurn == True:
        CursorAt = curX + curY * 3
        if CursorAt == CodeSequence[CurrentIndex]:
            AddToSpriteList()
            info.change_score_by(1)
            CurrentIndex += 1
            if CurrentIndex == len(CodeSequence):
                NextLevel()
        else:
            info.change_life_by(-1)
            music.power_down.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def InitImages():
    global imageList
    imageList = [img("""
            . . . . . . . . . . b 5 b . . . 
                    . . . . . . . . . b 5 b . . . . 
                    . . . . . . . . . b c . . . . . 
                    . . . . . . b b b b b b . . . . 
                    . . . . . b b 5 5 5 5 5 b . . . 
                    . . . . b b 5 d 1 f 5 5 d f . . 
                    . . . . b 5 5 1 f f 5 d 4 c . . 
                    . . . . b 5 5 d f b d d 4 4 . . 
                    b d d d b b d 5 5 5 4 4 4 4 4 b 
                    b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                    b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                    c d d c d 5 5 b 5 5 5 5 5 5 b . 
                    c b d d c c b 5 5 5 5 5 5 5 b . 
                    . c d d d d d d 5 5 5 5 5 d b . 
                    . . c b d d d d d 5 5 5 b b . . 
                    . . . c c c c c c c c b b . . .
        """),
        img("""
            . . . . c c c b b b b b . . . . 
                    . . c c b 4 4 4 4 4 4 b b b . . 
                    . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                    . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                    e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                    . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                    8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                    8 7 2 e e e e e e e e e e 2 7 8 
                    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                    e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                    e b e 8 8 c c 8 8 c c c 8 e b e 
                    e e b e c c e e e e e c e b e e 
                    . e e b b 4 4 4 4 4 4 4 4 e e . 
                    . . . c c c c c e e e e e . . .
        """),
        img("""
            . . . . . . . e c 7 . . . . . . 
                    . . . . e e e c 7 7 e e . . . . 
                    . . c e e e e c 7 e 2 2 e e . . 
                    . c e e e e e c 6 e e 2 2 2 e . 
                    . c e e e 2 e c c 2 4 5 4 2 e . 
                    c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                    . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                    . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                    . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                    . . . 2 2 e e 4 4 4 2 e e . . . 
                    . . . . . 2 2 e e e e . . . . .
        """),
        img("""
            . . . . . . . . . . b b b . . . 
                    . . . . . . . . b e e 3 3 b . . 
                    . . . . . . b b e 3 2 e 3 a . . 
                    . . . . b b 3 3 e 2 2 e 3 3 a . 
                    . . b b 3 3 3 3 3 e e 3 3 3 a . 
                    b b 3 3 3 3 3 3 3 3 3 3 3 3 3 a 
                    b 3 3 3 d d d d 3 3 3 3 3 d d a 
                    b b b b b b b 3 d d d d d d 3 a 
                    b d 5 5 5 5 d b b b a a a a a a 
                    b 3 d d 5 5 5 5 5 5 5 d d d d a 
                    b 3 3 3 3 3 3 d 5 5 5 d d d d a 
                    b 3 d 5 5 5 3 3 3 3 3 3 b b b a 
                    b b b 3 d 5 5 5 5 5 5 5 d d b a 
                    . . . b b b 3 d 5 5 5 5 d d 3 a 
                    . . . . . . b b b b 3 d d d b a 
                    . . . . . . . . . . b b b a a .
        """),
        img("""
            . . . . . 3 3 b 3 3 d d 3 3 . . 
                    . . . . 3 1 1 d 3 d 1 1 1 1 3 . 
                    . . . 3 d 1 1 1 d 1 1 1 d 3 1 3 
                    . . 3 d d 1 1 1 d d 1 1 1 3 3 3 
                    . 3 1 1 d 1 1 1 1 d d 1 1 b . . 
                    . 3 1 1 1 d 1 1 1 1 1 d 1 1 3 . 
                    . b d 1 1 1 d 1 1 1 1 1 1 1 3 . 
                    . 4 b 1 1 1 1 d d 1 1 1 1 d 3 . 
                    . 4 4 d 1 1 1 1 1 1 d d d b b . 
                    . 4 d b d 1 1 1 1 1 1 1 1 3 . . 
                    4 d d 5 b d 1 1 1 1 1 1 1 3 . . 
                    4 5 d 5 5 b b d 1 1 1 1 d 3 . . 
                    4 5 5 d 5 5 d b b b d d 3 . . . 
                    4 5 5 5 d d d d 4 4 b 3 . . . . 
                    . 4 5 5 5 4 4 4 . . . . . . . . 
                    . . 4 4 4 . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 6 6 6 6 6 6 6 6 . . 
                    . . . . . 6 c 6 6 6 6 6 6 9 6 . 
                    . . . . 6 c c 6 6 6 6 6 6 9 c 6 
                    . . d 6 9 c c 6 9 9 9 9 9 9 c c 
                    . d 6 6 9 c b 8 8 8 8 8 8 8 6 c 
                    . 6 6 6 9 b 8 8 b b b 8 b b 8 6 
                    . 6 6 6 6 6 8 b b b b 8 b b b 8 
                    . 6 6 6 6 8 6 6 6 6 6 8 6 6 6 8 
                    . 6 d d 6 8 f 8 8 8 f 8 8 8 8 8 
                    . d d 6 8 8 8 f 8 8 f 8 8 8 8 8 
                    . 8 8 8 8 8 8 8 f f f 8 8 8 8 8 
                    . 8 8 8 8 f f f 8 8 8 8 f f f f 
                    . . . 8 f f f f f 8 8 f f f f f 
                    . . . . f f f f . . . . f f f . 
                    . . . . . . . . . . . . . . . .
        """)]

def on_left_pressed():
    global curX
    curX = max(0, curX - 1)
    UpdateCurPos()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def UpdateCurPos():
    CursorSprite.x = 60 + 20 * curX
    CursorSprite.y = 90 + 18 * curY

def on_right_pressed():
    global curX
    curX = min(2, curX + 1)
    UpdateCurPos()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def InitSequence():
    for index3 in range(3):
        AddToSequence()
def NextLevel():
    global PlayerTurn
    PlayerTurn = False
    pause(500)
    for value3 in spriteList:
        value3.destroy()
    AddToSequence()
    PlaySequence()

def on_down_pressed():
    global curY
    curY = min(1, curX + 1)
    UpdateCurPos()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def AddToSpriteList():
    global x, y, mySprite
    x = CurrentIndex % 9 * 17
    y = Math.floor(CurrentIndex / 9) * 17
    mySprite = sprites.create(imageList[CodeSequence[CurrentIndex]], SpriteKind.glyph)
    spriteList[CurrentIndex] = mySprite
    mySprite.left = x + 5
    mySprite.top = y + 20
    music.play_tone(SoundList[CodeSequence[CurrentIndex]],
        music.beat(BeatFraction.HALF))

def on_on_created(sprite):
    sprite.set_flag(SpriteFlag.GHOST, True)
sprites.on_created(SpriteKind.UI, on_on_created)

y = 0
x = 0
CursorAt = 0
SoundList: List[number] = []
PlayerTurn = False
CurrentIndex = 0
CodeSequence: List[number] = []
curY = 0
curX = 0
CursorSprite: Sprite = None
imageList: List[Image] = []
mySprite: Sprite = None
spriteList: List[Sprite] = []
index = 0
value = 0
game.show_long_text("Memorize the sequence and replay it", DialogLayout.BOTTOM)
spriteList = sprites.all_of_kind(SpriteKind.glyph)
info.set_score(0)
info.set_life(3)
InitImages()
InitSounds2()
InitUI()
InitSequence()
PlaySequence()