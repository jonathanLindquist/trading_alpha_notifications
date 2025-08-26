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

# 1 hour default
delay_epoch = [5]

def update_delay(temp_epoch: list, new_delay: int):
    print(f'inside `update_delay`, temp_epoch: {temp_epoch}, delay_epoch: {delay_epoch}')
    temp_epoch[0] = new_delay

if __name__ == "__main__":
    while True:
        temp_epoch = delay_epoch.copy()
        print(f"beginning of while loop, temp_epoch: {temp_epoch}")
        notification = client.create_notification(
            title=choice(quotes),
            # subtitle="Team Standup",
            # icon="/Users/jorrick/zoom.png",
            sound="Frog",
            action_button_str="Snooze for 4 Hours",
            action_callback=update_delay(temp_epoch, 10),
            # reply_button_str="Snooze for 4 Hours",
            # reply_callback=update_delay(temp_epoch, 10),
            # snooze_button_str="Dismiss Message",
            # reply_button_str="Delay Messages"
        )

        print(f'right before time.sleep, temp_epoch: {temp_epoch}')
        time.sleep(temp_epoch[0])
        print(f'right after time.sleep, temp_epoch: {temp_epoch}')

    # Debug loop
    # while client.get_notification_manager().get_active_running_notifications() > 0:
    #     time.sleep(1)
    #     # print(f"Active number of notifications: {client.get_notification_manager().get_active_running_notifications()}")
    # client.stop_listening_for_callbacks()