# scripts/dev.ps1
Get-Content .env-dev | ForEach-Object {
    if ($_ -match "^(.*?)=(.*)$") { [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2]) }
}
uv run uvicorn app.main:app --reload --host $env:HOST --port $env:PORT
