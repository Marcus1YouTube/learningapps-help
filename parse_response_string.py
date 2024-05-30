from urllib.parse import unquote_plus
from rich.console import Console

console = Console()

"""
Tamás bácsi ezeket a feladat típusokat szokta adni:
- Párkereső
- Csoportba rendezés
- Egyszerű sorbarendezés
- Hiányos szöveg
- Legyen ön is milliomos
- Csoportos kirakós
- Keresztrejtvény
- Szókereső
"""
def parseResponseString(string: str, task_type: str, console: object):
    console.log("A fejlesztő túl lusta volt, hogy megcsinálja a feladat megoldó kódot. Ezért azt mondja, hogy oldd meg magad. Tessék, itt a feladat-string:")
    console.print(unquote_plus(string))

def textFillParse(string: str, console: object):
    ...

# Tesztelés
if __name__ == "__main__":
    textFillParse("""
        type=Kiválasztás listából&titel=image|https://dbimg.eu/i/n4ppgdzkzp.jpg|&clozetext=Széchenyi István -1- született és 1860-ban halt meg. Apja a -2- alapítója. Édesanyja Festetics -3-. Fiatalon katonának állt, harcolt a -4- csatában is. A háború után sokat utazott, járt Franciaországban, -5- és -6- is. 1825-ben a pozsonyi országgyűlésen birtokai egy évi jövedelmét ajánlotta fel a -7- javára. 1830-ban jelent meg a -8- című műve, melyben az -9- törvényének eltörlését szorgalmazza. Szerinte a mezőgazdaság fejlesztésének legfőbb akadálya a -10-. Véleménye szerint a jobbágyok robotját el kell törölni, helyette -11- kell alkalmazni. A polgári átalakulást szerinte a -12- kellene vezetnie.&cloze1=1791-ben&cloze2=Nemzeti Múzeum&cloze3=Julianna&cloze4=lipcsei&cloze5=Angliában&cloze6=Törökországban&cloze7=Magyar Tudományos Akadémia&cloze8=Hitel&cloze9=ősiség&cloze10=tőkehiány&cloze11=bérmunkát&cloze12=főnemességnek&cloze13=úriszék&cloze14=ingyenmunkát&cloze15=Országos Széchenyi Könyvtár&cloze16=waterloo-i&feedback=Nagyszerű! Minden megoldás helyes.
    """, console)