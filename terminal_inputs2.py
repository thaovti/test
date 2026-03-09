import typer
from rich import print

app = typer.Typer()

@app.command()
def build(env: str):
    print(f"[green]Building project for {env}[/green]")

@app.command()
def deploy(env: str):
    print(f"[yellow]Deploying to {env}[/yellow]")

@app.command()
def cache_clear():
    print("[red]Clearing cache[/red]")

if __name__ == "__main__":
    app()
