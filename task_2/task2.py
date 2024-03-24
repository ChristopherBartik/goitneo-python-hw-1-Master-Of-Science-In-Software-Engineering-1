def add_contact(name, phone, contacts):
    contacts[name.lower()] = phone
    return "Contact added."

def change_contact(name, phone, contacts):
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return "Contact updated."
    return "Contact not found."

def get_phone(name, contacts):
    return contacts.get(name.lower(), "Contact not found.")

def show_all_contacts(contacts):
    return '\n'.join([f"{name.title()}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    command_handlers = {
        "hello": lambda _: "How can I help you?",
        "add": lambda args: add_contact(args[0], args[1], contacts),
        "change": lambda args: change_contact(args[0], args[1], contacts),
        "phone": lambda args: get_phone(args[0], contacts),
        "all": lambda _: show_all_contacts(contacts),
        "close": lambda _: "Goodbye!",
        "exit": lambda _: "Goodbye!"
    }

    while True:
        user_input = input().lower()
        command, *args = user_input.split()
        if command in ["close", "exit"]:
            print(command_handlers[command](args))
            break
        response = command_handlers.get(command, lambda _: "Unknown command.")(args)
        print(response)

if __name__ == "__main__":

    main()