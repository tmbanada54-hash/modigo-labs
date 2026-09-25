def find_phone_number(contacts, name):
    contact_book = dict(contacts)
    return contact_book.get(name, "Not found")
    # TODO: build a dict from `contacts` (list of (name, phone) tuples),
    # then return the phone number for `name`, or "Not found"
    pass