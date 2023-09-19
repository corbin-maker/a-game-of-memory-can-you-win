namespace SpriteKind {
    export const glyph = SpriteKind.create()
    export const UI = SpriteKind.create()
}
function InitUI () {
    mySprite = sprites.create(imageList[0], SpriteKind.UI)
    mySprite.setPosition(60, 90)
    mySprite = sprites.create(imageList[1], SpriteKind.UI)
    mySprite.setPosition(80, 90)
    mySprite = sprites.create(imageList[2], SpriteKind.UI)
    mySprite.setPosition(100, 90)
    mySprite = sprites.create(imageList[3], SpriteKind.UI)
    mySprite.setPosition(60, 108)
    mySprite = sprites.create(imageList[4], SpriteKind.UI)
    mySprite.setPosition(80, 108)
    mySprite = sprites.create(imageList[5], SpriteKind.UI)
    mySprite.setPosition(100, 108)
    CursorSprite = sprites.create(img`
        ....................
        ....................
        ....................
        ....................
        ....................
        ....................
        .........33.........
        ........8888........
        ........8888........
        .........99.........
        .........a9.........
        .........aa.........
        ........aaaa........
        .......aaaaaa.......
        .......aaaaaa.......
        .......aaaaaa.......
        .......aaaaa8.......
        ........8888........
        ....................
        ....................
        `, SpriteKind.UI)
    CursorSprite.setPosition(60, 90)
    curX = 0
    curY = 0
}
function PlaySequence () {
    for (let index2 = 0; index2 <= CodeSequence.length - 1; index2++) {
        CurrentIndex = index2
        AddToSpriteList()
        pause(200)
    }
    pause(600)
    for (let value2 of spriteList) {
        value2.destroy()
    }
    CurrentIndex = 0
    PlayerTurn = true
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    curY = Math.max(0, curY - 1)
    UpdateCurPos()
})
function AddToSequence () {
    CodeSequence.push(randint(0, 5))
}
function InitSounds2 () {
    SoundList = [
    165,
    175,
    196,
    220,
    247,
    262
    ]
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (PlayerTurn == true) {
        CursorAt = curX + curY * 5
        if (CursorAt == CodeSequence[CurrentIndex]) {
            AddToSpriteList()
            info.changeScoreBy(1)
            CurrentIndex += 1
            if (CurrentIndex == CodeSequence.length) {
                NextLevel()
            }
        } else {
            info.changeLifeBy(-1)
            music.spooky.play()
        }
    }
})
function InitImages () {
    imageList = [
    img`
        . f f f . . . . . . . . f f f . 
        f f c . . . . . . . f c b b c . 
        f c c . . . . . . f c b b c . . 
        c f . . . . . . . f b c c c . . 
        c f f . . . . . f f b b c c . . 
        f f f c c . c c f b c b b c . . 
        f f f c c c c c f b c c b c . . 
        . f c 3 c c 3 b c b c c c . . . 
        . c b 3 b c 3 b b c c c c . . . 
        c c b b b b b b b b c c . . . . 
        c b 1 b b b 1 b b b b f c . . . 
        f b b b b b b b b b b f c c . . 
        f b c b b b c b b b b f . . . . 
        . f 1 f f f 1 b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . f f f f f . f f f f f . . 
        . . f f 3 3 3 f f f 3 3 3 f f . 
        . . f 3 3 3 3 3 f 3 3 3 3 3 f . 
        . . f 3 3 3 3 3 3 3 1 1 3 3 f . 
        . . f 3 3 3 3 3 3 3 1 1 3 3 f . 
        . . f 3 3 3 3 3 3 3 3 3 3 3 f . 
        . . f f 3 3 3 b b b 3 3 3 f f . 
        . . . f f 3 b b b b b 3 f f . . 
        . . . . f f b b b b b f f . . . 
        . . . . . f f b b b f f . . . . 
        . . . . . . f f b f f . . . . . 
        . . . . . . . f f f . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . 6 . . . . . . . . 
        . . . . . . 8 6 6 . . . 6 8 . . 
        . . . e e e 8 8 6 6 . 6 7 8 . . 
        . . e 2 2 2 2 e 8 6 6 7 6 . . . 
        . e 2 2 4 4 2 7 7 7 7 7 8 6 . . 
        . e 2 4 4 2 6 7 7 7 6 7 6 8 8 . 
        e 2 4 5 2 2 6 7 7 6 2 7 7 6 . . 
        e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 . 
        e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 . 
        e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 . 
        e 2 4 2 2 2 2 2 2 2 2 2 e c 6 . 
        e 2 2 2 2 2 2 2 4 e 2 e e c . . 
        e e 2 e 2 2 4 2 2 e e e c . . . 
        e e e e 2 e 2 2 e e e c . . . . 
        e e e 2 e e c e c c c . . . . . 
        . c c c c c c c . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . b b b b c . . c b b b c . . 
        . b d 1 1 1 3 c c 3 d 1 1 3 c . 
        b d 1 1 1 1 d d 1 3 1 1 1 1 3 c 
        b 1 1 1 1 1 d 1 1 d d 1 1 1 1 b 
        c 3 1 1 d c c 1 1 c c 1 1 1 1 b 
        c 3 3 d 3 . . c c . . d 1 1 d b 
        b 1 1 1 3 . . . . . . 3 d d 3 c 
        b 1 1 1 d b . . . . c d d 3 3 c 
        c 3 1 1 1 1 c . . b 1 1 1 d b c 
        . c d d 1 1 1 c b 3 1 1 1 1 c . 
        . . c 1 1 1 d d 3 3 1 1 1 b . . 
        . . . b 1 3 d 1 1 d d 3 b . . . 
        . . . . b 3 1 1 1 1 d c . . . . 
        . . . . . c b 1 1 b c . . . . . 
        . . . . . . c b b c . . . . . . 
        `,
    img`
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
        6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
        6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
        6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6 
        6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6 
        6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
        6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
        6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
        6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
        6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
        6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
        6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6 
        6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6 
        6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
        6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . c c . . . . . . 
        . . . . . c a a a a . . . . . . 
        . . . . . a a f f b a . . . . . 
        . . . . c a b f f c b . . . . . 
        . . . . c b b b a f c b . . . . 
        . . . . c b a c a b b b . . . . 
        . . . . . b b f f a a c . . . . 
        . . . . . . a a b b c . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `
    ]
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    curX = Math.max(0, curX - 1)
    UpdateCurPos()
})
function UpdateCurPos () {
    CursorSprite.x = 60 + 20 * curX
    CursorSprite.y = 90 + 18 * curY
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    curX = Math.min(2, curX + 1)
    UpdateCurPos()
})
function InitSequence () {
    for (let index3 = 0; index3 <= 2; index3++) {
        AddToSequence()
    }
}
function NextLevel () {
    PlayerTurn = false
    pause(100)
    for (let value3 of spriteList) {
        value3.destroy()
    }
    AddToSequence()
    PlaySequence()
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    curY = Math.min(1, curX + 1)
    UpdateCurPos()
})
function AddToSpriteList () {
    x = CurrentIndex % 9 * 17
    y = Math.floor(CurrentIndex / 9) * 17
    mySprite = sprites.create(imageList[CodeSequence[CurrentIndex]], SpriteKind.glyph)
    spriteList[CurrentIndex] = mySprite
    mySprite.left = x + 5
    mySprite.top = y + 20
    music.playTone(SoundList[CodeSequence[CurrentIndex]], music.beat(BeatFraction.Whole))
}
sprites.onCreated(SpriteKind.UI, function (sprite) {
    sprite.setFlag(SpriteFlag.Ghost, true)
})
let y = 0
let x = 0
let CursorAt = 0
let SoundList: number[] = []
let PlayerTurn = false
let CurrentIndex = 0
let CodeSequence: number[] = []
let curY = 0
let curX = 0
let CursorSprite: Sprite = null
let imageList: Image[] = []
let mySprite: Sprite = null
let spriteList: Sprite[] = []
let index = 0
let value = 0
game.showLongText("can you memorize the sequence and replay it?", DialogLayout.Bottom)
spriteList = sprites.allOfKind(SpriteKind.Player)
info.setScore(0)
info.setLife(5)
InitImages()
InitSounds2()
InitUI()
InitSequence()
PlaySequence()
