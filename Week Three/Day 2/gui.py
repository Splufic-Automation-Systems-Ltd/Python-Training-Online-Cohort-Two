
# import the module
import tkinter

# instantiate the window class
root = tkinter.Tk()
# title it 
root.title('My GUI')
# add size
root.maxsize(300, 400)
# add colour
# root.colo
# add a label
value = tkinter.StringVar()
value.set('This is a simple label')
my_label = tkinter.Label(root,\
 bg='red', fg='green', textvariable=value)
my_label.pack()

count = 0
def run():
	global count
	count += 1
	value.set(count)

my_button = tkinter.Button(root, text='Click Me', \
	command = run)
my_button.pack()

# start the app
root.mainloop()