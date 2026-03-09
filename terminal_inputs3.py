from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

table = Table(
    title="ANALYST SIGNALS:",
    box=box.ASCII_DOUBLE_HEAD
)

table.add_column("Analyst", style="cyan")
table.add_column("Signal", justify="center")
table.add_column("Confidence", justify="right", style="yellow")

table.add_row("Fundamentals", "[green]BULLISH[/green]", "50.0%")
table.add_row("Technical Analyst", "[green]BULLISH[/green]", "22%")
table.add_row("Valuation", "[red]BEARISH[/red]", "81.0%")
table.add_row("Sentiment", "[red]BEARISH[/red]", "100.0%")
table.add_row("Risk Management", "", "None%")

console.print(table)

decision = Table(title="TRADING DECISION:", box=box.ASCII)

decision.add_column("Field")
decision.add_column("Value", justify="right")

decision.add_row("Action", "[cyan]BUY[/cyan]")
decision.add_row("Quantity", "[cyan]20000[/cyan]")
decision.add_row("Confidence", "[yellow]0.7%[/yellow]")

console.print(decision)
