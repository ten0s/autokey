# Terminal -> Keyboard Shortcuts
# Edit -> Copy  Disabled
# Edit -> Paste Ctrl+V 
try:
    text = clipboard.get_selection()
    if len(text.strip()) > 0:
        clipboard.fill_clipboard(text)
        mouse.click_relative_self(0, 0, 1)       
    else:
        raise Exception("")
except:
    keyboard.send_keys("<ctrl>+C")
