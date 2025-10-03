def on_overlap_tile(sprite, location):
    global Animatronic, Night
    music.play(music.create_song(assets.song("""
            overworld song
        """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    music.set_volume(10)
    tiles.set_current_tilemap(tilemap("""
        Whole map fnaf 1
    """))
    sprites.destroy(Spirit)
    Animatronic = sprites.create(assets.image("""
        freddy 1
    """), SpriteKind.player)
    tiles.place_on_random_tile(Animatronic, assets.tile("""
        myTile16
    """))
    controller.move_sprite(Animatronic)
    scene.camera_follow_sprite(Animatronic)
    Night = 1
    info.set_life(3)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Fnaf 4
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    global Truth_ending_game_1
    music.stop_all_sounds()
    music.play(music.create_song(assets.song("""
            Eisoptrophobia
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    game.show_long_text("--Missing Children-- Kids vanish at local pizzeria- bodies not found. Two local children were reportedly lured into a back room during the late hours of operation at Freddy Fazbear's Pizza on the night of June 26th. While video surveillence identified the man responsible and led to his capture the following morning, the children themselves were never found and are presumed dead. Police think that the suspect dressed as a company mascot to earn their trust.",
        DialogLayout.FULL)
    game.set_dialog_cursor(assets.image("""
        Dialogue Freddy distressed
    """))
    game.show_long_text("...tha- that was... me... i... he... ", DialogLayout.BOTTOM)
    game.set_dialog_cursor(assets.image("""
        Dialogue Freddy dark
    """))
    game.show_long_text("HE KILLED me! My Family doesn't even know I'm Dead! It's HIS fault! HE will pay!",
        DialogLayout.BOTTOM)
    Truth_ending_game_1 += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile72
    """),
    on_overlap_tile2)

def on_up_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy 5
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy 2
        """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile3(sprite3, location3):
    if Truth_ending_game_1 == 1:
        game.set_dialog_cursor(assets.image("""
            Dialogue Freddy dark
        """))
        game.show_long_text("OPEN UP! I'M HERE TO SETTLE THE SCORE!",
            DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    tiles.set_current_tilemap(tilemap("""
        Level Select Menu
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    tiles.place_on_random_tile(Spirit, assets.tile("""
        Crying spirit spawn
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Portal proto
    """),
    on_overlap_tile4)

def on_button_pressed():
    global demo_end
    if demo_end == 1 and controller.right.is_pressed():
        game.show_long_text("Wait, what are you doing?", DialogLayout.FULL)
        demo_end += 1
    if controller.right.is_pressed() and demo_end == 2:
        game.show_long_text("No, Stop!", DialogLayout.FULL)
        demo_end += 1
    if controller.right.is_pressed() and demo_end == 3:
        game.show_long_text("I'm Warning you!", DialogLayout.FULL)
        demo_end += 1
    if controller.right.is_pressed() and demo_end == 4:
        game.show_long_text("WhAt A-a-a-re y-you doing-g-g-g-g?-?-/", DialogLayout.FULL)
        demo_end += 1
    if controller.right.is_pressed() and demo_end == 5:
        game.show_long_text("Th@T5 1t!", DialogLayout.FULL)
        demo_end += 1
    if controller.right.is_pressed() and demo_end == 6:
        tiles.set_current_tilemap(tilemap("""
            level35
        """))
        game.show_long_text("I tried to warn you, It's not done yet; Cheater >=(",
            DialogLayout.FULL)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        tear
    """), Spirit, -70, 0)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        tear
    """), Spirit, 70, 0)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        tear
    """), Spirit, 0, 70)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        tear
    """), Spirit, 0, -70)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy side 2
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy side 3
        """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile5(sprite5, location5):
    global Enemy_prototype
    tiles.place_on_random_tile(Enemy_prototype,
        assets.tile("""
            enemy spawner NOT COKE
        """))
    Enemy_prototype = sprites.create(assets.image("""
            Enemy PQ prototype
        """),
        SpriteKind.enemy)
    Enemy_prototype.follow(Spirit, 30)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile124
    """),
    on_overlap_tile5)

def on_on_overlap(sprite6, otherSprite):
    sprites.destroy(Enemy_prototype)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_overlap_tile6(sprite7, location6):
    game.splash("These are the rules:\"Don't run. Don't yell. Don't scream. Don't poop on floor. Stay close to Mom. Don't touch Freddy. Don't hit. Leave before dark\" ")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile54
    """),
    on_overlap_tile6)

def on_right_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy side 1
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy side 0
        """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile7(sprite8, location7):
    game.set_dialog_cursor(assets.image("""
        Dialogue Freddy distressed
    """))
    game.show_long_text("Dang, Doors locked. If only there was a vent nearby... I should check the party room above me...",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile57
    """),
    on_overlap_tile7)

def on_combos_attach_combo():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            Peppino Spaghetti
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy 1
        """))
controller.combos.attach_combo("up B", on_combos_attach_combo)

def on_down_pressed():
    if Animatronic:
        Animatronic.set_image(assets.image("""
            freddy 3
        """))
        pause(500)
        Animatronic.set_image(assets.image("""
            freddy 0
        """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.show_long_text("You died! (future me (aka entire dev team,) add a cutscene /animation here.) Player, restart!",
        DialogLayout.FULL)
info.on_life_zero(on_life_zero)

def on_overlap_tile8(sprite9, location8):
    global demo_end
    scene.set_background_image(assets.image("""
        myImage4
    """))
    game.set_dialog_text_color(1)
    game.set_dialog_frame(assets.image("""
        text box border
    """))
    game.set_dialog_cursor(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . c c c c . . . . . . 
                . . . . . . c f f c . . . . . . 
                . . . . . . c f f c . . . . . . 
                . . . . . . c f f c . . . . . . 
                . . . . . . c f f c . . . . . . 
                . . . . . . c f f c . . . . . . 
                . e . . c c f f f f c c . . e . 
                e d e . c c c c c c c c . e d e 
                . e . . . . . . . . . . . . e . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    music.stop_all_sounds()
    music.play(music.create_song(assets.song("""
            Music box demo
        """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    music.set_volume(50)
    game.show_long_text("* Hello! Thanks for playing my demo, it's not done yet as you can see, but I hope you enjoyed it! if you did, please share it with others and stay tuned because i'm going to be making fnaf 1,2,3,5, ruin, itp, onaf, fnac, joc, popgoes, DSaF and more! please, leave positive feedback! i'm only 14. ok, bye-bye!(BTW, restart the game, your now stuck in an infinite puppet box music loop)",
        DialogLayout.FULL)
    game.show_long_text("oh, and you cant explore anymore =)", DialogLayout.FULL)
    demo_end += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile68
    """),
    on_overlap_tile8)

def on_overlap_tile9(sprite10, location9):
    game.splash("Huh, It's a poster of me. I look... Good!")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile56
    """),
    on_overlap_tile9)

def on_on_overlap2(sprite11, otherSprite2):
    sprites.destroy(otherSprite2)
    sprites.destroy(sprite11)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

Enemy_prototype: Sprite = None
projectile: Sprite = None
demo_end = 0
Night = 0
Animatronic: Sprite = None
Truth_ending_game_1 = 0
Spirit: Sprite = None
Spirit = sprites.create(assets.image("""
    Spirit
"""), SpriteKind.player)
scene.camera_follow_sprite(Spirit)
controller.move_sprite(Spirit, 100, 100)
tiles.set_current_tilemap(tilemap("""
    tutorial wip
"""))
tiles.place_on_random_tile(Spirit, assets.tile("""
    myTile14
"""))
Truth_ending_game_1 = 0
game.set_dialog_text_color(1)
game.set_dialog_frame(assets.image("""
    text box border
"""))
game.show_long_text("welcome! the controls are simple, wasd= movement, a= attack",
    DialogLayout.BOTTOM)