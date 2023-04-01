import function
import PySimpleGUI as sg

label = sg.Text("Type in a todo: ")
input_box = sg.InputText(tooltip="Enter todo:")
add_button = sg.Button("add")


window = sg.Window("Pro's Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
