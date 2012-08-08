text = clipboard.get_selection()
text = clipboard.get_selection()
system.exec_command("gnome-open http://dictionary.reference.com/browse/" + text, False)
command = "dict-mp3 '" + text + "'"
system.exec_command(command, False)
