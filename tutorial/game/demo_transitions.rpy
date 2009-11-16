# This file demonstrates the built-in transitions which are defined in
# common/definitions.rpy, and also the new transitions given above.

init:
    # Define some new transitions here.
    $ slow_dissolve = Dissolve(1.0)    
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    # Imagedissolve Transitions.
    $ circleirisout = ImageDissolve("id_circleiris.png", 1.0, 8)
    $ circleirisin = ImageDissolve("id_circleiris.png", 1.0, 8, reverse=True)
    $ circlewipe = ImageDissolve("id_circlewipe.png", 1.0, 8)
    $ dream = ImageDissolve("id_dream.png", 2.0, 64)
    $ teleport = ImageDissolve("id_teleport.png", 1.0, 0)

    image bg circleiris = "id_circleiris.png"
    image bg teleport = "id_teleport.png"
    

label demo_transitions:

    e "Ren'Py ships with a large number of built-in transitions, and also includes classes that let you define your own."

    menu demo_transitions_menu:
        
        e "What kind of transitions would you like demonstrated?"

        "Simple Transitions":            

            call demo_simple_transitions from _call_demo_simple_transitions_1

        "ImageDissolve Transitions":

            call demo_imagedissolve_transitions from _call_demo_imagedissolve_transitions_1

        "MoveTransition Transitions":

            call demo_movetransition from _call_demo_movetransition_1

        "CropMove Transitions":

            call demo_cropmove_transitions from _call_demo_cropmove_transitions_1
            
            
        ""

        "How about something else?":

            return
        
    jump demo_transitions_menu


label demo_simple_transitions:

    e "Okay, I can tell you about simple transitions. We call them simple because they don't take much in the way of configuration."

    e "But don't let that get you down, since they're the transitions you'll probably use the most in a game."

    show bg whitehouse
    with dissolve

    e "The 'dissolve' transition is probably the most useful, blending one scene into another."

    show bg washington
    with slow_dissolve

    e "The 'Dissolve' function lets you create your own dissolves, taking a different amount of time."
    
    show bg whitehouse
    with fade

    e "The 'fade' transition fades to black, and then fades back in to the new scene."

    e "If you're going to stay at a black screen, you'll probably want to use 'dissolve' rather than 'fade'."

    with flashbulb

    e "You can use 'Fade' to define your own fades. By changing the timing and the color faded to, you can use this for special effects, like flashbulbs."
    
    show bg washington
    with pixellate
    
    e "The 'pixellate' transition pixellates out the old scene, switches to the new scene, and then unpixellates that."

    e "It's probably not appropriate for most games, but we
       think it's kind of neat."

    e "You can use 'Pixellate' to change the details of the pixellation."
    
    e "Motions can also be used as transitions."

    "..."

    "......"

    $ renpy.play('punch.wav')
    with vpunch

    e "Hey! Pay attention."

    e "I was about to demonstrate 'vpunch'... well, I guess I just did."

    $ renpy.play('punch.wav')
    with hpunch

    e "We can also shake the screen horizontally, with 'hpunch'. These were defined using the 'Move' function."

    e "There's also the 'move' transition, which is confusingly enough defined using the 'MoveTransition' function."

    show eileen happy at right
    with move
    show eileen happy at center
    with move

    e "The 'move' transition finds images that have changed placement, and slides them to their new place. It's an easy way to get motion in your game."

    e "Finally, there's 'Pause', which lets you define a transition that just waits for a given amount of time."

    e "Why would you want to do that?"

    e "It's because clicking during a sequence of transitions will skip all of the remaining transitions."

    e "Try clicking during the following transitions:"

    show bg whitehouse
    with dissolve
    with Pause(1)
    show bg washington
    with dissolve

    e "Having 'Pause' makes it easy to implement skippable cut-scenes in terms of transitions."
    
    e "Anyway, that's it for the simple transitions."

    return


label demo_imagedissolve_transitions:

    e "Perhaps the most flexible kind of transition is the ImageDissolve, which lets you use an image to control a dissolve."

    e "This lets us specify very complex transitions, fairly simply. Let's try some, and then I'll show you how they work."

    e "There are two ImageDissolve transitions built into Ren'Py."

    
    scene black
    with blinds
    
    scene bg washington
    show eileen happy
    with blinds
    
    
    e "The 'blinds' transition opens and closes what looks like vertical blinds."

    scene black
    with squares

    scene bg washington
    show eileen happy
    with squares

    e "The 'squares' transition uses these squares to show things."

    e "I'm not sure why anyone would want to use it, but it was used in some translated games, so we added it."

    e "The most interesting transitions aren't in the standard library."

    e "These ones require an image the size of the screen, and so we couldn't include them as the size of the screen can change from game to game."

    e "You can click the button above to see how they are defined in the demo script."

    scene black
    with circleirisin

    e "We can hide things with a 'circleirisin'..."

    scene bg washington
    with circleirisout

    e "... and show them again with a 'circleirisout'."

    show bg whitehouse
    with circlewipe

    e "The 'circlewipe' transitions changes screens using a circular wipe effect."

    scene bg washington
    with dream

    e "The 'dream' transition does this weird wavy dissolve, and does it relatively slowly."

    show eileen happy
    with teleport

    e "The 'teleport' transition reveals the new scene one line at a time."

    scene bg circleiris
    with dissolve

    e "This is the background picture used with the circleirisout transition."

    e "When we use an ImageDissolve, the white will dissolve in first, followed by progressively darker colors. Let's try it."

    show bg washington
    with circleirisout

    e "If we give ImageDissolve the 'reverse' parameter, black areas will dissolve in first."

    show bg circleiris
    with circleirisin

    e "This lets circleirisin and circleirisout use the same image."

    show bg teleport
    with dissolve

    e "The teleport transition uses a different image, one that dissolves things in one line at a time."

    show bg washington
    with teleport

    e "A dissolve only seems to affect parts of the scene that have changed..."

    show eileen happy
    with teleport

    e "... which is how we apply the teleport effect to a single character."
    
    e "For more examples of ImageDissolve, check out the {i}Utsukushii Effects{/i} demo."

    e "It shows how a clever game-maker can use ImageDissolve to create all sorts of effects."

    return
    
label demo_cropmove_transitions:

    e "The CropMove transition class provides a wide range of transition effects. It's not used very much in practice, though."

    show eileen happy at offscreenleft
    with move

    e "I'll stand offscreen, so you can see some of its modes. I'll read out the mode name after each transition."

    scene bg whitehouse
    with wiperight

    e "We first have wiperight..."

    scene bg washington
    with wipeleft

    e "...followed by wipeleft... "    

    scene bg whitehouse
    with wipeup

    e "...wipeup..."

    scene bg washington
    with wipedown

    e "...and wipedown."

    e "Next, the slides."

    scene bg whitehouse
    with slideright

    e "Slideright..."

    scene bg washington
    with slideleft

    e "...slideleft..."

    scene bg whitehouse
    with slideup

    e "...slideup..."

    scene bg washington
    with slidedown

    e "and slidedown."

    e "While the slide transitions slide in the new scene, the
       slideaways slide out the old scene."

    scene bg whitehouse
    with slideawayright

    e "Slideawayright..."

    scene bg washington
    with slideawayleft

    e "...slideawayleft..."

    scene bg whitehouse
    with slideawayup

    e "...slideawayup..."

    scene bg washington
    with slideawaydown

    e "and slideawaydown."

    e "We also have a couple of transitions that use a
       rectangular iris."

    scene bg whitehouse
    with irisout

    e "There's irisout..."

    scene bg washington
    show eileen happy
    with irisin

    e "... and irisin."

    e "It's enough to make you feel a bit dizzy."

    return

label demo_movetransition:

    e "The most common MoveTransition is move, which slides around images that have changed position on the screen."

    show eileen happy at left
    with move

    e "Just like that."

    e "There are also the moveout and movein transitions."

    e "The moveout transitions (moveoutleft, moveoutright, moveouttop, and moveoutbottom) slide hidden images off the appropriate side of the screen."

    e "The movein transitions (moveinleft, moveinright, moveintop, and moveinbottom) slide in new images."

    e "Let's see them all in action."

    hide eileen happy
    with moveoutleft

    show eileen happy
    with moveinbottom

    hide eileen happy
    with moveoutbottom

    show eileen happy
    with moveinright

    hide eileen happy
    with moveoutright

    show eileen flip
    with moveintop

    hide eileen flip
    with moveouttop

    show eileen happy
    with moveinleft

    e "That's it for the moveins and moveouts."

    e "Finally, there are the zoomin and zoomout transtions, which show and hide things using a zoom."

    hide eileen happy
    with zoomout

    show eileen happy
    with zoomin

    e "And that's all there is."
    
    return