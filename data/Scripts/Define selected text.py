word = system.exec_command("echo $(xsel)", True)
keyboard.send_keys("<tab>")
time.sleep(0.1)
    
retCode, word = dialog.input_dialog("Fetch data?", word, word)
if retCode == 0:
    ipa = system.exec_command("fetch-ipa '%s'" % word, True)
    retCode, ipa = dialog.input_dialog("Paste IPA?", ipa, ipa)
    if retCode == 0:
        system.exec_command("echo '%s' | xclip -sel clip" % ipa, False)
        time.sleep(0.5)
        keyboard.send_keys("<ctrl>+V")
        time.sleep(0.1)
        
        keyboard.send_keys("<tab>")
        time.sleep(0.1)
        
        mp3 = system.exec_command("fetch-mp3-url '%s'" % word, True)
        retCode, mp3 = dialog.input_dialog("Paste Sound?", mp3, mp3)
        if retCode == 0:            
            system.exec_command("echo '%s' | xclip -sel clip" % mp3, False)
            time.sleep(0.5)
            keyboard.send_keys("<ctrl>+V")
            time.sleep(0.1)
      
            url = system.exec_command("echo gnome-open http://dictionary.reference.com/browse/" + word, True)      
            retCode, url = dialog.input_dialog("Open in Browser?", url, url)
            if retCode == 0:
                system.exec_command(url, False)
