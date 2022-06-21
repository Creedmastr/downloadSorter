def startup():
    from tkinter import simpledialog
    from os.path import exists

    #First setup using Tkinter
    files_json_startup = exists("./config.json")

    global USER_CONFIG
    USER_CONFIG = ""

    if not files_json_startup:
        USER_CONFIG = simpledialog.askstring(title="Base config starts", prompt="Please enter the path to 'C:/Users/<yourusernamehere>' (Replace the \ by /, otherwise it won't work)")
        if USER_CONFIG == "":
            exit()
        USER_CONFIG_TOWRITE = '{ "user_path_input": "' + str(USER_CONFIG) + '" }'
        with open("config.json", "w") as f:
                f.write(USER_CONFIG_TOWRITE)