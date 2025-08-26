# from functools import partial
from mac_notifications import client
from random import choice
import time

quotes = [
    "Don't blow up",
    "Be Patient",
    "Stick to the plan",
    "Thaks God! IT's Monday!"
]

DEFAULT_DELAY = 3600

class Timer:
    def __init__(self):
        self.delay_epoch = DEFAULT_DELAY

def update_delay(timer: Timer, new_delay: int):
    timer.delay_epoch = new_delay

if __name__ == "__main__":

    app_timer = Timer()

    while True:
        time.sleep(app_timer.delay_epoch) # delay for timer

        # reset to default after 1 cycle
        if app_timer.delay_epoch != DEFAULT_DELAY:
            app_timer.delay_epoch = DEFAULT_DELAY

        notification = client.create_notification(
            title=choice(quotes),
            # subtitle="Team Standup",
            # icon="/Users/jorrick/zoom.png",
            sound="Frog",
            action_button_str="Snooze",
            action_callback=lambda: update_delay(timer=app_timer, new_delay=14400),
            # reply_button_str="Snooze for 4 Hours",
            # reply_callback=update_delay(temp_epoch, 10),
            # snooze_button_str="Dismiss Message",
            # reply_button_str="Delay Messages"
        )

        time.sleep(20) # delay enough time to handle snooze button if user presses it

    # Debug loop
    # while client.get_notification_manager().get_active_running_notifications() > 0:
    #     time.sleep(1)
    #     # print(f"Active number of notifications: {client.get_notification_manager().get_active_running_notifications()}")
    # client.stop_listening_for_callbacks()