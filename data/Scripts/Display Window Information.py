import time
#time.sleep(2)
mouse.wait_for_click(1)
time.sleep(0.2)
winTitle = window.get_active_title()
winClass = window.get_active_class()
dialog.info_dialog("Window information", 
          "Active window information:\\nTitle: '%s'\\nClass: '%s'" % (winTitle, winClass))