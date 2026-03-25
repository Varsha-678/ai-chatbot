def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great!"
    elif "bye" in user_input:
        return "Goodbye! 👋"
    else:
        return "I didn't understand that."
