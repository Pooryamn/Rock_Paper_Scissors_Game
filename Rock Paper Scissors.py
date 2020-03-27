import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import QTimer
from random import randint

################# FONTS #################
TextFONT = QFont("Times",12)
ButtonFONT = QFont("Arial",12)

################# Global Variables #################
CScore = 0 # Compute score
UScore = 0 # User score 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game 1")
        self.setGeometry(350,150,550,300)
        self.setFixedSize(self.width(),self.height())
        self.setWindowIcon(QIcon('resources/images/game1_Icon.png'))
        self.UI()
        

    def UI(self):
        # all your code is here :

        ################# Labels #################

        self.ComputerScore = QLabel("Computer Score : ",self)
        self.ComputerScore.setGeometry(30,20,150,35)
        self.ComputerScore.setFont(TextFONT)

        self.UserScore = QLabel("User Score : ",self)
        self.UserScore.setGeometry(360,20,150,35)
        self.UserScore.setFont(TextFONT)

        
        ################# Pixmaps #################
        self.RockImg = QPixmap('resources/images/Rock.png')

        self.PaperImg = QPixmap('resources/images/Paper.png')
        self.ScissorsImg = QPixmap('resources/images/Scissors.png')


        ################# Images #################

        # Computer image :
        self.ComputerImg = QLabel(self)
        self.RockImg = self.RockImg.scaledToHeight(100)
        self.ComputerImg.setPixmap(self.RockImg)
        self.ComputerImg.move(50,100)

        # User Rock image :
        self.UserRock = QLabel(self)
        self.RockImg = self.RockImg.scaledToHeight(50)
        self.UserRock.setPixmap(self.RockImg)
        self.UserRock.move(330,125)
        self.UserRock.mousePressEvent = self.Rock_pressed

        # User Paper image :
        self.UserPaper = QLabel(self)
        self.PaperImg = self.PaperImg.scaledToHeight(50)
        self.UserPaper.setPixmap(self.PaperImg)
        self.UserPaper.move(385,125)
        self.UserPaper.mousePressEvent = self.Paper_pressd

        # User Scissors image : 
        self.UserScissors = QLabel(self)
        self.ScissorsImg = self.ScissorsImg.scaledToHeight(50)
        self.UserScissors.setPixmap(self.ScissorsImg)
        self.UserScissors.move(440,125)
        self.UserScissors.mousePressEvent = self.Scissors_pressed

        ################# Buttons #################
        btn_start = QPushButton("&Start",self)
        btn_start.setFont(ButtonFONT)
        btn_start.move(175,250)
        btn_start.clicked.connect(self.start)

        btn_stop = QPushButton("S&top",self)
        btn_stop.setFont(ButtonFONT)
        btn_stop.move(285,250)
        btn_stop.clicked.connect(self.stop)

        ################# Timmer #################
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Play)

        self.show()

    def Play(self):
        self.RndComp = randint(1,3) # generate 1 to 3 random integer

        if(self.RndComp == 1):
            
            self.RockImg = self.RockImg.scaledToHeight(100)
            self.ComputerImg.setPixmap(self.RockImg)

        elif(self.RndComp == 2):
            
            self.PaperImg = self.PaperImg.scaledToHeight(100)
            self.ComputerImg.setPixmap(self.PaperImg)

        elif(self.RndComp == 3):
            
            self.ScissorsImg = self.ScissorsImg.scaledToHeight(100)
            self.ComputerImg.setPixmap(self.ScissorsImg)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def Rock_pressed(self,event):

        if(self.timer.isActive() == False):
            return

        self.UserChoise = 1
        self.timer.stop()
        
        global CScore 
        global UScore

        if (self.RndComp == 1):
            # Draw game
            QMessageBox.about(self,"Stop","Draw Game")
        elif (self.RndComp == 2):
            # Computer
            QMessageBox.about(self,"Stop","CPU wins")
            CScore += 1
            self.ComputerScore.setText("Computer Score : {0}".format(CScore))
        else:
            # user
            QMessageBox.about(self,"Stop","User wins")
            UScore += 1
            self.UserScore.setText("User Score : {0}".format(UScore))

    
    def Paper_pressd(self,event):

        if(self.timer.isActive() == False):
            return

        self.UserChoise = 2
        self.timer.stop()

        global CScore 
        global UScore

        if (self.RndComp == 1):
            # user
            QMessageBox.about(self,"Stop","User wins")
            UScore += 1
            self.UserScore.setText("User Score : {0}".format(UScore))

        elif (self.RndComp == 2):
            # Draw game
            QMessageBox.about(self,"Stop","Draw Game")            
        else:
            # Computer
            QMessageBox.about(self,"Stop","CPU wins")
            CScore += 1
            self.ComputerScore.setText("Computer Score : {0}".format(CScore))


    def Scissors_pressed(self,event):

        if(self.timer.isActive() == False):
            return

        self.UserChoise = 3
        self.timer.stop()

        global CScore 
        global UScore

        if (self.RndComp == 1):

            # Computer
            QMessageBox.about(self,"Stop","CPU wins")
            CScore += 1
            self.ComputerScore.setText("Computer Score : {0}".format(CScore))

        elif (self.RndComp == 2):
            # user
            QMessageBox.about(self,"Stop","User wins")
            UScore += 1
            self.UserScore.setText("User Score : {0}".format(UScore))
        else:
            # Draw game
            QMessageBox.about(self,"Stop","Draw Game")



def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()