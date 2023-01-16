import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import PRM


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.obstacles = []
        self.qinit = (0, 0)
        self.qend = (0, 0)
        self.edges = []
        self.vertices = []
        self.flag = False
        self.result = []
        self.dist = 0
        self.n = 300
        self.k = 30

        self.setStyleSheet("background-color: #0e7c52;"
                           "")

        self.start_button = QPushButton(self)
        self.start_button.setGeometry(QRect(20, 790, 141, 41))
        self.start_button.setStyleSheet("background-color: #26d98f;"
                                        "font: italic 16pt \"Book Antiqua\";"
                                        "border-radius: 10;")
        self.start_button.setObjectName("start_button")
        self.start_button.setText("Start")
        self.start_button.clicked.connect(self.start)

        self.exit_button = QPushButton(self)
        self.exit_button.setGeometry(QRect(20, 840, 141, 41))
        self.exit_button.setStyleSheet("background-color: #26d98f;\n"
                                       "font: italic 16pt \"Book Antiqua\";\n"
                                       "border-radius: 10;")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setText("Exit")
        self.exit_button.clicked.connect(self.stop)

        self.add_qend = QPushButton(self)
        self.add_qend.setGeometry(QRect(190, 840, 141, 41))
        self.add_qend.setStyleSheet("background-color: #fc4052;\n"
                                    "font: italic 16pt \"Book Antiqua\";\n"
                                    "border-radius: 10;")
        self.add_qend.setObjectName("add_qend")
        self.add_qend.setText("Add Qend")
        self.add_qend.clicked.connect(self.get_qend)

        self.add_qinit = QPushButton(self)
        self.add_qinit.setGeometry(QRect(190, 790, 141, 41))
        self.add_qinit.setStyleSheet("background-color: #fc4052;\n"
                                     "font: italic 16pt \"Book Antiqua\";\n"
                                     "border-radius: 10;")
        self.add_qinit.setObjectName("add_qinit")
        self.add_qinit.setText("Add Qinit")
        self.add_qinit.clicked.connect(self.get_qinit)

        self.export_button = QPushButton(self)
        self.export_button.setGeometry(QRect(860, 840, 141, 41))
        self.export_button.setStyleSheet("background-color: #26d98f;\n"
                                         "font: italic 16pt \"Book Antiqua\";\n"
                                         "border-radius: 10;")
        self.export_button.setObjectName("export_button")
        self.export_button.setText("Export")
        self.export_button.clicked.connect(self.export_scene)

        self.import_button = QPushButton(self)
        self.import_button.setGeometry(QRect(860, 790, 141, 41))
        self.import_button.setStyleSheet("background-color: #26d98f;\n"
                                         "font: italic 16pt \"Book Antiqua\";\n"
                                         "border-radius: 10;")
        self.import_button.setObjectName("import_button")
        self.import_button.setText("Import")
        self.import_button.clicked.connect(self.import_scene)

        self.add_obstacle_button = QPushButton(self)
        self.add_obstacle_button.setGeometry(QRect(610, 790, 231, 41))
        self.add_obstacle_button.setStyleSheet("background-color: #26d98f;\n"
                                               "font: italic 16pt \"Book Antiqua\";\n"
                                               "border-radius: 10;")
        self.add_obstacle_button.setObjectName("add_obstacle_button")
        self.add_obstacle_button.setText("Add obstacle")
        self.add_obstacle_button.clicked.connect(self.add_obstacle)

        self.input_qinit = QLineEdit(self)
        self.input_qinit.setGeometry(QRect(340, 800, 91, 21))
        self.input_qinit.setLayoutDirection(Qt.LeftToRight)
        self.input_qinit.setStyleSheet("background-color: #25d88e;\n"
                                       "font: 10pt \"Book Antiqua\";\n"
                                       "border-radius: 5;")
        self.input_qinit.setObjectName("input_qinit")
        self.input_qinit.setText("Qinit point")

        self.input_qend = QLineEdit(self)
        self.input_qend.setGeometry(QRect(340, 850, 91, 21))
        self.input_qend.setLayoutDirection(Qt.LeftToRight)
        self.input_qend.setStyleSheet("background-color: #25d88e;\n"
                                      "font: 10pt \"Book Antiqua\";\n"
                                      "border-radius: 5;")
        self.input_qend.setObjectName("input_qend")
        self.input_qend.setText("Qend point")

        self.input_obst_max = QLineEdit(self)
        self.input_obst_max.setGeometry(QRect(470, 850, 131, 21))
        self.input_obst_max.setLayoutDirection(Qt.LeftToRight)
        self.input_obst_max.setStyleSheet("background-color: #25d88e;\n"
                                          "font: 10pt \"Book Antiqua\";\n"
                                          "border-radius: 5;")
        self.input_obst_max.setObjectName("input_obst_max")
        self.input_obst_max.setText("obstacle x2, y2")

        self.input_obst_min = QLineEdit(self)
        self.input_obst_min.setGeometry(QRect(470, 800, 131, 21))
        self.input_obst_min.setLayoutDirection(Qt.LeftToRight)
        self.input_obst_min.setStyleSheet("background-color: #25d88e;\n"
                                          "font: 10pt \"Book Antiqua\";\n"
                                          "border-radius: 5;")
        self.input_obst_min.setText("obstacle x1, y1")

        self.input_n = QLineEdit(self)
        self.input_n.setGeometry(QRect(610, 850, 40, 21))
        self.input_n.setLayoutDirection(Qt.LeftToRight)
        self.input_n.setStyleSheet("background-color: #25d88e;\n"
                                   "font: 10pt \"Book Antiqua\";\n"
                                   "border-radius: 5;")
        self.input_n.setText("n")

        self.input_k = QLineEdit(self)
        self.input_k.setGeometry(QRect(660, 850, 20, 21))
        self.input_k.setLayoutDirection(Qt.LeftToRight)
        self.input_k.setStyleSheet("background-color: #25d88e;\n"
                                   "font: 10pt \"Book Antiqua\";\n"
                                   "border-radius: 5;")
        self.input_k.setText("k")

        self.add_n_k = QPushButton(self)
        self.add_n_k.setGeometry(QRect(700, 840, 141, 41))
        self.add_n_k.setStyleSheet("background-color: #fc4052;\n"
                                   "font: italic 16pt \"Book Antiqua\";\n"
                                   "border-radius: 10;")
        self.add_n_k.setObjectName("add_qinit")
        self.add_n_k.setText("Add n, k")
        self.add_n_k.clicked.connect(self.set_n_k)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(QRect(300, 900, 400, 41))
        self.result_label.setStyleSheet("background-color: #ffffff;\n"
                                        "font: italic 16pt \"Book Antiqua\";\n"
                                        "border-radius: 10;")
        self.result_label.setText(f"  Result: ")

    def get_qinit(self):
        self.qinit = tuple(int(item) for item in self.input_qinit.text().split(','))
        return tuple(int(item) for item in self.input_qinit.text().split(','))

    def get_qend(self):
        self.qend = tuple(int(item) for item in self.input_qend.text().split(','))
        return tuple(int(item) for item in self.input_qend.text().split(','))

    def get_obst_min(self):
        return tuple(int(item) for item in self.input_obst_min.text().split(','))

    def get_obst_max(self):
        return tuple(int(item) for item in self.input_obst_max.text().split(','))

    def set_n_k(self):
        self.n = int(self.input_n.text())
        self.k = int(self.input_k.text())

    def add_obstacle(self):
        a = self.get_obst_min()
        b = self.get_obst_max()
        self.obstacles.append(PRM.Ugolnic(*a, *b))

    def import_scene(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        with open(f'{filename}', 'r') as F:
            lines = F.readlines()

        self.n = int(lines[0])
        self.k = int(lines[1])
        self.qinit = tuple(map(int, lines[2].split(', ')))
        self.qend = tuple(map(int, lines[3].split(', ')))
        self.obstacles = []
        for i in range(4, len(lines)):
            line = tuple(map(int, lines[i].split(', ')))
            self.obstacles.append(PRM.Ugolnic(line[0], line[1], line[2], line[3]))

    def export_scene(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        with open(f'{filename}', 'w') as F:
            F.write(f'{self.n}' + '\n')
            F.write(f'{self.k}' + '\n')
            F.write(f'{self.qinit}'[1:-1:] + '\n')
            F.write(f'{self.qend}'[1:-1:] + '\n')
            for item in self.obstacles:
                F.write(f'{item.point_min}'[1:-1:] + ', ' + f'{item.point_max}'[1:-1:] + '\n')

    def stop(self):
        exit(0)

    def create_obstacle(self):
        self.obstacles.append(
            PRM.Ugolnic((int(self.obstacle_min_input_x.text()), int(self.obstacle_min_input_y.text())),
                        (int(self.obstacle_max_input_x.text()), int(self.obstacle_max_input_y.text()))))

    def start(self):
        self.edges, self.vertices, self.result, self.dist = PRM.PRM(self.n, self.k, self.qinit, self.qend,
                                                                    self.obstacles)
        if self.dist == '':
            self.result_label.setText("  Unable to find the path")
        else:
            self.result_label.setText(f"  Result: {self.dist}")
        self.flag = True

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.white, 10, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.drawRect(20, 20, 981, 740)
        if self.flag:
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            for obstacle in self.obstacles:
                painter.drawLine(20 + obstacle.points[0][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[0][1],
                                 20 + obstacle.points[2][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[2][1])
                painter.drawLine(20 + obstacle.points[1][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[1][1],
                                 20 + obstacle.points[2][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[2][1])
                painter.drawLine(20 + obstacle.points[1][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[1][1],
                                 20 + obstacle.points[3][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[3][1])
                painter.drawLine(20 + obstacle.points[0][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[0][1],
                                 20 + obstacle.points[3][0], 20 + PRM.Y_MAX_CRUTOI - obstacle.points[3][1])
            for edge in self.edges:
                painter.setPen(QPen(Qt.green, 0.5, Qt.SolidLine))
                painter.drawLine(20 + edge[0][0], 20 + PRM.Y_MAX_CRUTOI - edge[0][1],
                                 20 + edge[1][0], 20 + PRM.Y_MAX_CRUTOI - edge[1][1])
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            for i in range(0, len(self.result) - 1):
                painter.drawLine(20 + self.result[i][0], 20 + PRM.Y_MAX_CRUTOI - self.result[i][1],
                                 20 + self.result[i + 1][0], 20 + PRM.Y_MAX_CRUTOI - self.result[i + 1][1])
            for v in self.vertices:
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(20 + v[0] - 2, 20 + PRM.Y_MAX_CRUTOI - v[1] - 2, 4, 4)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawEllipse(20 + self.qinit[0] - 5, 20 + PRM.Y_MAX_CRUTOI - self.qinit[1] - 5, 10, 10)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawEllipse(20 + self.qend[0] - 5, 20 + PRM.Y_MAX_CRUTOI - self.qend[1] - 5, 10, 10)
            self.update()
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.resize(1038, 958)
    ex.show()
    sys.exit(app.exec_())
