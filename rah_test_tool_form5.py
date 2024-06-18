#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import QProcess

class ToolingControlForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.process = None  # Initialize the process variable

    def initUI(self):
        self.setWindowTitle('Tooling Control Form')
        self.setGeometry(100, 100, 800, 600)

        layout = QGridLayout()

        # Left Column Buttons
        left_buttons = [
            "Set Matrix", "Create Working Step",
        ]

        self.buttons = {}  # Dictionary to hold buttons for easier reference

        for i, text in enumerate(left_buttons):
            btn = QPushButton(text)
            btn.setFixedHeight(30)
            layout.addWidget(btn, i, 0)
            self.buttons[text] = btn

        # Connect the "Set Matrix" button to the set_matrix method
        self.buttons["Set Matrix"].clicked.connect(self.set_matrix)

        # Connect the "Create Working Step" button to the create_working_step method
        self.buttons["Create Working Step"].clicked.connect(self.create_working_step)

        self.setLayout(layout)

    def set_matrix(self):
        # Method to handle the Set Matrix button click
        print("Set Matrix button clicked")
        # Run the external script
        self.run_external_script("C:/Plot/bb_bit_size.py")

    def create_working_step(self):
        # Method to handle the Create Working Step button click
        print("Create Working Step button clicked")
        # Run the associated external script
        self.run_external_script("C:/Plot/bb_bit_size.py")

    def run_external_script(self, script_path):
        # Method to run an external script
        if self.process is not None and self.process.state() == QProcess.Running:
            print("A process is already running. Please wait for it to finish before starting a new one.")
            return

        self.process = QProcess(self)

        # Connect signals for debugging
        self.process.started.connect(lambda: print(f"Process started: {script_path}"))
        self.process.finished.connect(self.on_process_finished)
        self.process.readyReadStandardOutput.connect(self.on_ready_read_standard_output)
        self.process.readyReadStandardError.connect(self.on_ready_read_standard_error)

        # Start the script using the Python interpreter
        self.process.start("python", [script_path])

    def on_process_finished(self, exitCode, exitStatus):
        print(f"Process finished with exit code {exitCode}, exit status {exitStatus}")
        self.process = None  # Reset the process variable

    def on_ready_read_standard_output(self):
        if self.process:
            sys.stdout.write(str(self.process.readAllStandardOutput(), 'utf-8'))

    def on_ready_read_standard_error(self):
        if self.process:
            sys.stderr.write(str(self.process.readAllStandardError(), 'utf-8'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToolingControlForm()
    ex.show()
    sys.exit(app.exec_())
