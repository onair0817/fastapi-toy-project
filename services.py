def process_message(message):
    item_id = message.get("item_id")
    q = message.get("q")
    # Do something with the message
    print(f"Processing item_id={item_id}, q={q}")
