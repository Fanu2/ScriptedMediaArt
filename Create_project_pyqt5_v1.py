import os
import subprocess

# Project setup
project_name = "PyQt5_Suite"
project_path = os.path.join("/home/jasvir/PycharmProjects", project_name)
virtual_env_path = os.path.join(project_path, "venv")

# PyQt5 Applications
applications = {
    "TextEditor": "text_editor.py",
    "ImageViewer": "image_viewer.py",
    "Calculator": "calculator.py",
    "ToDoList": "to_do_list.py",
    "MediaPlayer": "media_player.py",
    "FileExplorer": "file_explorer.py",
    "PaintApplication": "paint_app.py",
    "VideoTrimmer": "video_trimmer.py",
    "VideoMerger": "video_merger.py",
    "VideoResizer": "video_resizer.py",
    "VideoConverter": "video_converter.py",
    "VideoWatermark": "video_watermark.py"
}

# Create project directory
os.makedirs(project_path, exist_ok=True)

# Create virtual environment
subprocess.run(["python3", "-m", "venv", virtual_env_path])

# Activate virtual environment
activate_env = f"source {virtual_env_path}/bin/activate"

# Install PyQt5 and additional packages in virtual environment
subprocess.run(f"{activate_env} && pip install PyQt5 moviepy opencv-python", shell=True)

# Create directories and files for each application
for app_name, script_name in applications.items():
    app_dir = os.path.join(project_path, app_name)
    os.makedirs(app_dir, exist_ok=True)

    script_path = os.path.join(app_dir, script_name)

    # Example code for each application
    app_code = {
        "text_editor.py": """# Text Editor Example
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Text Editor')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
""",
        "image_viewer.py": """# Image Viewer Example
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QAction
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Image Viewer')

        openFile = QAction('Open', self)
        openFile.triggered.connect(self.showDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)

    def showDialog(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname:
            pixmap = QPixmap(fname)
            self.label.setPixmap(pixmap)
            self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
""",
        "calculator.py": """# Calculator Example
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.display = QLineEdit()
        vbox.addWidget(self.display)
        grid = QGridLayout()
        vbox.addLayout(grid)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        positions = [(i, j) for i in range(4) for j in range(4)]
        for position, name in zip(positions, buttons):
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.on_click)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Calculator')

    def on_click(self):
        sender = self.sender()
        text = sender.text()
        current = self.display.text()
        if text == '=':
            try:
                result = str(eval(current))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(current + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
""",
        "to_do_list.py": """# To-Do List Example
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget, QPushButton

class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.listWidget = QListWidget()
        vbox.addWidget(self.listWidget)
        self.textBox = QLineEdit(self)
        vbox.addWidget(self.textBox)
        addButton = QPushButton("Add Task")
        vbox.addWidget(addButton)
        addButton.clicked.connect(self.add_task)
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('To-Do List')

    def add_task(self):
        task = self.textBox.text()
        if task:
            self.listWidget.addItem(task)
            self.textBox.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo = ToDoList()
    todo.show()
    sys.exit(app.exec_())
""",
        "media_player.py": """# Media Player Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QStyle, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.setCentralWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        openFile = QAction('Open', self)
        openFile.triggered.connect(self.open_file)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Media Player')

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.mediaPlayer.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MediaPlayer()
    player.show()
    sys.exit(app.exec_())
""",
        "file_explorer.py": """# File Explorer Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QTreeView

class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.setCentralWidget(self.tree)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('File Explorer')
        self.tree.setRootIndex(self.model.index(''))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    explorer = FileExplorer()
    explorer.show()
    sys.exit(app.exec_())
""",
        "paint_app.py": """# Paint Application Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint

class PaintApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.canvas = QLabel(self)
        self.canvas.setGeometry(0, 0, 800, 600)
        self.canvas.setPixmap(QPixmap(800, 600))
        self.canvas.pixmap().fill(Qt.white)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Paint Application')
        self.last_point = QPoint()
        self.drawing = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.canvas.pixmap())
            painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = PaintApplication()
    mainWindow.show()
    sys.exit(app.exec_())
""",
        "video_trimmer.py": """# Video Trimmer Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from moviepy.editor import VideoFileClip

class VideoTrimmer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Trimmer')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()
        self.status_label = QLabel("No file selected", self)
        layout.addWidget(self.status_label)

        self.select_button = QPushButton("Select Video", self)
        self.select_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_button)

        self.trim_button = QPushButton("Trim Video", self)
        self.trim_button.clicked.connect(self.trim_video)
        layout.addWidget(self.trim_button)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def select_video(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File")
        if self.file_path:
            self.status_label.setText(f"Selected file: {self.file_path}")

    def trim_video(self):
        if hasattr(self, 'file_path') and self.file_path:
            clip = VideoFileClip(self.file_path)
            trimmed_clip = clip.subclip(0, min(10, clip.duration))  # Trim first 10 seconds or less
            trimmed_clip.write_videofile("trimmed_output.mp4")
            self.status_label.setText("Video trimmed and saved as trimmed_output.mp4")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = VideoTrimmer()
    mainWindow.show()
    sys.exit(app.exec_())
""",
        "video_merger.py": """# Video Merger Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from moviepy.editor import VideoFileClip, concatenate_videoclips

class VideoMerger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Merger')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()
        self.status_label = QLabel("No files selected", self)
        layout.addWidget(self.status_label)

        self.select_button = QPushButton("Select Videos", self)
        self.select_button.clicked.connect(self.select_videos)
        layout.addWidget(self.select_button)

        self.merge_button = QPushButton("Merge Videos", self)
        self.merge_button.clicked.connect(self.merge_videos)
        layout.addWidget(self.merge_button)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def select_videos(self):
        self.file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Video Files")
        if self.file_paths:
            self.status_label.setText(f"Selected files: {', '.join(self.file_paths)}")

    def merge_videos(self):
        if hasattr(self, 'file_paths') and self.file_paths:
            clips = [VideoFileClip(f) for f in self.file_paths]
            merged_clip = concatenate_videoclips(clips)
            merged_clip.write_videofile("merged_output.mp4")
            self.status_label.setText("Videos merged and saved as merged_output.mp4")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = VideoMerger()
    mainWindow.show()
    sys.exit(app.exec_())
""",
        "video_resizer.py": """# Video Resizer Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from moviepy.editor import VideoFileClip

class VideoResizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Resizer')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()
        self.status_label = QLabel("No file selected", self)
        layout.addWidget(self.status_label)

        self.select_button = QPushButton("Select Video", self)
        self.select_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_button)

        self.resize_button = QPushButton("Resize Video", self)
        self.resize_button.clicked.connect(self.resize_video)
        layout.addWidget(self.resize_button)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def select_video(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File")
        if self.file_path:
            self.status_label.setText(f"Selected file: {self.file_path}")

    def resize_video(self):
        if hasattr(self, 'file_path') and self.file_path:
            clip = VideoFileClip(self.file_path)
            resized_clip = clip.resize(width=640)  # Resize to width 640, maintaining aspect ratio
            resized_clip.write_videofile("resized_output.mp4")
            self.status_label.setText("Video resized and saved as resized_output.mp4")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = VideoResizer()
    mainWindow.show()
    sys.exit(app.exec_())
""",
        "video_converter.py": """# Video Converter Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from moviepy.editor import VideoFileClip

class VideoConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Converter')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()
        self.status_label = QLabel("No file selected", self)
        layout.addWidget(self.status_label)

        self.select_button = QPushButton("Select Video", self)
        self.select_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_button)

        self.convert_button = QPushButton("Convert Video", self)
        self.convert_button.clicked.connect(self.convert_video)
        layout.addWidget(self.convert_button)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def select_video(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File")
        if self.file_path:
            self.status_label.setText(f"Selected file: {self.file_path}")

    def convert_video(self):
        if hasattr(self, 'file_path') and self.file_path:
            clip = VideoFileClip(self.file_path)
            clip.write_videofile("converted_output.mp4", codec='libx264')
            self.status_label.setText("Video converted and saved as converted_output.mp4")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = VideoConverter()
    mainWindow.show()
    sys.exit(app.exec_())
""",
        "video_watermark.py": """# Video Watermark Example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip

class VideoWatermark(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Watermark')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()
        self.status_label = QLabel("No files selected", self)
        layout.addWidget(self.status_label)

        self.select_video_button = QPushButton("Select Video", self)
        self.select_video_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_video_button)

        self.select_watermark_button = QPushButton("Select Watermark", self)
        self.select_watermark_button.clicked.connect(self.select_watermark)
        layout.addWidget(self.select_watermark_button)

        self.add_watermark_button = QPushButton("Add Watermark", self)
        self.add_watermark_button.clicked.connect(self.add_watermark)
        layout.addWidget(self.add_watermark_button)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def select_video(self):
        self.video_path, _ = QFileDialog.getOpenFileName(self, "Select Video File")
        if self.video_path:
            self.status_label.setText(f"Selected video: {self.video_path}")

    def select_watermark(self):
        self.watermark_path, _ = QFileDialog.getOpenFileName(self, "Select Watermark Image")
        if self.watermark_path:
            self.status_label.setText(f"Selected watermark: {self.watermark_path}")

    def add_watermark(self):
        if hasattr(self, 'video_path') and hasattr(self, 'watermark_path'):
            video_clip = VideoFileClip(self.video_path)
            watermark = ImageClip(self.watermark_path).set_duration(video_clip.duration).resize(height=100).set_pos(("right", "bottom"))
            watermarked_clip = CompositeVideoClip([video_clip, watermark])
            watermarked_clip.write_videofile("watermarked_output.mp4")
            self.status_label.setText("Watermark added and saved as watermarked_output.mp4")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = VideoWatermark()
    mainWindow.show()
    sys.exit(app.exec_())
"""
    }

    for app_name, script in video_editing_apps.items():
        app_file_path = os.path.join(project_path, app_name)
        with open(app_file_path, "w") as file:
            file.write(script)
        print(f"Created: {app_file_path}")


# Create virtual environment and setup
def create_virtual_environment(project_path):
    venv_path = os.path.join(project_path, 'venv')
    os.system(f"python3 -m venv {venv_path}")
    pip_install_cmd = f"{venv_path}/bin/pip install PyQt5 moviepy"
    os.system(pip_install_cmd)


create_virtual_environment(project_path)
print("Virtual environment created and packages installed.")
