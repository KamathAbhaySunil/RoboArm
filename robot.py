import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

class RoboticArm:
    def __init__(self, joint_angles=(0, 0, 0), arm_length=(1, 1, 1)):
        self.joint_angles = np.array(joint_angles, dtype=float)
        self.arm_length = np.array(arm_length, dtype=float)
        self.update_arm_positions()

    def move_joint(self, joint_index, angle):
        self.joint_angles[joint_index] += angle
        self.update_arm_positions()

    def update_arm_positions(self):
        self.arm_positions = np.zeros((4, 3))
        for i in range(1, 4):
            transformation_matrix = self.calculate_transformation_matrix(i)
            self.arm_positions[i, :] = np.dot(transformation_matrix, np.array([0, 0, 1, 1]))[:3]

    def calculate_transformation_matrix(self, joint_index):
        transformation_matrix = np.eye(4)
        for i in range(joint_index):
            if i == 1:  # Rotate joint 2 on the ZX plane
                rotation_matrix = self.rotation_matrix(self.joint_angles[i], 'z')
            else:
                rotation_matrix = self.rotation_matrix(self.joint_angles[i], 'y')
            translation_matrix = self.translation_matrix(self.arm_length[i], 'x')
            transformation_matrix = np.dot(transformation_matrix, np.dot(rotation_matrix, translation_matrix))
        return transformation_matrix

    def rotation_matrix(self, angle, axis):
        c = np.cos(np.radians(angle))
        s = np.sin(np.radians(angle))
        if axis == 'x':
            return np.array([[1, 0, 0, 0],
                             [0, c, -s, 0],
                             [0, s, c, 0],
                             [0, 0, 0, 1]])
        elif axis == 'y':
            return np.array([[c, 0, s, 0],
                             [0, 1, 0, 0],
                             [-s, 0, c, 0],
                             [0, 0, 0, 1]])
        elif axis == 'z':
            return np.array([[c, -s, 0, 0],
                             [s, c, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])

    def translation_matrix(self, distance, axis):
        if axis == 'x':
            return np.array([[1, 0, 0, distance],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        elif axis == 'y':
            return np.array([[1, 0, 0, 0],
                             [0, 1, 0, distance],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        elif axis == 'z':
            return np.array([[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, distance],
                             [0, 0, 0, 1]])

class RoboticArmControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Robotic Arm Control")

        self.robotic_arm = RoboticArm()

        # Define colors for each joint
        self.joint_colors = ['red', 'green', 'blue']

        self.create_widgets()

    def create_widgets(self):
        # Set up the 3D plot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create control buttons
        self.create_joint_buttons()

    def create_joint_buttons(self):
        for i in range(3):
            left_button = tk.Button(self.master, text=f"Rotate Left", command=lambda idx=i: self.rotate_joint(idx, -5),
                                    width=15, height=2, bg=self.joint_colors[i], fg='white')
            left_button.pack(side=tk.LEFT, padx=10, pady=10)

            right_button = tk.Button(self.master, text=f"Rotate Right", command=lambda idx=i: self.rotate_joint(idx, 5),
                                     width=15, height=2, bg=self.joint_colors[i], fg='white')
            right_button.pack(side=tk.LEFT, padx=10, pady=10)

    def rotate_joint(self, joint_index, angle):
        self.robotic_arm.move_joint(joint_index, angle)
        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        for i in range(1, 4):
            self.ax.plot3D([self.robotic_arm.arm_positions[i-1, 0], self.robotic_arm.arm_positions[i, 0]],
                           [self.robotic_arm.arm_positions[i-1, 1], self.robotic_arm.arm_positions[i, 1]],
                           [self.robotic_arm.arm_positions[i-1, 2], self.robotic_arm.arm_positions[i, 2]],
                           marker='o', linestyle='-', color=self.joint_colors[i-1], markersize=8)

        self.ax.set_xlim(-3, 3)
        self.ax.set_ylim(-3, 3)
        self.ax.set_zlim(0, 3)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoboticArmControlApp(root)
    root.mainloop()
