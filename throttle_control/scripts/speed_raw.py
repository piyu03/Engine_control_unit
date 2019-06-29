#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64


from Tkinter import*
vehicle_speed = 200
speed = 0.0
def create_widgets_in_last_frame():
    pass
    # imgPath = "engine1.gif"
    # photo = PhotoImage(file = imgPath)
    # label = Label(first_frame,image = photo)
    # label.image = photo # keep a reference!
    # label.place(x=175,y=150)

def create_widgets_in_first_frame():

    label=Label(first_frame,text="Mini Project ",bg="antique white",foreground="sienna",anchor=NE,font=("SHOWCARD GOTHIC",50),fg="black",bd=5,height=1,takefocus=1,state=NORMAL,relief=FLAT,highlightthickness=1)
    label.place(x=150,y=60)

    button = Button(first_frame, text="NEXT",command = call_second_frame_on_top)
    button.pack()
    button.place(x=630,y=420)             #x=350,y=210
    button.config(bg="azure",borderwidth=5,height=1,width=4,font=("Arial Black",10))

def create_widgets_in_second_frame():
    b = Label(second_frame, text="ENGINE UNIT",font=("Viner Hand ITC",32),highlightthickness=12,foreground="black")       #borderwidth=2,relief=RIDGE,)
    b.config(background="antique white")          #borderwidth=2,relief=RIDGE,
    b.place(x=100,y=50)

    var = StringVar()
    var.set("ENGINE CONTROL") # initial value
    option = OptionMenu(second_frame, var, "THROTTLE CONTROL","IGNITION CONTROL")
    option.place (x=300,y=160)                         #x=300,y=150
    option.config(bg="tan",borderwidth=5,cursor="hand2",height=2,width=20,fg="black",font=("Arial Black",18))
    z=option.nametowidget(option.menuname)              #to change the widget config
    z.config(font=("Arial Black",14),bg="linen")


    def ok():
        #print ("value is", var.get())
        root.quit()

    """button1 = Button(second_frame, text="OK", command=ok)
    button1.pack()
    button1.place(x=550,y=260)             #x=350,y=210
    button1.config(bg="azure",borderwidth=5,height=2,width=6,font=("Arial Black",14))"""

    button2 = Button(second_frame, text="BACK", command = call_first_frame_on_top)
    button2.pack()
    button2.place(x=100,y=420)             #x=350,y=210
    button2.config(bg="azure",borderwidth=5,height=1,width=4,font=("Arial Black",10))

    button3 = Button(second_frame, text="NEXT",command = call_third_frame_on_top)
    button3.pack()
    button3.place(x=630,y=420)             #x=350,y=210
    button3.config(bg="azure",borderwidth=5,height=1,width=4,font=("Arial Black",10))

def create_widgets_in_third_frame():
    p= Label(third_frame, text="THROTTLE CONTROL",font=("Bauhaus 93",32),highlightthickness=12,foreground="black")
    p.config(background="antique white")          #borderwidth=2,relief=RIDGE,
    p.place(x=180,y=20)

    b = Label(third_frame, text="Enter the speed (in RPM)",font=("Rockwell Extra Bold",16),highlightthickness=12)
    b.config(background="antique white")          #borderwidth=2,relief=RIDGE,
    b.place(x=50,y=120)

    e = Entry(third_frame,textvariable=vehicle_speed)
    e.pack()
    e.place(x=180,y=190)
    e.config(width=10)
    e.focus_set()               #to blink cursor at that point

    def callback():
        print ("RPM=",e.get())
        # pub.publish(e.get())

    def setRPM():
        global pub, speed
        speed = float(e.get())
        print ("RPM=",speed)
        pub.publish(speed)

    b = Button(third_frame, text="ENTER", width=10, command=setRPM)
    b.pack()
    b.config(width=10,font=("Rockwell Extra Bold",10),bg="azure")
    b.place(x=300,y=190)

    button4 = Button(third_frame, text="BACK", command = call_second_frame_on_top)
    button4.pack()
    button4.place(x=100,y=420)             #x=350,y=210
    button4.config(bg="azure",borderwidth=5,height=1,width=4,font=("Arial Black",10))

    """button5 = Button(third_frame, text="NEXT",command = call_third_frame_on_top)
    button5.pack()
    button5.place(x=630,y=420)             #x=350,y=210
    button5.config(bg="azure",borderwidth=5,height=1,width=4,font=("Arial Black",10))"""

def call_last_frame_on_top():
    # This function can be called from the first windows.
    # Hide the first windows and show the second window.
    first_frame.grid_forget()
    last_frame.grid(column=0, row=0, padx=20, pady=5)

def call_first_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    #last_frame.grid_forget()
    second_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5)

def call_second_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    first_frame.grid_forget()
    third_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5)

def call_third_frame_on_top():
    # This function can only be capublled from the second window.
    # Hide the second window and show the third window.
    second_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=20, pady=5)

    def quit_program():
        root_window.destroy()



if __name__ == '__main__':
    rospy.init_node('speed')
    pub = rospy.Publisher('set_speed', Float64, queue_size=10)
    rate = rospy.Rate(60)

    root_window =Tk()
    root_window.title("MINI PROJECT GUI")
    root_window.configure(background="antique white")
    root_window.geometry("750x500")
    # Define window size
    window_width = 700
    window_heigth = 500

    # Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions.
    last_frame=Frame(root_window, width=window_width, height=window_heigth,background="antique white")
    last_frame['borderwidth'] = 2
    last_frame.grid(column=0, row=0, padx=20, pady=5)

    first_frame=Frame(root_window, width=window_width, height=window_heigth,background="antique white")
    first_frame['borderwidth'] = 2
    first_frame['relief'] = 'raised'
    first_frame.grid(column=0, row=0, padx=20, pady=5)

    second_frame=Frame(root_window, width=window_width, height=window_heigth,background="antique white")
    second_frame['borderwidth'] = 2
    second_frame.grid(column=0, row=0, padx=20, pady=5)

    third_frame=Frame(root_window, width=window_width, height=window_heigth,background="antique white")
    third_frame['borderwidth'] = 2
    third_frame['relief'] = 'raised'
    third_frame.grid(column=0, row=0, padx=20, pady=5)


    # Create all widgets to all frames
    create_widgets_in_third_frame()
    create_widgets_in_second_frame()
    create_widgets_in_first_frame()
    create_widgets_in_last_frame()

    # Hide all frames in reverse order, but leave first frame visible (unhidden).
    third_frame.grid_forget()
    second_frame.grid_forget()
    #last_frame.grid_forget()

    # Start tkinter event - loop
    root_window.mainloop()
    # vehicle_speed = input("Enter speed of the vehicle:")


    while not rospy.is_shutdown():
        rate.sleep()
        # pub.publish(vehicle_speed)
