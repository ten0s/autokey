text = clipboard.get_selection()
system.exec_command("espeak '" + text + "'",False)

