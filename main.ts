controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . 5 2 2 2 2 2 2 2 2 . . . . . . 
        . . 5 4 4 4 4 4 4 4 2 . . . . . 
        . . . 5 4 4 4 4 4 4 4 2 . . . . 
        . . . . 5 4 4 4 4 4 4 4 2 . . . 
        . . . 5 4 4 4 4 4 4 4 2 . . . . 
        . . 5 4 4 4 4 4 4 4 2 . . . . . 
        . 5 2 2 2 2 2 2 2 2 . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, ironman_mark_85, 500, 0)
})
info.onCountdownEnd(function () {
    game.over(true)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    info.setScore(0)
    info.setLife(3)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    bogey.destroy(effects.fire, 500)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    scene.cameraShake(4, 500)
    info.changeLifeBy(-1)
})
let bogey: Sprite = null
let projectile: Sprite = null
let ironman_mark_85: Sprite = null
info.setScore(info.score())
scene.setBackgroundImage(assets.image`space`)
ironman_mark_85 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . 2 2 2 2 2 2 2 2 . . . . . . 
    . . 2 5 5 5 5 5 5 2 . . . . . . 
    . . 2 2 2 2 2 2 2 2 . . . . 2 . 
    . . f 2 2 2 2 2 2 2 . 2 2 2 5 2 
    . f f 2 5 5 5 5 5 2 2 5 5 9 5 2 
    f f f 2 5 5 5 5 5 2 2 5 5 5 5 2 
    . f f 2 5 5 5 5 5 2 2 5 5 9 5 2 
    . . f 2 2 2 2 2 2 2 . 2 2 2 5 2 
    . . . . 2 2 2 2 2 2 2 2 . . 2 . 
    . . . . 2 5 5 5 5 5 5 2 . . . . 
    . . . . 2 2 2 2 2 2 2 2 . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
info.setLife(3)
controller.moveSprite(ironman_mark_85, 200, 200)
ironman_mark_85.setStayInScreen(true)
game.onUpdateInterval(1000, function () {
    bogey = sprites.create(img`
        ........................
        ........................
        ........................
        ........................
        ..........fffff.........
        ........ff1111bff.......
        .......fb1111111bf......
        .......f111111111f......
        ......fd1111111ffff.....
        ......fd111dd1c111bf....
        ......fb11fcdf1b1bff....
        ......f11111bfbfbff.....
        ......f1b1bdfcffff......
        ......fbfbfcfcccf.......
        ......ffffffffff........
        .........ffffff.........
        .........ffffff.........
        .........fffffff..f.....
        ..........fffffffff.....
        ...........fffffff......
        ........................
        ........................
        ........................
        ........................
        `, SpriteKind.Enemy)
    bogey.setVelocity(-50, 0)
    bogey.setPosition(160, randint(5, 115))
    bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
