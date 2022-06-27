import json

def JsonOpen(json_file_pass, key):
    json_data = json.load(open(json_file_pass, "r", encoding="utf-8_sig"))
    json_data = json_data[key]
    return json_data

def choice(json_data):
    check = json_data["check"]
    if check == "True":
        check = True
    elif check == "False":
        check = False
    else:
        print("An error occurred: json file is not correct!!")
    number_of_choices = len(json_data["choices"])
    for i in range(number_of_choices):
        outline = str(json_data["choices"][i]["id"]) + ": " + json_data["choices"][i]["name"]
        print(outline)
    return [number_of_choices, check]

def InputProcesser(number_of_choices, check = False):
    range_flag = False
    check_flag = False
    inline = 0
    while True:
        print(">>")
        inline = int(input())
        if inline <= number_of_choices:
            range_flag = True
        else:
            print("この値は対応していません")
            continue

        if check == False:
            check_flag = True
        else:
            print(str(inline)+"本当によろしいですか?(y/n)")
            ans = input()
            if ans in ["y", "Y", "yes", "YES"]:
                check_flag = True
            elif ans in ["n", "N", "no", "NO"]:
                continue
            else:
                print("この値は対応していません")
                continue
        if range_flag and check_flag:
            break
    return inline
