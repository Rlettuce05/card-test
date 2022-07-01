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
                self.status_data["status"][status[i][0]] = status[i][1]

    def Add(self, *status):
        if status:
            for i in range(len(status)):
                self.status_data["status"][status[i][0]] = status[i][1]
    
    def Remove(self, key):
        self.status_data.pop(key)
    
    def ChangeStates(self, key, value):
        self.status_data["status"][key] = value

    def CallStatusData(self):
        return self.status_data
