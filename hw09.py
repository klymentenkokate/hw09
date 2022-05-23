dict = {
    "Kate": '380635196798',
    "Yevhen": '0635196799',
    "Olesia": '380635196796',
    "Eduard": '+380635196798'

}

def input_error(func):
    #print("Decorator called")
    def inner_function(*args, **kwargs):
        #print("Calling the function")
        try:
            return func(*args, **kwargs)
            
        except KeyError:
            print(f'Please enter a name')
        except ValueError:
            print(f'Please enter a phone number')
        except IndexError:
            print(f"Please enter a name and a phone number divided by space")
            
    return inner_function

@input_error
def hello_func():
    return "Hello, how can I assist you?"

@input_error
def add_func():
    #print("Executing the function")
    add_input = input("Please enter name and phone number: ")
    list = add_input.split()
    dict[list[0]]=list[1]
    return list[0], list[1]
    
@input_error
def change_func():
    add_input = input("Please enter name and phone number: ")
    list = add_input.split()
    dict[list[0]]=list[1]
    return list[0], list[1]
 
@input_error
def phone_func():
    add_input = input("Please enter phone number: ")
    for n, ph in dict.items():
        if add_input == ph:
            return n


@input_error
def showall_func():
    #for name,phone in dict.items():
        #print(name,' ',phone)
    return dict
    

#def bye_func():
    #return "Good bye"

COMMANDS = {
    hello_func: "hello",
    add_func: "add",
    change_func: "change",
    phone_func: "phone",
    showall_func: "show all"
    
}

def main():
    while True:
        user_input = input(">>>")
        for k,v in COMMANDS.items():
            if v == user_input.lower():
                print(k())
        if user_input == "bye" or user_input == "exit" or user_input == "close":
            print("Good bye")
            break
        if user_input == '.':
            break
            

if __name__ == "__main__":
    main()
    
    
        