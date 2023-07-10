def on_button_pressed_a():
    global nivel
    nivel = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global nivel
    nivel = 2
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global nivel
    nivel = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global nivel
    nivel = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

roll = 0
pitch = 0
nivel = 0
nivel = 0
input.calibrate_compass()

def on_forever():
    global pitch, roll
    pitch = input.rotation(Rotation.PITCH)
    roll = input.rotation(Rotation.ROLL)
    if abs(roll) < 10 and abs(pitch) < 10:
        if nivel == 0:
            basic.show_leds("""
                . # . # .
                . . . . .
                . . . . .
                # . . . #
                . # # # .
            """)
        elif nivel == 1:
            if input.compass_heading() < 45 or input.compass_heading() > 315:
                basic.show_string("N")
            elif input.compass_heading() > 45 and input.compass_heading() < 135:
                basic.show_string("E")
            elif input.compass_heading() > 135 and input.compass_heading() < 225:
                basic.show_string("S")
            elif input.compass_heading() > 225 and input.compass_heading() < 315:
                basic.show_string("W")
        elif nivel == 2:
            basic.show_number(input.temperature())
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
        """)
basic.forever(on_forever)
