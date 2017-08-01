from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3 as db
import sys

import MainMenu_ui
import Start_ui
import options_ui
import highscore_ui
import wonDialog_ui
import howToPlay_ui
import time
import calc


# High Score list window. Connects to database and retrieves the scores
class HighScoreWindow(QDialog, highscore_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setModal(True)
        self.pushButton.clicked.connect(self.onClose)
        self.showLeaderboard()

    def showLeaderboard(self):
        con = db.connect('highScore.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM highScores;")
            result = cur.fetchall()
            listData = []
            for row in result:
                # print(row)
                listData.append(list(row))

            for i in range(len(listData)):
                digit = listData[i][2]
                time = listData[i][3]
                tries = listData[i][4]
                listData[i].append(int(1000.0 * digit / tries**2 / time**0.5))
            sortedList = sorted(listData, key=lambda x: x[6], reverse=True)
        if con:
            con.close()

        leaderboard = """
        <table>
            <tr>
                <th> # </th>
                <th> Name </th>
                <th> Digit </th>
                <th> Time </th>
                <th> Tries </th>
                <th> Date </th>
                <th> Score </th>
            </tr>
        """
        count = 1
        for row in sortedList:
            name = row[1]
            digit = row[2]
            time = row[3]
            tries = row[4]
            date = row[5]
            score = row[6]
            leaderboard += """
            <tr>
            <td> %d </td>
            <td> %s </td>
            <td> %d </td>
            <td> %d </td>
            <td> %d </td>
            <td> %s </td>
            <td> %d </td>
            </tr>
            """
            leaderboard = leaderboard % (count, name, digit, time, tries, date, score)
            count += 1

        leaderboard += "</table>"
        # print(leaderboard)
        self.textEdit.setHtml(leaderboard)

    def onClose(self):
        self.close()

# Start Game window. In this window, the player will guess the number
class StartWindow(QDialog, Start_ui.Ui_Form):
    def __init__(self, digit):
        QDialog.__init__(self)
        self.startTime = time.time()
        self.setupUi(self)
        self.setModal(True)
        self.digit = digit
        self.alphaBeta = calc.alphaBeta(self.digit)
        self.label.setText("Guess My " + str(self.digit) + " Digit Number")
        self.pushButton.clicked.connect(self.checkGuess)
        self.count = 1

    def checkGuess(self):
        self.textEdit.selectAll()
        myGuess = int(self.lineEdit.text())
        response = self.alphaBeta.guess(myGuess)
        won = response[0]
        alpha = response[1]
        beta = response[2]
        if self.count == 1:
            currentText = ""
        else:
            currentText = self.textEdit.toHtml()
        self.textEdit.setHtml(currentText + str(self.count) + ") <strong>You guessed:</strong> " + str(myGuess) + " &rarr; " + str(alpha) + " &alpha; and " + str(beta) + " &#x3B2;")
        font = QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.count += 1
        if won:
            self.openWon()

    def openWon(self):
        self.pushButton.setDisabled(True)
        window = wonDialog(time.time() - self.startTime, self.count - 1, self.digit)
        window.show()
        window.exec_()

# This Dialog will show up when the player has won, and updates the database table with a given name
class wonDialog(QDialog, wonDialog_ui.Ui_Form):
    def __init__(self, time, tries, digit):
        QDialog.__init__(self)
        self.time = time
        self.tries = tries
        self.digit = digit
        self.setupUi(self)
        self.setModal(True)
        self.pushButton.clicked.connect(self.onClose)

    def onClose(self):
        self.addScore(self.lineEdit.text())
        self.close()

    def addScore(self, name):
        con = db.connect('highScore.db')
        cur = con.cursor()
        print("Connected!")
        with con:
            cur.execute("""
                    INSERT INTO highScores(Name, Digit, Time, Tries, Date) VALUES(?,?,?,?,?)""",
                    (name, self.digit, int(self.time), self.tries, time.strftime("%Y/%m/%d")))
        con.commit()

        if con:
            con.close()

# Options window. The Player can change the digits in here.
class OptionsWindow(QDialog, options_ui.Ui_Form):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setModal(True)
        self.pushButton.clicked.connect(self.onSave)
        self.pushButton_2.clicked.connect(self.onClose)
        self.partnerDialog = parent

    def onSave(self):
        self.partnerDialog.digit = int(self.spinBox.text())
        self.close()

    def onClose(self):
        self.close()

# How to Play Window. Sime info showing window with close button
class HowToPlayWindow(QDialog, howToPlay_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setModal(True)
        self.pushButton.clicked.connect(self.onClose)

    def onClose(self):
        self.close()

# Main Menu window. The Player can navigate to all the menus
class MainWindow(QDialog, MainMenu_ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.digit = 4
        self.createDatabase()
        self.pushButton.clicked.connect(self.openStart)
        self.pushButton_2.clicked.connect(self.openHighScore)
        self.pushButton_3.clicked.connect(self.openOptions)
        self.pushButton_4.clicked.connect(self.openHowToPlay)

    def createDatabase(self):
        con = db.connect('highScore.db')
        with con:
            cur = con.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS highScores(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Digit INTEGER,
            Time INTEGER,
            Tries INTEGER,
            Date DATE
            );""")

        if con:
            con.close()

    def openStart(self):
        window = StartWindow(self.digit)
        window.show()
        window.exec_()

    def openOptions(self):
        window = OptionsWindow(self)
        window.show()
        window.exec_()

    def openHighScore(self):
        window = HighScoreWindow()
        window.show()
        window.exec_()

    def openHowToPlay(self):
        window = HowToPlayWindow()
        window.show()
        window.exec_()

# Start the application
def run():
    app = QApplication(sys.argv)
    alphaBeta = MainWindow()
    alphaBeta.show()
    app.exec_()

if __name__ == '__main__':
    run()