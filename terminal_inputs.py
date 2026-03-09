from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Select Action")

table.add_column("Option", style="cyan")
table.add_column("Description", style="magenta")

table.add_row("1", "Build Project")
table.add_row("2", "Deploy")
table.add_row("3", "Clear Cache")

console.print(table)

choice = console.input("[bold yellow]Enter option:[/] ")

console.print(f"You selected: [green]{choice}[/green]")
