from plyer import notification
import time
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    time.sleep(5)
    notification.notify(title = 'Remainder',
                        message = speaker.speak("Drink water buddy!"),
                        timeout = 5)