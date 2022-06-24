import json

def choice(json_file_pass, key):
    json_data = json.load(open(json_file_pass))
    check = json_data[key]["check"]
    if check == "True":
        check = True
    elif check == "False":
        check = False
    else:
        print("An error occurred: json file is not correct")
    json_data = json_data[key]["choices"]
    number_of_choices = json_data.values()
    for i in range(number_of_choices):
        outline = str(i) + json_data[i]
        print(outline)
    return [number_of_choices, check]

