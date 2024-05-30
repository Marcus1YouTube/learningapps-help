import json
import os

class Cacher:
    def __init__(self, console):
        self.console = console
    
    def findIsCached(self, id: int):
        try:
            with open("./cache/" + id + ".json", "r") as f:
                self.console.log(":heavy_check_mark: Cache megtalálva: [bold]" + id)
                return True
        except:
            self.console.log(":x: [bold orange]Nincs cache: " + id)
            return False
        
    def saveCache(self, text: str, id: int):
        with open("./cache/" + id + ".json", "w") as f:
            f.write(json.dumps(text))
            self.console.log(":heavy_check_mark: Cache mentve: [bold]" + id)
            return True

    def loadCache(self, id: int):
        with open("./cache/" + id + ".json", "r") as f:
            self.console.log(":heavy_check_mark: Cache betöltve: [bold]" + id)
            return json.loads(f.read())
        
    def removeCache(self, id: int):
        try:
            os.remove("./cache/" + id + ".json")
            self.console.log(":heavy_check_mark: Cache törölve: [bold]" + id)
            return True
        except:
            self.console.log(":x: [bold orange]Nincs cache ezzel az ID-vel, ami törölhető lenne.: " + id)
            return False
    