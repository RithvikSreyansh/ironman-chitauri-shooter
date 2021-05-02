def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
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
        """),
        ironman_mark_85,
        500,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.over(True)
info.on_countdown_end(on_countdown_end)

def on_menu_pressed():
    info.set_score(0)
    info.set_life(3)
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_on_overlap(sprite, otherSprite):
    bogey.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
ironman_mark_85: Sprite = None
info.set_score(info.score())
scene.set_background_image(assets.image("""
    space
"""))
ironman_mark_85 = sprites.create(img("""
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
    """),
    SpriteKind.player)
info.set_life(3)
controller.move_sprite(ironman_mark_85, 200, 200)
ironman_mark_85.set_stay_in_screen(True)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(160, randint(5, 115))
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval)
