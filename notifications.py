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

if __name__ == "__main__":
    notification = client.create_notification(
        title=choice(quotes),
        subtitle="Team Standup",
        icon="/Users/jorrick/zoom.png",
        sound="Frog",
        action_button_str="Join zoom meeting",
        action_callback=lambda: print("Pressed action button"),
    )

    # TODO: remove before making a running daemon
    while client.get_notification_manager().get_active_running_notifications() > 0:
        time.sleep(1)
        print(f"Active number of notifications: {client.get_notification_manager().get_active_running_notifications()}")
    client.stop_listening_for_callbacks()