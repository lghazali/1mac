import time
import webbrowser

no_of_breaks = 3
time_between_breaks = 3
video_length = 225

for i in range(no_of_breaks):
    print "Time for work, till next break! "
    time.sleep(time_between_breaks)
    print "Time for a break! "
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=xlauT5TvczE")
    time.sleep(video_length)
