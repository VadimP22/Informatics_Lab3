import time
import yaml
import json

class YamlLabel():
    def __init__(self, name, number_of_spaces, content = False):
        self.name = name
        self.number_of_spaces = number_of_spaces
        self.content = content


class Node:
    def __init__(self, name):
        self.name = name
        self.child = []
        self.parent = 0

        self.have_child_node = False
        self.content_something = False
        self.have_parent = False
        self.level = 0
        self.last = False
        # self.rec = False

    def add_child_node(self, node):
        self.have_child_node = True
        self.child.append(node)
        for i in range(len(self.child)):
            self.child[i].parent = self
            self.child[i].last = False
        self.child[len(self.child) - 1].last = True

    def set_content(self, content):
        self.content_something = True
        self.content = content

    def set_level(self, level):
        self.level = level


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
        

def recursive_text_constructor(node: Node, text):
    
    if node.level != 8:
        text = text + node.level*"  " + '"' + node.name + '": {\n'
    else:
        text = text + node.level*"  " + '"' + node.name + '":' + node.content
        if node.last == False:
            text = text + "," 
        text = text + "\n"

    for ch in node.child:
        text = recursive_text_constructor(ch, text)

    if node.level != 8:
        text = text + node.level*"  " + "}"
        if node.last == False:
            text = text + ","

        text = text + "\n"



    return text



def tree_to_json(tree):
    json_text = ""
    return recursive_text_constructor(tree, json_text)


def get_yaml_labels(yaml):
    
    yaml_labels = []


    char_number = 0
    for c in yaml:
        
        if c == ":":
            yaml_labels.append(colon_detected(char_number, yaml))


        char_number = char_number + 1

    # print("labels list is done")
    
    return yaml_labels


def make_node_tree(labels):
    root = Node("root")

    zero_level = root
    level_2 = root
    level_4 = root

    for i in range(len(labels)):

        if labels[i].number_of_spaces == 0:
            node = Node(labels[i].name)
            node.set_level(2)
            root.add_child_node(node)
            zero_level = node

        if labels[i].number_of_spaces == 2:
            node = Node(labels[i].name)
            node.set_level(4)
            zero_level.add_child_node(node)
            level_2 = node

        if labels[i].number_of_spaces == 4:
            node = Node(labels[i].name)
            node.set_level(6)
            level_2.add_child_node(node)
            level_4 = node

        if labels[i].number_of_spaces == 6:
            node = Node(labels[i].name)
            node.set_level(8)
            node.set_content(labels[i].content)
            level_4.add_child_node(node)

    return root


def parse_and_convert(path_to_yaml, path_to_json):

    yaml_text = ""

    with open(path_to_yaml, "r") as file:
        yaml_text = file.read()

    yaml_text = yaml_text + "\n"

    yaml_labels = get_yaml_labels(yaml_text)
    # print("label list is done")
    root = make_node_tree(yaml_labels)
    # print("tree is ready")
    json_text = "{\n" + tree_to_json(root.child[0]) + "}"




    with open(path_to_json, "w") as file:
         file.write(json_text)


def external_library_parser(path_to_yaml, path_to_json):
    with open(path_to_yaml, 'r') as yaml_in, open(path_to_json, "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
        json.dump(yaml_object, json_out)


def main():
    start_time = time.time()
    for i in range(10):
        parse_and_convert("./yaml.yaml", "./json.json")
    delta_time1 = time.time() - start_time
    print("My script: (s) " + str(delta_time1))

    start_time = time.time()
    for i in range(10):
        external_library_parser("./yaml.yaml", "./json.json")
    delta_time2 = time.time() - start_time
    print("External library: (s) " + str(delta_time2))
    print("my time - lib time:" + str(delta_time1 - delta_time2)) 


if __name__ == "__main__":
    main()
    print("===READY===")