import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox

class VideoProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Video Processor')
        layout = QVBoxLayout()

        self.info_label = QLabel('Select the input files and output location:')
        layout.addWidget(self.info_label)

        self.image_btn = QPushButton('Select Image File')
        self.image_btn.clicked.connect(self.select_image_file)
        layout.addWidget(self.image_btn)

        self.audio_btn = QPushButton('Select Audio File')
        self.audio_btn.clicked.connect(self.select_audio_file)
        layout.addWidget(self.audio_btn)

        self.subtitle_btn = QPushButton('Select Subtitle File')
        self.subtitle_btn.clicked.connect(self.select_subtitle_file)
        layout.addWidget(self.subtitle_btn)

        self.output_btn = QPushButton('Select Output File')
        self.output_btn.clicked.connect(self.select_output_file)
        layout.addWidget(self.output_btn)

        self.process_btn = QPushButton('Create Video')
        self.process_btn.clicked.connect(self.create_video)
        layout.addWidget(self.process_btn)

        self.setLayout(layout)

    def select_image_file(self):
        options = QFileDialog.Options()
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.jpg *.jpeg *.png);;All Files (*)", options=options)
        if self.image_path:
            self.info_label.setText(f'Selected Image: {self.image_path}')

    def select_audio_file(self):
        options = QFileDialog.Options()
        self.audio_path, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.mp3 *.wav);;All Files (*)", options=options)
        if self.audio_path:
            self.info_label.setText(f'Selected Audio: {self.audio_path}')

    def select_subtitle_file(self):
        options = QFileDialog.Options()
        self.subtitle_path, _ = QFileDialog.getOpenFileName(self, "Select Subtitle File", "", "ASS Files (*.ass);;All Files (*)", options=options)
        if self.subtitle_path:
            self.info_label.setText(f'Selected Subtitle: {self.subtitle_path}')

    def select_output_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Output File Path", "", "MP4 Files (*.mp4);;All Files (*)", options=options)
        if file_name:
            # Ensure the file name ends with .mp4
            if not file_name.endswith(".mp4"):
                file_name += ".mp4"
            self.output_path = file_name
            self.info_label.setText(f'Selected Output: {self.output_path}')

    def create_video(self):
        if not all([self.image_path, self.audio_path, self.subtitle_path, self.output_path]):
            QMessageBox.warning(self, "Missing Information", "Please select all the required files.")
            return

        command = [
            'ffmpeg',
            '-loop', '1',
            '-i', self.image_path,
            '-i', self.audio_path,
            '-vf', f'ass={self.subtitle_path}',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-strict', 'experimental',
            '-shortest',
            '-y',  # Overwrite output file if it exists
            self.output_path
        ]

        try:
            subprocess.run(command, check=True)
            QMessageBox.information(self, "Success", "Video created successfully.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

if __name__ == '__main__':
    app = QApplication([])
    processor = VideoProcessor()
    processor.show()
    app.exec_()
