from src.bot.commands import change_phone_by_name, get_phone_by_name, add_contact, print_commands, add_birthday, \
    show_birthday, birthdays


def handle_close(args, contacts):
    print("Good bye!")
    return True


def handle_hello(args, contacts):
    print("How can I help you?")


def handle_help(args, contacts):
    print_commands()


def handle_add(args, contacts):
    print(add_contact(args, contacts))


def handle_phone(args, contacts):
    print(get_phone_by_name(args, contacts))


def handle_all(args, contacts):
    print(contacts)


def handle_change(args, contacts):
    print(change_phone_by_name(args, contacts))


def handle_invalid_command(args, contacts):
    print("Invalid command.")


def handle_add_birthday(args, contacts):
    print(add_birthday(args, contacts))


def handle_show_birthday(args, contacts):
    print(show_birthday(args, contacts))


def handle_birthdays(args, contacts):
    upcoming_birthdays = birthdays(args, contacts)
    for birthday in upcoming_birthdays:
        print(f"{birthday['name']}'s birthday is on {birthday['congratulation_date']}")


command_handlers = {
    "close": handle_close,
    "exit": handle_close,
    "hello": handle_hello,
    "help": handle_help,
    "add": handle_add,
    "phone": handle_phone,
    "all": handle_all,
    "change": handle_change,
    "add-birthday": handle_add_birthday,
    "show-birthday": handle_show_birthday,
    "birthdays": handle_birthdays
}
