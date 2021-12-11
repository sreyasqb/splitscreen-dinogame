import math
from pygame import*
init()
root=display.set_mode((1200,800))
run=True
test=image.load('socgame/c1r.jpeg')
bg1=image.load('icegame/new1.jpeg')
bg2=image.load('icegame/new2.jpeg')
dinoimage=[image.load('icegame/dr1.png'),image.load('icegame/dr2.png'),image.load('icegame/dr3.png'),image.load('icegame/dr4.png'),image.load('icegame/dr5.png'),image.load('icegame/dr6.png'),image.load('icegame/dr7.png'),image.load('icegame/dr8.png')]
standingimage=[image.load('icegame/Idle (1).png'),image.load('icegame/Idle (2).png'),image.load('icegame/Idle (3).png'),image.load('icegame/Idle (4).png'),image.load('icegame/Idle (5).png'),image.load('icegame/Idle (6).png'),image.load('icegame/Idle (7).png'),image.load('icegame/Idle (8).png'),image.load('icegame/Idle (9).png'),image.load('icegame/Idle (10).png')]
jumpingmovingimage=[image.load('icegame/Jump (4).png'),image.load('icegame/Jump (5).png'),image.load('icegame/Jump (6).png'),image.load('icegame/Jump (7).png'),image.load('icegame/Jump (8).png'),image.load('icegame/Jump (9).png'),image.load('icegame/Jump (10).png'),image.load('icegame/Jump (11).png'),image.load('icegame/Jump (12).png')]
dinodead=image.load('icegame/Dead (8).png')
pumprunimage=[image.load('icegame/Run (1).png'),image.load('icegame/Run (2).png'),image.load('icegame/Run (3).png'),image.load('icegame/Run (4).png'),image.load('icegame/Run (5).png'),image.load('icegame/Run (6).png'),image.load('icegame/Run (7).png'),image.load('icegame/Run (8).png')]
pumpstandingimage=[image.load('icegame/Idle (1)1.png'),image.load('icegame/Idle (2)1.png'),image.load('icegame/Idle (3)1.png'),image.load('icegame/Idle (4)1.png'),image.load('icegame/Idle (5)1.png'),image.load('icegame/Idle (6)1.png'),image.load('icegame/Idle (7)1.png'),image.load('icegame/Idle (8)1.png'),image.load('icegame/Idle (9)1.png'),image.load('icegame/Idle (10)1.png')]
pumpjumpingimage=[image.load('icegame/Jump (3)1.png'),image.load('icegame/Jump (4)1.png'),image.load('icegame/Jump (5)1.png'),image.load('icegame/Jump (7)1.png'),image.load('icegame/Jump (8)1.png'),image.load('icegame/Jump (9)1.png')]
pumpdead=image.load('icegame/Dead (10).png')
gamewinner='none'
maxpowerup=0
gameover=False
flashdino=False
flashpump=False
c1=0
c2=0
fdc=0
fpc=0
class characters:
    def __init__(self,x,y,vel,walkcount,moving,standing,standcount,isjump,jumpcount,jumpvel,jumpmoving,jumpability,no,fps,stuck,landed,fall,deathcount,level,invel,fivel,disp):
        self.x=x
        self.y=y
        self.vel=vel
        self.walkcount=walkcount
        self.moving=moving
        self.standing=standing
        self.standcount=standcount
        self.jumpcount=jumpcount
        self.isjump=isjump
        self.jumpvel=jumpvel
        self.jumpmoving=jumpmoving
        self.jumpability=jumpability
        self.no=no
        self.fps=fps
        self.stuck=stuck
        self.landed=landed
        self.fall=fall
        self.deathcount=deathcount
        self.level=level
        self.invel=invel
        self.fivel=fivel
        self.disp=disp
#CHARACTERS
dino=characters(x=190,y=240,vel=10,walkcount=0,moving=False,standing=True,standcount=0,isjump=False,jumpcount=10,jumpvel=7,jumpmoving=False,jumpability=True,no=False,fps=0,stuck=False,landed=False,fall=False,deathcount=0,level=240,invel=0,fivel=20,disp=0)
dinomir=characters(x=190,y=640,vel=10,walkcount=0,moving=False,standing=True,standcount=0,isjump=False,jumpcount=10,jumpvel=7,jumpmoving=False,jumpability=True,no=False,fps=0,stuck=False,landed=False,fall=False,deathcount=0,level=640,invel=0,fivel=20,disp=0)
pump=characters(x=200,y=640,vel=10,walkcount=0,moving=False,standing=True,standcount=0,isjump=False,jumpcount=10,jumpvel=7,jumpmoving=False,jumpability=True,no=False,fps=0,stuck=False,landed=False,fall=False,deathcount=0,level=640,invel=0,fivel=20,disp=0)
pumpmir=characters(x=200,y=240,vel=10,walkcount=0,moving=False,standing=True,standcount=0,isjump=False,jumpcount=10,jumpvel=7,jumpmoving=False,jumpability=True,no=False,fps=0,stuck=False,landed=False,fall=False,deathcount=0,level=240,invel=0,fivel=20,disp=0)
class screen:
    def __init__(self,vel,bgx,lap):
        self.vel=vel
        self.bgx=bgx
        self.lap=lap




up=screen(vel=10,bgx=0,lap=0)
low=screen(vel=10,bgx=0,lap=0)




font = font.SysFont('Times New Roman', 40)
while run:
    updist=font.render(('DINO DISTANCE->'+str(abs(up.bgx))),True,((24,91,6)))
    lowdist=font.render('PUMP DISTANCE->'+str((abs(low.bgx))),True,((24,91,6)))

    if abs(up.bgx)>abs(low.bgx) and not gameover:
        gamewinner='DINO'
        text = font.render('#1-----> DINO', True, (214, 8, 67))
    elif abs(low.bgx)>abs(up.bgx) and not gameover:
        gamewinner='PUMPKIN'
        text = font.render('#1-----> PUMPKIN', True, (10, 85, 206))
    else:
        text = font.render('TIE', True, (0, 0, 0))
        gamewinner='none'

    if up.lap>=3 or low.lap>=3:
        wintext = font.render('CONGRATS'+str(' ')+str(gamewinner), True, (117, 21, 81))
        gameover=True
        root.blit(wintext,(600,400))
        display.update()


    if dino.standcount > 27:
        dino.standcount = 0
    if dino.fps > 22:
        dino.fps = 0
    for events in event.get():
        if events.type==QUIT:
            run=False
    def upper():
        if not flashdino:
            root.blit(bg1,(up.bgx,0))
            if up.bgx<-6850:
                up.bgx=0
                up.lap+=1
            root.blit(text, (800,40))
            root.blit(updist,(800,80))
            display.update()
            dinonormal()
            pumpmirror()

    def lower():
        if not flashpump:
            root.blit(bg2,(low.bgx,400))
            if low.bgx<-6850:
                low.bgx=0
                low.lap+=1
            root.blit(text, (800, 440))
            root.blit(lowdist,(800,480))
            dinomirror()
            display.update()
            pumpnormal()



    def dinonormal():
        if not dino.fall :
            if dino.standing:
                root.blit(standingimage[dino.standcount//3],(dino.x,dino.y))
            if dino.moving and not dino.isjump:
                root.blit(dinoimage[dino.walkcount//3], (dino.x,dino.y))
            if dino.walkcount>=22:
                dino.walkcount=0
            if dino.standcount>28:
                dino.standcount=0
            if dino.moving and dino.isjump:
                root.blit(jumpingmovingimage[dino.fps//3],(dino.x,dino.y))
            if dino.fps>22:
                dino.fps=0
        else:
            if dino.deathcount<20:
                root.blit(dinodead,(dino.x,dino.y))
        display.update()
    def dinomirror():
        if not flashdino:
            if not dinomir.fall:
                if dinomir.standing:
                    root.blit(standingimage[dinomir.standcount//3],(dinomir.x,dinomir.y))
                if dinomir.moving and not dinomir.isjump:
                    root.blit(dinoimage[dinomir.walkcount//3], (dinomir.x,dinomir.y))
                if dinomir.walkcount>22:
                    dinomir.walkcount=0
                if dinomir.standcount>27:
                    dinomir.standcount=0
                if dinomir.moving and dinomir.isjump:
                    root.blit(jumpingmovingimage[dinomir.fps//3],(dinomir.x,dinomir.y))
                if dinomir.fps>22:
                    dinomir.fps=0
            else:
                if dinomir.deathcount<20:
                    root.blit(dinodead,(dinomir.x,dinomir.y))
        display.update()
    keys=key.get_pressed()


    def pumpnormal():
        if not pump.fall:
            if pump.standing:
                root.blit(pumpstandingimage[pump.standcount//3],(pump.x,pump.y))
            if pump.moving and not pump.isjump:
                root.blit(pumprunimage[pump.walkcount//3], (pump.x,pump.y))
            if pump.walkcount>22:
                pump.walkcount=0
            if pump.standcount>28:
                pump.standcount=0
            if pump.moving and pump.isjump:
                root.blit(pumpjumpingimage[pump.fps//3],(pump.x,pump.y))
            if pump.fps>22:
                pump.fps=0
        else:
            if pump.deathcount<20:
                root.blit(pumpdead,(pump.x,pump.y))
        display.update()


    def pumpmirror():
        if not flashpump:
            if not pumpmir.fall:
                if pumpmir.standing:
                    root.blit(pumpstandingimage[pumpmir.standcount//3],(pumpmir.x,pumpmir.y))
                if pumpmir.moving and not pumpmir.isjump:
                    root.blit(pumprunimage[pumpmir.walkcount//3], (pumpmir.x,pumpmir.y))
                if pumpmir.walkcount>22:
                    pumpmir.walkcount=0
                if pumpmir.standcount>28:
                    pumpmir.standcount=0
                if pumpmir.moving and pumpmir.isjump:
                    root.blit(pumpjumpingimage[pumpmir.fps//3],(pumpmir.x,pumpmir.y))
                if pumpmir.fps>22:
                    pumpmir.fps=0
            else:
                if pumpmir.deathcount<20:
                    root.blit(pumpdead,(pumpmir.x,pumpmir.y))
        display.update()


    def controls1():
        if keys[K_d] and not dino.stuck and not dino.fall and not dinomir.stuck:
            up.bgx -= up.vel
            if dino.walkcount<22:
                dino.walkcount+=1
            dino.moving=True
            dino.standing=False
            #for dinomirror
            if dinomir.walkcount<22:
                dinomir.walkcount += 1
            dinomir.moving = True
            dinomir.standing = False
            dino.jumpmoving=True
        else:
            dino.standing = True
            dino.moving = False
            dino.standcount += 1
            # for dino mirror
            dinomir.standing = True
            dinomir.moving = False
            if dinomir.standcount<27:
                dinomir.standcount += 1
            else:
                dinomir.standcount=0
        #dino normal jump
        if keys[K_w] and dino.jumpability and not dino.fall:
            dino.isjump=True
        if dino.isjump:
            if dino.y<=dino.level :
                dino.disp=-((dino.fivel)**2-(dino.invel)**2)/20
                dino.y+=dino.disp
                dino.invel+=1
                dino.fivel-=1
                dino.fps+=1
            elif dino.y>dino.level:
                dino.y = dino.level
                dino.isjump=False
                dino.jumpcount=10
                dino.jumpability=True
                dino.fivel=20
                dino.invel=0
                dino.disp=0
        #dino mirror jump
        if keys[K_w] and dinomir.jumpability and not dinomir.fall:
            dinomir.isjump=True
        if dinomir.isjump:
            if dinomir.y<=dinomir.level :
                dinomir.disp=-((dinomir.fivel)**2-(dinomir.invel)**2)/20
                dinomir.y+=dinomir.disp
                dinomir.invel+=1
                dinomir.fivel-=1
                dinomir.fps+=1
            elif dinomir.y>dinomir.level:
                dinomir.y = dinomir.level
                dinomir.isjump=False
                dinomir.jumpcount=10
                dinomir.jumpability=True
                dinomir.fivel=20
                dinomir.invel=0
        if dino.standcount>27:
            dino.standcount=0
        if dino.fps>22:
            dino.fps=0
        if dinomir.standcount>25:
            dino.standcount=0
        if dinomir.fps>22:
            dinomir.fps=0



    def relativescreen():
        #dino Mirror moving
        if dino.moving and not keys[K_RIGHT] and  dinomir.vel != 0 :
            dinomir.x += dino.vel
        if dino.standing and keys[K_RIGHT] :
            dinomir.x -= dino.vel
        #pumpkin mirror
        if pump.moving and not keys[K_d]  :
            pumpmir.x += pump.vel
        if pump.standing and keys[K_d] :
            pumpmir.x -= pump.vel
        if dino.stuck and keys[K_d]:
            pumpmir.x+=pump.vel

        if pump.stuck and keys[K_RIGHT]:
            dinomir.x+=dino.vel
        if dino.fall and keys[K_d]:
            pumpmir.x+=pump.vel
    relativescreen()




    def controls2():

        if keys[K_RIGHT] and not pump.stuck and not pump.fall :
            low.bgx -= low.vel
            pump.walkcount+=1
            pump.moving=True
            pump.standing=False
            #for pumpmirror
            if pumpmir.walkcount<22:
                pumpmir.walkcount += 1
            pumpmir.moving = True
            pumpmir.standing = False
            pump.jumpmoving=True
        else:
            pump.standing = True
            pump.moving = False
            pump.standcount += 1
            # for pump mirror
            pumpmir.standing = True
            pumpmir.moving = False
            if pumpmir.standcount<27:
                pumpmir.standcount += 1
            else:
                pumpmir.standcount=0
        #pump normal jump
        if keys[K_UP] and pump.jumpability and not pump.fall:
            pump.isjump=True
        if pump.isjump:
            if pump.y<=pump.level :
                pump.disp=-((pump.fivel)**2-(pump.invel)**2)/20
                pump.y+=pump.disp
                pump.invel+=1
                pump.fivel-=1
                if pump.fps<16:
                    pump.fps+=1
                else:
                    pump.fps=0
            elif pump.y>pump.level:
                pump.y = pump.level
                pump.isjump=False
                pump.jumpcount=10
                pump.jumpability=True
                pump.fivel=20
                pump.invel=0
                pump.disp=0
        #pump mirror jump
        if keys[K_UP] and pumpmir.jumpability and not pumpmir.fall:
            pumpmir.isjump=True
        if pumpmir.isjump:
            if pumpmir.y<=pumpmir.level :
                pumpmir.disp=-((pumpmir.fivel)**2-(pumpmir.invel)**2)/20
                pumpmir.y+=pumpmir.disp
                pumpmir.invel+=1
                pumpmir.fivel-=1
                if pumpmir.fps<16:
                    pumpmir.fps+=1
                else:
                    pump.fps=0
            elif pumpmir.y>pumpmir.level:
                pumpmir.y = pumpmir.level
                pumpmir.isjump=False
                pumpmir.jumpcount=10
                pumpmir.jumpability=True
                pumpmir.fivel=20
                pumpmir.invel=0
        if pump.standcount>27:
            pump.standcount=0
        if pump.fps>22:
            pump.fps=0
        if pumpmir.standcount>25:
            pump.standcount=0
        if pumpmir.fps>22:
            pumpmir.fps=0




    def dinocollisons():
        #starting
        if 0<=abs(up.bgx)<770:
            dino.level=240
            if dino.y==180 and dino.y!=dino.level:
                dino.y=240
        #firstjump and first stuck
        if 770<abs(up.bgx)<1330:
            dino.level=180
        if 760<abs(up.bgx)<780:
            dino.stuck=True
        if dino.stuck and dino.y<240:
            dino.stuck=False
        #first fall
        if 1355<abs(up.bgx)<1430 and dino.y>179:
            dino.fall=True
        if dino.fall:
            dino.deathcount+=1
            dino.y=400-116
        if dino.deathcount>20 and dino.fall:
            dino.fall=False
            dino.y=180
            up.bgx-=75
            pumpmir.x-=75
            dino.deathcount=0
        #2nd bridge
        if 1430<=abs(up.bgx)<2130:
            dino.level=180
        #second fall
        if 2131<abs(up.bgx)<2210 and dino.y>179 :
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 230
                up.bgx -= 80
                pumpmir.x-=80
                dino.deathcount=0
        #3rd bridge
        if 2210<abs(up.bgx)<2495:
            dino.level=230
        #3rdbridgebox
        if 2500<abs(up.bgx)<2590:
            dino.level=180
        if 2490<abs(up.bgx)<2520:
            dino.stuck=True
        if dino.stuck and dino.y<230:
            dino.stuck=False
        #3rdbridge continue
        if 2590<=abs(up.bgx)<2975:
            dino.level=230
            if dino.y==180 and dino.y!=dino.level:
                dino.y=dino.level
        #3rdbridge fall
        if 2990<abs(up.bgx)<3030 and dino.y>229:
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 170
                up.bgx -= 40
                pumpmir.x-=40
                dino.deathcount=0
        #4thbridge
        if 3030<=abs(up.bgx)<3295:
            dino.level=170
        #4thbridge fall
        if 3295<=abs(up.bgx)<3370 and dino.y>169:
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 230
                up.bgx -= 75
                pumpmir.x-=75
                dino.deathcount=0
        #4thbridgelowerleftcrate
        if 3370<=abs(up.bgx)<4080:
            dino.level=230
            if dino.y == 180 and dino.y != dino.level:
                dino.y=230
        #4thbridgeendcrate
        if 4950<abs(up.bgx)<5030:
            dino.level=160
        if 4940<abs(up.bgx)<4955:
            dino.stuck=True
        if dino.stuck and dino.y<230:
            dino.stuck=False
        #4thbridgefall
        if 5060<abs(up.bgx)<5100 and dino.y>159:
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 130
                up.bgx -= 45
                pumpmir.x -=45
                dino.deathcount=0
        #5thbridge
        if 5100<=abs(up.bgx)<5240:
            dino.level=130
        #6thbridge
        if 5245<abs(up.bgx)<5945:
            dino.level=230
            if dino.y == 130 and dino.y != dino.level:
                dino.y = 230
        #7thbridge
        if 5960<abs(up.bgx)<6230:
            dino.level=180
        if 5950<abs(up.bgx)<5960:
            dino.stuck=True
        if dino.stuck and dino.y<230:
            dino.stuck=False
        #7thbridgefall
        if 6245<abs(up.bgx)<6325 and dino.y>179:
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 180
                up.bgx -= 80
                pumpmir.x -=80
                dino.deathcount=0
        #8thbridge
        if 6325<abs(up.bgx)<6445:
            dino.level=180
        #8thbridgefall
        if 6460<abs(up.bgx)<6530 and dino.y>179:
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 230
                up.bgx -= 70
                pumpmir.x -=70
                dino.deathcount=0
        #9th bridge
        if 6530<=abs(up.bgx)<6780:
            dino.level=230
        #9thbridgefall
        if 6800<abs(up.bgx)<6850 and dino.y>229:
            dino.fall=True
            if dino.fall:
                dino.deathcount += 1
                dino.y = 400 - 116
            if dino.deathcount > 20 and dino.fall:
                dino.fall = False
                dino.y = 180
                up.bgx -= 70
                pumpmir.x -=70
                dino.deathcount=0
        if 6850<=abs(up.bgx)<7165:
            dino.level=180



    def dinomircollisons():
        # starting
        if 0 <= abs(up.bgx) < 770:
            dinomir.level = 240 + 400
            if pumpmir.y == 180 + 400 and dinomir.y != dinomir.level:
                dinomir.y = 240 + 400
        # firstjump and first stuck
        if 770 < abs( up.bgx) < 1330:
            dinomir.level = 180 + 400
        if 760 < abs(up.bgx):
            dinomir.stuck = True
        if dinomir.stuck and dinomir.y < 240 + 400:
            dinomir.stuck = False
        # first fall
        if 1355 < abs(up.bgx) < 1430 and dinomir.y > 179 + 400:
            dinomir.fall = True
        if dinomir.fall:
            dinomir.deathcount += 1
            dinomir.y = 400 - 116 + 400
        if dinomir.deathcount > 20 and dinomir.fall:
            dinomir.fall = False
            dinomir.y = 180 + 400
            dinomir.x += 75
            dinomir.deathcount = 0
        # 2nd bridge
        if 1430 <= abs(up.bgx) < 2130:
            dinomir.level = 180 + 400
        # second fall
        if 2131 < abs(up.bgx) < 2200 and dinomir.y > 179 + 400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116 + 400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 230 + 400
                dinomir.x+= 80
                dinomir.deathcount = 0
        # 3rd bridge
        if 2190 <= abs(up.bgx) < 2495:
            dinomir.level = 230 + 400
            if dinomir.y==580 and dinomir.y!=dino.level:
                dinomir.y=630
        # 3rdbridgebox
        if 2500 < abs(up.bgx) < 2590:
            dinomir.level = 180+400
        if 2490 < abs(up.bgx) < 2520:
            dinomir.stuck = True
        if dinomir.stuck and dinomir.y < 230 + 400:
            dinomir.stuck = False
        # 3rdbridge continue
        if 2590 <= abs(up.bgx) < 2975:
            dinomir.level = 230 + 400
            if dinomir.y == 180 + 400 and dinomir.y != dinomir.level:
                dinomir.y = dinomir.level
        # 3rdbridge fall
        if 2990 < abs(up.bgx) < 3030 and dinomir.y > 229 + 400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116+400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 170+400
                dinomir.x+= 40
                dinomir.deathcount = 0
        # 4thbridge
        if 3030 <= abs(up.bgx) < 3295:
            dinomir.level = 170+400
        # 4thbridge fall
        if 3295 <= abs(up.bgx) < 3370 and dinomir.y > 169+400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116+400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 230+400
                dinomir.x+= 75
                dinomir.deathcount = 0
        # 4thbridgelowerleftcrate
        if 3360 <= abs(up.bgx) < 4090:
            dinomir.level = 230+400
            if dinomir.y == 180+400 and dinomir.y != dinomir.level:
                dinomir.y = 230+400
        # 4thbridgeendcrate
        if 4950 < abs(up.bgx) < 5030:
            dinomir.level = 160+400
        if 4940 < abs(up.bgx) < 4955:
            dinomir.stuck = True
        if dinomir.stuck and dinomir.y < 230+400:
            dinomir.stuck = False
        # 4thbridgefall
        if 5060 < abs(up.bgx) < 5100 and dinomir.y > 159+400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116+400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 130+400
                dinomir.x+=45
                dinomir.deathcount = 0
        # 5thbridge
        if 5100 <= abs(up.bgx) < 5240:
            dinomir.level = 130+400
        # 6thbridge
        if 5245 < abs(up.bgx) < 5945:
            dinomir.level = 230+400
            if dinomir.y == 130+400 and dinomir.y != dinomir.level:
                dinomir.y = 230+400
        # 7thbridge
        if 5960 < abs(up.bgx) < 6230:
            dinomir.level = 180+400
        if 5950 < abs(up.bgx) < 5960:
            dinomir.stuck = True
        if dinomir.stuck and dinomir.y < 230+400:
            dinomir.stuck = False
        # 7thbridgefall
        if 6245 < abs(up.bgx) < 6325 and dinomir.y > 179+400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116+400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 180+400
                dinomir.x+= 80
                dinomir.deathcount = 0
        # 8thbridge
        if 6320 <=abs(up.bgx) < 6445:
            dinomir.level = 180+400
        # 8thbridgefall
        if 6460 < abs(up.bgx) < 6530 and dinomir.y > 179+400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116+400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 230+400
                dinomir.x+= 80
                dinomir.deathcount = 0

        # 9th bridge
        if 6530 <= abs(up.bgx) < 6780:
            dinomir.level = 230+400
            if dinomir.y==580 and dinomir.y!=dinomir.level:
                dinomir.y=dinomir.level
        # 9thbridgefall
        if 6800 < abs(up.bgx) < 6850 and dinomir.y > 229+400:
            dinomir.fall = True
            if dinomir.fall:
                dinomir.deathcount += 1
                dinomir.y = 400 - 116+400
            if dinomir.deathcount > 20 and dinomir.fall:
                dinomir.fall = False
                dinomir.y = 180+400
                dinomir.x+= 70
                dinomir.deathcount = 0
        if 6850 <= abs(up.bgx) < 7165:
            dinomir.level = 180+400


    def pumpmircollisons():
        # starting
        if 0 <= abs(low.bgx) < 770:
            pumpmir.level = 240
            if pumpmir.y == 180 and pumpmir.y != pumpmir.level:
                pumpmir.y = 240
        # firstjump and first stuck
        if 770 < abs(low.bgx) < 1330:
            pumpmir.level = 180
        if 760 < abs(low.bgx) < 780:
            pumpmir.stuck = True
        if pumpmir.stuck and pumpmir.y < 240:
            pumpmir.stuck = False
        # first fall
        if 1355 < abs(low.bgx) < 1430 and pumpmir.y > 179:
            pumpmir.fall = True
        if pumpmir.fall:
            pumpmir.deathcount += 1
            pumpmir.y = 400 - 116
        if pumpmir.deathcount > 20 and pumpmir.fall:
            pumpmir.fall = False
            pumpmir.y = 180
            pumpmir.x += 75
            pumpmir.deathcount = 0
        # 2nd bridge
        if 1430 <= abs(low.bgx) < 2130:
            pumpmir.level = 180
        # second fall
        if 2131 < abs(low.bgx) < 2210 and pumpmir.y > 179:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 230
                pumpmir.x += 80
                pumpmir.deathcount = 0
        # 3rd bridge
        if 2210 < abs(low.bgx) < 2495:
            pumpmir.level = 230
        # 3rdbridgebox
        if 2500 < abs(low.bgx) < 2590:
            pumpmir.level = 180
        if 2490 < abs(low.bgx) < 2520:
            pumpmir.stuck = True
        if pumpmir.stuck and pumpmir.y < 230:
            pumpmir.stuck = False
        # 3rdbridge continue
        if 2590 <= abs(low.bgx) < 2975:
            pumpmir.level = 230
            if pumpmir.y == 180 and pumpmir.y != pumpmir.level:
                pumpmir.y = pumpmir.level
        # 3rdbridge fall
        if 2990 < abs(low.bgx) < 3030 and pumpmir.y > 229:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 170
                pumpmir.x += 40
                pumpmir.deathcount = 0
        # 4thbridge
        if 3030 <= abs(low.bgx) < 3295:
            pumpmir.level = 170
        # 4thbridge fall
        if 3295 <= abs(low.bgx) < 3370 and pumpmir.y > 169:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 230
                pumpmir.x += 75
                pumpmir.deathcount = 0
        # 4thbridgelowerleftcrate
        if 3370 <= abs(low.bgx) < 4090:
            pumpmir.level = 230
            if pumpmir.y == 180 and pumpmir.y != pumpmir.level:
                pumpmir.y = 230
        # 4thbridgeendcrate
        if 4950 < abs(low.bgx) < 5030:
            pumpmir.level = 160
        if 4940 < abs(low.bgx) < 4955:
            pumpmir.stuck = True
        if pumpmir.stuck and pumpmir.y < 230:
            pumpmir.stuck = False
        # 4thbridgefall
        if 5060 < abs(low.bgx) < 5100 and pumpmir.y > 159:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 130
                pumpmir.x+= 45
                pumpmir.deathcount = 0
        # 5thbridge
        if 5100 <= abs(low.bgx) < 5240:
            pumpmir.level = 130
        # 6thbridge
        if 5245 < abs(low.bgx) < 5945:
            pumpmir.level = 230
            if pumpmir.y == 130 and pumpmir.y != pumpmir.level:
                pumpmir.y = 230
        # 7thbridge
        if 5960 < abs(low.bgx) < 6230:
            pumpmir.level = 180
        if 5950 < abs(low.bgx) < 5960:
            pumpmir.stuck = True
        if pumpmir.stuck and pumpmir.y < 230:
            pumpmir.stuck = False
        # 7thbridgefall
        if 6245 < abs(low.bgx) < 6325 and pumpmir.y > 179:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 180
                pumpmir.x+= 80
                pumpmir.deathcount = 0
        # 8thbridge
        if 6325 < abs(low.bgx) < 6445:
            pumpmir.level = 180
        # 8thbridgefall
        if 6460 < abs(low.bgx) < 6530 and pumpmir.y > 179:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 230
                pumpmir.x+= 70
                pumpmir.deathcount = 0
        # 9th bridge
        if 6530 <= abs(low.bgx) < 6780:
            pumpmir.level = 230
        # 9thbridgefall
        if 6800 < abs(low.bgx) < 6850 and pumpmir.y > 229:
            pumpmir.fall = True
            if pumpmir.fall:
                pumpmir.deathcount += 1
                pumpmir.y = 400 - 116
            if pumpmir.deathcount > 20 and pumpmir.fall:
                pumpmir.fall = False
                pumpmir.y = 180
                pumpmir.x+= 70
                pumpmir.deathcount = 0
        if 6850 <= abs(low.bgx) < 7165:
            pumpmir.level = 180


    def pumpcollisons():
        # starting
        if 0 <= abs(low.bgx) < 770:
            pump.level = 240 + 400
            if pumpmir.y == 180 + 400 and pump.y != pump.level:
                pump.y = 240 + 400
        # firstjump and first stuck
        if 770 < abs( low.bgx) < 1330:
            pump.level = 180 + 400
        if 760 < abs(low.bgx):
            pump.stuck = True
        if pump.stuck and pump.y < 240 + 400:
            pump.stuck = False
        # first fall
        if 1355 < abs(low.bgx) < 1430 and pump.y > 179 + 400:
            pump.fall = True
        if pump.fall:
            pump.deathcount += 1
            pump.y = 400 - 116 + 400
        if pump.deathcount > 20 and pump.fall:
            pump.fall = False
            pump.y = 180 + 400
            low.bgx -= 75
            dinomir.x-=75

            pump.deathcount = 0
        # 2nd bridge
        if 1430 <= abs(low.bgx) < 2130:
            pump.level = 180 + 400
        # second fall
        if 2131 < abs(low.bgx) < 2200 and pump.y > 179 + 400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116 + 400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 230 + 400
                low.bgx -= 80
                dinomir.x-=80
                pump.deathcount = 0
        # 3rd bridge
        if 2190 <= abs(low.bgx) < 2495:
            pump.level = 230 + 400
            if pump.y==580 and pump.y!=dino.level:
                pump.y=630
        # 3rdbridgebox
        if 2500 < abs(low.bgx) < 2590:
            pump.level = 180+400
        if 2490 < abs(low.bgx) < 2520:
            pump.stuck = True
        if pump.stuck and pump.y < 230 + 400:
            pump.stuck = False
        # 3rdbridge continue
        if 2590 <= abs(low.bgx) < 2975:
            pump.level = 230 + 400
            if pump.y == 180 + 400 and pump.y != pump.level:
                pump.y = pump.level
        # 3rdbridge fall
        if 2990 < abs(low.bgx) < 3030 and pump.y > 229 + 400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116+400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 170+400
                low.bgx -= 40
                dinomir.x -=40
                pump.deathcount = 0
        # 4thbridge
        if 3030 <= abs(low.bgx) < 3295:
            pump.level = 170+400
        # 4thbridge fall
        if 3295 <= abs(low.bgx) < 3370 and pump.y > 169+400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116+400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 230+400
                low.bgx -= 75
                dinomir.x -=75
                pump.deathcount = 0
        #4thbridge
        if 3360 <= abs(low.bgx) < 4940:
            pump.level = 230+400
            if pump.y == 580 and pump.y != pump.level:
                pump.y = pump.level
        # 4thbridgeendcrate
        if 4950 < abs(low.bgx) < 5030:
            pump.level = 160+400
        if 4940 < abs(low.bgx) < 4955:
            pump.stuck = True
        if pump.stuck and pump.y < 230+400:
            pump.stuck = False
        # 4thbridgefall
        if 5060 < abs(low.bgx) < 5100 and pump.y > 159+400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116+400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 130+400
                low.bgx -=45
                dinomir.x -=45
                pump.deathcount = 0
        # 5thbridge
        if 5100 <= abs(low.bgx) < 5240:
            pump.level = 130+400
        # 6thbridge
        if 5245 < abs(low.bgx) < 5945:
            pump.level = 230+400
            if pump.y == 130+400 and pump.y != pump.level:
                pump.y = 230+400
        # 7thbridge
        if 5960 < abs(low.bgx) < 6230:
            pump.level = 180+400
        if 5950 < abs(low.bgx) < 5960:
            pump.stuck = True
        if pump.stuck and pump.y < 230+400:
            pump.stuck = False
        # 7thbridgefall
        if 6245 < abs(low.bgx) < 6325 and pump.y > 179+400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116+400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 180+400
                low.bgx -= 80
                dinomir.x -=80
                pump.deathcount = 0
        # 8thbridge
        if 6320 <=abs(low.bgx) < 6445:
            pump.level = 180+400
        # 8thbridgefall
        if 6460 < abs(low.bgx) < 6530 and pump.y > 179+400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116+400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 230+400
                low.bgx -= 80
                dinomir.x -=80
                pump.deathcount = 0

        # 9th bridge
        if 6530 <= abs(low.bgx) < 6780:
            pump.level = 230+400
            if pump.y==580 and pump.y!=pump.level:
                pump.y=pump.level
        # 9thbridgefall
        if 6800 < abs(low.bgx) < 6850 and pump.y > 229+400:
            pump.fall = True
            if pump.fall:
                pump.deathcount += 1
                pump.y = 400 - 116+400
            if pump.deathcount > 20 and pump.fall:
                pump.fall = False
                pump.y = 180+400
                low.bgx -= 70
                dinomir.x -=70
                pump.deathcount = 0
        if 6850 <= abs(low.bgx) < 7165:
            pump.level = 180+400

    c1+=1
    c2+=1

    if c1>=500:
        if keys[K_z]:
            flashpump=True
            c1=0
    if c2>=500:
        if keys[K_KP0]:
            flashdino=True
            c2=0
    if flashpump:
        root.fill((250,250,250))
        if fpc<100:
            fpc+=1
        else:
            fpc=0
            flashpump=False
    if flashdino:
        root.fill((250,250,250))
        if fdc<100:
            fdc+=1
        else:
            fdc=0
            flashdino=False
    def callfunction():
        if not gameover:
            controls1()
            controls2()
            lower()
            upper()
            dinocollisons()
            dinomircollisons()
            pumpmircollisons()
            pumpcollisons()
    callfunction()
    print(dino.walkcount)
