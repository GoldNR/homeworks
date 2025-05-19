def session_counter():
    counter = 0
    for i in range(5):
        counter += 1
        print(f"Session visits: {counter}")

def kiosk_usage():
    if not hasattr(kiosk_usage, "total_users"):
        kiosk_usage.total_users = 0

    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

for customer in range(1,4):
    print(f"\n--- Customer Session {customer} ---")
    session_counter()
    kiosk_usage()
