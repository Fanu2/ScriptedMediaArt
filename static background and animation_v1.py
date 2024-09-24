import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPainter

class AnimatedSvgWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SVG Animation Example')
        self.setGeometry(100, 100, 800, 600)

        # Set up the graphics view and scene
        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

        # Load static SVG background
        self.background_svg_path = QFileDialog.getOpenFileName(self, 'Select Background SVG File', '', 'SVG Files (*.svg)')[0]
        if not self.background_svg_path:
            QMessageBox.critical(self, 'Error', 'No background SVG file selected.')
            sys.exit()

        self.background_svg_item = QGraphicsSvgItem(self.background_svg_path)
        self.background_svg_item.setFlag(QGraphicsSvgItem.ItemClipsToShape)
        self.scene.addItem(self.background_svg_item)

        # Load animated SVG character
        self.character_svg_path = QFileDialog.getOpenFileName(self, 'Select Character SVG File', '', 'SVG Files (*.svg)')[0]
        if not self.character_svg_path:
            QMessageBox.critical(self, 'Error', 'No character SVG file selected.')
            sys.exit()

        self.character_svg_item = QGraphicsSvgItem(self.character_svg_path)
        self.character_svg_item.setFlag(QGraphicsSvgItem.ItemClipsToShape)
        self.scene.addItem(self.character_svg_item)

        # Initialize animation parameters
        self.character_x_pos = 0
        self.character_y_pos = 250  # Start position of the character
        self.frame_number = 0

        # Create a temporary directory to store frames
        self.temp_dir = '/tmp/animation_frames'
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

        # Prompt for output file name
        self.output_file_name, _ = QInputDialog.getText(self, 'Save Animation', 'Enter output video file name (e.g., animation.mp4):')
        if not self.output_file_name:
            QMessageBox.critical(self, 'Error', 'No output file name provided.')
            sys.exit()

        self.output_file_path = os.path.join('/home/jasvir/Pictures/', self.output_file_name)

        # Set up the animation parameters
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_timer.start(30)  # Update every 30 ms

    def update_animation(self):
        # Update the position of the character
        self.character_x_pos += 5  # Move right by 5 units
        if self.character_x_pos > self.view.width():
            self.character_x_pos = -self.character_svg_item.boundingRect().width()  # Reset to start position

        # Update the position of the character item
        self.character_svg_item.setPos(self.character_x_pos, self.character_y_pos)

        # Save frame to video
        self.save_frame()

    def save_frame(self):
        # Render the scene to an image
        image = QImage(self.view.size(), QImage.Format_ARGB32)
        painter = QPainter(image)
        self.view.render(painter)
        painter.end()

        # Save the image to a file
        frame_file_name = os.path.join(self.temp_dir, f'frame_{self.frame_number:04d}.png')
        image.save(frame_file_name)
        self.frame_number += 1

        # If the animation is complete, compile frames into a video
        if self.character_x_pos <= -self.character_svg_item.boundingRect().width():
            self.animation_timer.stop()
            self.compile_video()

    def compile_video(self):
        # Compile the frames into a video using ffmpeg
        ffmpeg_cmd = [
            'ffmpeg',
            '-framerate', '30',  # Set frame rate
            '-i', os.path.join(self.temp_dir, 'frame_%04d.png'),  # Input pattern
            '-c:v', 'libx264',  # Codec
            '-pix_fmt', 'yuv420p',  # Pixel format
            self.output_file_path
        ]
        subprocess.run(ffmpeg_cmd, check=True)

        # Clean up temporary files
        for file_name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file_name))
        os.rmdir(self.temp_dir)

        QMessageBox.information(self, 'Success', f'Animation saved to {self.output_file_path}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimatedSvgWindow()
    window.show()
    sys.exit(app.exec_())
