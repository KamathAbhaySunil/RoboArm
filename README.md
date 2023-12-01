# RoboArm
code to simulate a robotic arm with three degrees of freedom using numpy tkinter and matplotlib

### `RoboticArm` Class:

The `RoboticArm` class represents a simple robotic arm with three joints. Here's a breakdown of its components:

- **Attributes:**
  - `joint_angles`: A NumPy array representing the current angles of the three joints.
  - `arm_length`: A NumPy array representing the lengths of the arm segments.

- **Methods:**
  - `move_joint(joint_index, angle)`: Updates the angle of a specific joint.
  - `update_arm_positions()`: Calculates the 3D positions of the arm segments based on the current joint angles.
  - `calculate_transformation_matrix(joint_index)`: Calculates the transformation matrix for a given joint index.
  - `rotation_matrix(angle, axis)`: Generates a 3D rotation matrix for a specified angle and axis (x, y, or z).
  - `translation_matrix(distance, axis)`: Generates a 3D translation matrix for a specified distance along an axis.

### `RoboticArmControlApp` Class:

The `RoboticArmControlApp` class represents the GUI application for controlling the robotic arm.

- **Attributes:**
  - `joint_colors`: A list of colors associated with each joint.

- **Methods:**
  - `create_widgets()`: Sets up the 3D plot and creates control buttons.
  - `create_joint_buttons()`: Creates buttons for controlling each joint.
  - `rotate_joint(joint_index, angle)`: Callback function to rotate a specific joint.
  - `update_plot()`: Updates the 3D plot with the current arm positions.

### GUI Initialization:

- **Tkinter Window:**
  - `root = tk.Tk()`: Creates the main Tkinter window.

- **Arm and GUI Initialization:**
  - `app = RoboticArmControlApp(root)`: Initializes the robotic arm control application.

- **Main Loop:**
  - `root.mainloop()`: Enters the Tkinter main event loop, allowing the GUI to respond to user inputs.

### 3D Plotting:

- **Matplotlib 3D Plot:**
  - `self.fig = plt.figure()`: Creates a Matplotlib figure.
  - `self.ax = self.fig.add_subplot(111, projection='3d')`: Adds a 3D subplot to the figure.
  - `self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)`: Creates a Tkinter canvas for embedding the Matplotlib plot.

### Arm Movement and Update:

- **Arm Movement:**
  - `self.robotic_arm.move_joint(joint_index, angle)`: Updates the joint angle to simulate arm movement.

- **Plot Update:**
  - `self.update_plot()`: Clears the previous plot and re-plots the arm in its updated configuration.

### NumPy Arrays for Arm Movement:

- The `RoboticArm` class utilizes NumPy arrays to represent joint angles (`joint_angles`) and arm lengths (`arm_length`).
- These arrays allow for efficient manipulation of joint angles and arm lengths, making it easy to calculate the 3D positions of the arm segments.

### Transformation Matrices:

- The `calculate_transformation_matrix` method uses rotation and translation matrices to compute the transformation for each joint.
- Rotation matrices (`rotation_matrix`) are used to rotate joints around the x, y, or z axis.
- Translation matrices (`translation_matrix`) are used to move the arm segments along the x, y, or z axis.

### GUI Buttons:

- Each joint has "Rotate Left" and "Rotate Right" buttons.
- Button presses trigger the `rotate_joint` method, which updates the joint angle and calls `update_plot` to refresh the 3D plot.

### Color-Coding:

- Each joint is assigned a color (red, green, or blue) for better visualization.
- Buttons associated with each joint have the same color to indicate the correspondence.

### Plot Limitations:

- The 3D plot limits are set to (-3, 3) on the x and y axes and (0, 3) on the z axis to keep the arm within a visible range.

This program provides a simple simulation of a robotic arm controlled through a Tkinter GUI, allowing users to manipulate joint angles and visualize the arm's movements in 3D space. The use of NumPy facilitates efficient computation of arm positions based on joint angles and lengths.
