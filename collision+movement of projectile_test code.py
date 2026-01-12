#Check for collision between bullet and enemy
if isCollision(bullet, enemy):
    play_sound("explosion.wav")#Explosion sound file
    #Reset bullet
    bullet.hideturtle()
    bulletstate = "ready"
    bullet.setposition(0,10000)
    #update player score
    score+=10
    scorestring="Score:{}".format(score)
    score_pen.clear()
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    
    if isCollision(plqyer, enemy):
        play_sound("explosion.wav")
        player.hideturtle()
        enemy.hideturtle()
        print("You died")
        break
    #Game pauses
    
    #Movement of projectile
    if bulletstate == "fire"
    y=bullet.ycor()
    y+=bulletspeed
    bullet.sety(y)