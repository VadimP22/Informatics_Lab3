class Node:
    def __init__(self, name):
        self.name = name
        self.child = []

        self.have_child_node = False
        self.content_something = False

    def add_child_node(self, node):
        self.have_child_node = True
        self.child.append(node)

    def set_content(self, content):
        self.content_something = True
        self.content = content


def colon_detected(char_number, text):
    print(text[char_number])


    counter = char_number
    colon = char_number

    number_of_spaces = 0
    is_first_space = True
    first_character_number = 0

    while counter >= 0:
        counter = counter - 1

        if text[counter] == '\n':
            break


        if text[counter] == " ":
            number_of_spaces = number_of_spaces + 1

            if is_first_space:
                is_first_space = False
                first_character_number = counter + 1


    print(number_of_spaces)
    print(text[first_character_number : colon])
    # {number of spaces, string name, }
        
        
    


def convert_yaml_to_json(yaml):
    
    root = Node("root")

    char_number = 0
    for c in yaml:
        
        if c == ":":
            colon_detected(char_number, yaml)


        char_number = char_number + 1



def main():

    yaml_text = ""

    with open("./yaml.yaml", "r") as file:
        yaml_text = file.read()


    json_text = convert_yaml_to_json(yaml_text)

    # with open("./json.json", "w"):
    #     file.write(json_text)

    print(yaml_text)





if __name__ == "__main__":
    main()
    print("READY")