phone_book = {"Kate": '123',
    "Yevhen": '0635196799',
    "Olesia": '380635196796',
    "Eduard": '+380635196798'}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Sorry, try later.'
        except KeyError:
            return 'Sorry, try the correct key'
        except ValueError:
            return 'Sorry, no value found'
    return wrapper

def exit(*args):
    return "Good bye!"

def hello_func(*args):
    return "Hello! How can I help you?"

@input_error
def add(*args):
    name = args[0]
    phone = int(args[1])
    for n, ph in phone_book.items():
        if n == name:
            return f'Contact {name} already exists'
        else:
            phone_book[name]= phone
            return f'Contact {name} added successfully'

@input_error
def change_phone(*args):
    name = args[0]
    phone = int(args[1])
    for n, ph in phone_book.items():
        if n == name:
            phone_book[name]= phone
            return f'Contact {name} update successful'
        else:
            return "Name not found in phone book"
    
def show_all(*args):
    lst = ['{:^10}:{:>10}'.format(k,v) for k,v in phone_book.items()]
    return "\n".join(lst)
    
@input_error
def phone(*args):
    phone = args[0]
    for n1, ph1 in phone_book.items():
        if str(ph1) == phone:
            return f"This is {n1}'s phone"
        else:
            return "Contact not found"
        


COMMANDS = {hello_func:["hello"], exit:["exit", ".", "bye"], add:["add", "добавь", "додай"], change_phone:["change"], phone:["phone"], show_all:["show all", "show"]}


def parse_command(user_input:str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")


def main():
    while True:
        user_input = input(">>>")
        result, data = parse_command(user_input)
        print(result(*data))
        if result is exit:
            break


if __name__ == "__main__":
    main()