import PySimpleGUI as sg


sg.theme("DarkGrey9")
layout = [
    [sg.Text("Conquer", font=("Helvetica", 40))],
    [sg.InputText("", key="-TASK-", size=(35, 3)),sg.Button("Add", size=(30, 1),enable_events=True)],
    [sg.Listbox(values=[], size=(69, 7), key="-TASKS-")],
    [sg.Button("Exit", size=(30, 1)), sg.Button("Delete", size=(30, 1))]
]

window = sg.Window("To-Do List App", layout, keep_on_top=False,
                    auto_size_buttons=True,
                    resizable=True,
                    grab_anywhere=True,
                    no_titlebar=True,
                    alpha_channel=0.75,
                    use_default_focus=True,
                    return_keyboard_events=True,
                    finalize=True)

tasks = []

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Add" and values["-TASK-"]:
        task = values["-TASK-"]
        tasks.append(task)
        window["-TASKS-"].update(values=tasks)
        window["-TASK-"].update("")

    if event == "Delete" and values["-TASKS-"]:
        selected_task = values["-TASKS-"][0]
        tasks.remove(selected_task)
        window["-TASKS-"].update(values=tasks)

window.close()
