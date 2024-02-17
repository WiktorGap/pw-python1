#Biblioteka Rich to narzędzie w języku Python, które umożliwia tworzenie interaktywnych i kolorowych w konsoli interfejsów użytkownika.
#Jest to narzędzie do formatowania tekstu w terminalu w bardziej zaawansowany sposób niż standardowe metody dostępne w języku Python. 
#Biblioteka ta zapewnia różnorodne funkcje do formatowania tekstu, takie jak zmiana kolorów, stylowanie, tworzenie tabel, wyświetlanie obrazów 
#oraz wiele innych




from rich.console import Console
from rich.table import Table
from rich.text import Text

# Tworzenie obiektu konsoli
console = Console()

# Formatowanie tekstu
text = Text("Witaj, to jest [bold magenta]tekst[/bold magenta] z wykorzystaniem [italic cyan]biblioteki[/italic cyan] Rich!")
console.print(text)

# Tworzenie tabeli
table = Table(title="Dane użytkownika")
table.add_column("ID")
table.add_column("Imię")
table.add_column("Nazwisko")

table.add_row("1", "Jan", "Kowalski")
table.add_row("2", "Anna", "Nowak")

console.print(table)

# Wyświetlanie obrazu
console.print("[image]https://www.example.com/image.jpg[/image]")




from rich import print as rprint

# Stylowanie tekstu
rprint("[bold]Tekst pogrubiony[/bold]")
rprint("[italic]Tekst pochylony[/italic]")
rprint("[underline]Tekst podkreślony[/underline]")
rprint("[bold red]Tekst pogrubiony i czerwony[/bold red]")
rprint("[italic cyan]Tekst pochylony i cyjanowy[/italic cyan]")
rprint("[underline yellow]Tekst podkreślony i żółty[/underline yellow]")
