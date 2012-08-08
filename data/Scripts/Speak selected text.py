word = clipboard.get_selection()
command = "dict-mp3 '" + word + "'"
try:
    system.exec_command(command, False)
except subprocess.CalledProcessError, e:
    dialog.info_dialog(title = "Error", message = str(e.output))

