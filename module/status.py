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

class status:

    def __init__(self, *status):
        self.status_data = {"status": {}}
        if status:
            for i in range(len(status)):
                self.status_data["status"].update((status[0],status[1]))