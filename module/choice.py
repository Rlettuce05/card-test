def JsonOpen(json_file_pass, key):
    import json
    json_data = json.load(open(json_file_pass, "r", encoding="utf-8_sig"))
    json_data = json_data[key]
    return json_data

def ChoiceOutput(json_data):
    check = json_data["check"]
    if check == "True":
        check = True
    elif check == "False":
        check = False
    else:
        print("An error occurred: json file is not correct!!")
    choices_id = []
    for i in json_data["choices"]:
        json_data_ = json_data["choices"][i]
        outline = str(json_data_["id"]) + ": " + json_data_["name"]
        choices_id.append(json_data_["id"])
        print(outline)
    return [choices_id, check]

def InputProcesser(choices_id, check = False):
    range_flag = False
    check_flag = False
    inline = 0
    while True:
        print(">>")
        inline = input()
        choices_id = list(map(str, choices_id))
        if inline in choices_id:
            range_flag = True
            inline = int(inline)
        else:
            print("この値は対応していません")
            continue

        if check == False:
            check_flag = True
        else:
            while True:
                print(str(inline)+":"+"本当によろしいですか?(y/n)")
                ans = input()
                if ans in ["y", "Y", "yes", "YES"]:
                    check_flag = True
                    break
                elif ans in ["n", "N", "no", "NO"]:
                    break
                else:
                    print("この値は対応していません")
        if range_flag and check_flag:
            break
    return inline

def CallCondition(json_data, id_):
    condition = ""
    for i in json_data["choices"]:
        json_data_ = json_data["choices"][i]
        if json_data_["id"] == id_:
            condition = json_data_["conditions"]
    return condition

def CheckCondition(status_data, condition_data):
    condition = False
    if condition_data == "":
        condition = True
    else:
        condition_data = condition_data.split(" ")
        status_data = status_data["status"][condition_data[0]]["value"]
        if condition_data[1] == ">=":
            condition = status_data >= int(condition_data[2])
        elif condition_data[1] == "<=":
            condition = status_data <= int(condition_data[2])
        elif condition_data[1] == "==":
            condition = status_data == int(condition_data[2])
        elif condition_data[1] == "!=":
            condition = status_data != int(condition_data[2])
    return condition
