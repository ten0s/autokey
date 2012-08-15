# get selection. xsel works more stable than clipboard.get_selection()
word = system.exec_command("echo $(xsel)", True)
# clear selection
keyboard.send_keys("<right>")
time.sleep(0.2)

# open browser
system.exec_command("gnome-open http://dictionary.reference.com/browse/" + word, False)

# fetch ipa, copy it to clipboard, move to next field, and paste it
ipa = system.exec_command("fetch-ipa '%s'" % word, True)
#dialog.info_dialog("", ipa)
system.exec_command("echo '%s' | xclip -sel clip" % ipa, False)
time.sleep(0.5)
keyboard.send_keys("<tab>")
time.sleep(0.2)
keyboard.send_keys("<ctrl>+V")
time.sleep(0.2)

# fetch mp3 url, copy it to clipboard, move to next field, and paste it
url = system.exec_command("fetch-mp3-url '%s'" % word, True)
#dialog.info_dialog("", url)
system.exec_command("echo '%s' | xclip -sel clip" % url, False)
time.sleep(0.5)
keyboard.send_keys("<tab>")
time.sleep(0.2)
keyboard.send_keys("<ctrl>+V")
time.sleep(0.2)
