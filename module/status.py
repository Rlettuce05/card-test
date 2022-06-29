def Save(status_list, json_file_pass):
    import json
    json_file = open(json_file_pass, "w")
    json.dump(status_list, json_file)
    json_file.close()

def Load(json_file_pass):
    import json
    json_file = open(json_file_pass, "r")
    json_file = json.load(json_file)
    return json_file