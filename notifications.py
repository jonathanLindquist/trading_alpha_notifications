# from functools import partial
from mac_notifications import client
from random import choice
import time

quotes = [
    "It's okay to be wrong, it's a problem to stay wrong",
    "It's not about being right, it's about not remaining wrong",
    "Slow down. Is your intuition driving your choices, and is it correct?",
    "You act too quickly when trying to grow capital, and too slowly when trying to protect it"
]

DEFAULT_DELAY = 14400

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
            action_button_str="Snooze for 1 day",
            action_callback=lambda: update_delay(timer=app_timer, new_delay=86400),
            # reply_button_str="Snooze for 4 Hours",
            # reply_callback=update_delay(temp_epoch, 10),
            snooze_button_str="Dismiss Message",
            # reply_button_str="Delay Messages"
        )

        time.sleep(100) # delay enough time to handle snooze button if user presses it

    # Debug loop
    # while client.get_notification_manager().get_active_running_notifications() > 0:
    #     time.sleep(1)
    #     # print(f"Active number of notifications: {client.get_notification_manager().get_active_running_notifications()}")
    # client.stop_listening_for_callbacks()
