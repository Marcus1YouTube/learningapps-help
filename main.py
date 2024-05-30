from urllib.parse import urlparse, parse_qs
import requests
import json
from pyfiglet import Figlet
from rich.console import Console
from rich.prompt import Confirm, Prompt
from cacher import Cacher
import parse_response_string

figlet = Figlet(font='doom', width=150)
console = Console()
confirm = Confirm()
prompt = Prompt()
cacher = Cacher(console)

def main():
    if not confirm.ask("Igazán kell segítség"):
        console.print("[bold red]Hát akkor menj innen!")
        exit(0)

    console.print(figlet.renderText("LearningApps segitsegkero program"), highlight=False, style="bold cyan")
    learningapps_url = console.input("[bold orange]Jobb kattintással nyomj rá a feladat képére (a kiválasztó kijelzőn) és nyomj rá a Képcím másolása gombra.[/] Illeszd be ide, kérlek: ")
    
    # NOTE: Például: https://learningapps.org/appicons/thumbs.php?url=https%3A%2F%2Flearningapps.org%2Fwatch%3Fv%3Dpazwm18x320&r=1712589009450 
    learningapps_url = urlparse(learningapps_url)
    url_params = parse_qs(learningapps_url.query)
    learningapps_id: int = None

    try:
        if url_params["url"][0]:
            url_param_params = parse_qs(urlparse(url_params["url"][0]).query)
            console.log(":heavy_check_mark: Kód: [bold]" + url_param_params["v"][0])
            learningapps_id = url_param_params["v"][0]
    except:
        console.print("[bold red]Ezzel nem tudok mit kezdeni...")
        exit(1)
    
    if not cacher.findIsCached(learningapps_id):
        with console.status("Letöltés az internetről...") as status:
            response = requests.get(f"https://learningapps.org/data?jsonp=1&id={learningapps_id}&version=46")
            response_text = response.text.strip("var AppClientAppData = ;")
            cacher.saveCache(response_text, learningapps_id)

    response_obj = json.loads(cacher.loadCache(learningapps_id))

    if response_obj["result"] != "SUCCESS":
        console.log(":x: HIBA: " + response_obj["result"], style="bold red")
        cacher.removeCache(learningapps_id)
        exit(1)

    # "Melyik feladatot szeretnéd megjelenítendődni?" lol ez funny
    task_type = prompt.ask("Milyen típusú feladatot szeretnéd megoldani?", choices=["Párkereső", "Csoportba rendezés", "Egyszerű sorbarendezés", "Hiányos szöveg", "Csoportos kirakós", "Keresztrejtvény", "Szókereső"], default="Párkereső")
    parse_response_string.parseResponseString(response_obj["initparameters"], task_type, console)


if __name__ == "__main__":
    main()