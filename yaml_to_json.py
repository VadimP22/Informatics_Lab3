class YamlLabel():
    def __init__(self, name, number_of_spaces, content = False):
        self.name = name
        self.number_of_spaces = number_of_spaces
        self.content = content


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


def colon_detected(char_number, text) -> YamlLabel:
    # print(text[char_number])


    counter = char_number
    colon = char_number

    number_of_spaces = 0
    is_first_space = True
    first_character_number = 0


    #обработка символов до двоеточия
    while counter >= 0:
        counter = counter - 1

        if text[counter] == '\n':
            break


        if text[counter] == " ":
            number_of_spaces = number_of_spaces + 1

            if is_first_space:
                is_first_space = False
                first_character_number = counter + 1


    #обработка символов после двоеточия
    counter = char_number
    

    
    while text[counter] != "\n":
        counter = counter + 1
        

    content = text[colon + 1 : counter]
        


    # print(number_of_spaces)
    # print(text[first_character_number : colon])
    if content != "":
        return YamlLabel(text[first_character_number : colon], number_of_spaces, content)
    else:
        return YamlLabel(text[first_character_number : colon], number_of_spaces)
        

def get_yaml_labels(yaml):
    
    yaml_labels = []


    char_number = 0
    for c in yaml:
        
        if c == ":":
            yaml_labels.append(colon_detected(char_number, yaml))


        char_number = char_number + 1

    # print("labels list is done")
    
    return yaml_labels


# def make_node_tree(label_list):
#     root = Node("root")

#     upper_level = root
#     upper_upper_level = root

#     for label in  label_list:
#         pass


#     return root


def make_json_text(label_list: YamlLabel):
    
    json_text = "azaza \n"

    for i in range(len(label_list)):
        pass

    return json_text


def main():

    yaml_text = ""

    with open("./yaml.yaml", "r") as file:
        yaml_text = file.read()

    yaml_text = yaml_text + "\n"

    yaml_labels = get_yaml_labels(yaml_text)
    print("label list is done")
    json_text = make_json_text(yaml_labels)
    print("json text is ready")


    with open("./json.json", "w") as file:
         file.write(json_text)






if __name__ == "__main__":
    main()
    print("READY")