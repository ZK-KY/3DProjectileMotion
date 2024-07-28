from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create the main window for the GUI (tkinter)
win_input = Tk()

# Create frames
frm_title = Frame(padx=30, pady=10)
frm_v = Frame(padx=30, pady=10)
frm_a = Frame(padx=30, pady=10)
frm_ah = Frame(padx=30, pady=10)
frm_g = Frame(padx=30, pady=10)
frm_btn = Frame(padx=30, pady=10)
frm_d = Frame(padx=30, pady=10)
frm_dc = Frame(padx=30, pady=10)
frm_csa = Frame(padx=30, pady=10)

# Create labels for user input
lbl_title = Label(master=frm_title, font=15, text="Physics Modelling For L6B/Ph. Made by Zain, Mahfuzur and Isaac", pady=5, padx=5)
lbl_v = Label(master=frm_v, font=15, text="Enter the initial velocity (m/s): ")
lbl_a = Label(master=frm_a, font=15, text="Enter the angle of projection vertically (deg): ")
lbl_ah = Label(master=frm_ah, font=15, text="Enter the angle of projection horizontally (deg): ")
lbl_g = Label(master=frm_g, font=15, text="Enter the acceleration due to gravity (m/s^2): ")
lbl_d = Label(master=frm_d, font=15, text="Enter density: (kg/m^3) ")
lbl_dc = Label(master=frm_dc, font=15, text="Enter drag coefficient: (No Units)")
lbl_csa = Label(master=frm_csa, font=15, text="Enter cross sectional area: (m^2) ")

ent_v = Entry(master=frm_v, font=15, borderwidth=2)
ent_a = Entry(master=frm_a, font=15, borderwidth=2)
ent_ah = Entry(master=frm_ah, font=15, borderwidth=2)
ent_g = Entry(master=frm_g, font=15, borderwidth=2)
ent_d = Entry(master=frm_d, font=15, borderwidth=2)
ent_dc = Entry(master=frm_dc, font=15, borderwidth=2)
ent_csa = Entry(master=frm_csa, font=15, borderwidth=2)

btn_calc = Button(font=15, master=frm_btn, text="Calculate Trajectory", pady=5, padx=10)

# Pack the frames
frm_title.pack()
lbl_title.pack()
frm_v.pack()
lbl_v.pack()
ent_v.pack()
frm_a.pack()
lbl_a.pack()
ent_a.pack()
frm_ah.pack()
lbl_ah.pack()
ent_ah.pack()
frm_g.pack()
lbl_g.pack()
ent_g.pack()
frm_d.pack()
lbl_d.pack()
ent_d.pack()
frm_dc.pack()
lbl_dc.pack()
ent_dc.pack()
frm_csa.pack()
lbl_csa.pack()
ent_csa.pack()
frm_btn.pack()
btn_calc.pack()

# Function to calculate and plot the trajectory
def traj_calc():
    vinit = float(ent_v.get())
    angleverticalinit = float(ent_a.get())
    anglehorizontalinit = float(ent_ah.get())
    acceleration = float(ent_g.get())
    density = float(ent_d.get())
    DragCoeff = float(ent_dc.get())
    CrossSecArea = float(ent_csa.get())
    
    angle_rad = np.deg2rad(angleverticalinit)
    angle_horizontal_rad = np.deg2rad(anglehorizontalinit)

    # Initial velocity components
    vx = vinit * np.cos(angle_horizontal_rad) * np.cos(angle_rad)
    vy = vinit * np.sin(angle_horizontal_rad) * np.cos(angle_rad)
    vz = vinit * np.sin(angle_rad)

    # Initial positions
    x = 0
    y = 0
    z = 0

    # Time step and mass (kg)
    dt = 0.1
    mass = 1.0

    # Lists to store trajectory points
    trajectory_points = []

    # Simulate the trajectory
    while z >= 0:
        trajectory_points.append([x, y, z])

        # Calculate air resistance
        v = np.sqrt(vx**2 + vy**2 + vz**2)
        air_resistance = 0.5 * density * v**2 * DragCoeff * CrossSecArea

        # Acceleration components
        ax = (-air_resistance * (vx / v)) / mass
        ay = (-air_resistance * (vy / v)) / mass
        az = (-acceleration - air_resistance * (vz / v)) / mass

        # Update velocity components
        vx += ax * dt
        vy += ay * dt
        vz += az * dt

        # Update position components
        x += vx * dt
        y += vy * dt
        z += vz * dt

    # Plotting the trajectory
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Convert trajectory points to arrays for plotting
    trajectory_array = np.array(trajectory_points)

    # Plot the trajectory
    ax.scatter(trajectory_array[:, 0], trajectory_array[:, 1], trajectory_array[:, 2])

    ax.set_xlim(0, np.max(trajectory_array[:, 0]) + 10)
    ax.set_ylim(0, np.max(trajectory_array[:, 1]) + 10)
    ax.set_zlim(0, np.max(trajectory_array[:, 2]) + 10)

    ax.set_xlabel("X distance (m)")
    ax.set_ylabel("Y distance (m)")
    ax.set_zlabel("Z distance (m)")
    ax.set_title("3D Trajectory")

    plt.show()

# Bind the button click event to the traj_calc function
btn_calc.config(command=traj_calc)

# Start the Tkinter event loop
win_input.mainloop()
