import config as cfg

class OptionsParser:
    def __init__(self, argv, command):
        self.argv = argv
        self.argc = len(self.argv)
        self.command = command

    def Parse(self):
        skipNext = False

        for i in range(0, self.argc):
            if skipNext:
                skipNext = False
                continue

            option = self.argv[i]
            if "entrypoint" in self.command.options and i == self.argc-1 and option.find(".py") != -1:
                self.command.options["entrypoint"] = option
                continue

            if option not in self.command.options:
                raise Exception(f"invalid option: \"{option}\"")
            
            if type(self.command.options[option]) == bool:
                self.command.options[option] = True

            else:
                if i+1 >= self.argc or self.argv[i+1].find("--") != -1:
                    raise Exception(f"invalid \"{option}\" value")
                
                value = self.argv[i+1]

                match type(self.command.options[option]).__name__:
                    case "str":
                        self.command.options[option] = value

                    case "int":
                        self.command.options[option] = int(value)

                    case "list":
                        self.command.options[option] = value.split(";")

                    case _:
                        raise Exception(f"unsupported \"{option}\" type")
                skipNext = True
    
    def Validate(self):
        ...


