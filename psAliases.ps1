function Git-Update {
    Push-Location;gci . -Directory|%{Set-Location $_.FullName;Write-Host $_.Name; git pull;Write-Host};Pop-Location
}
new-alias gitpull Git-Update

function Git-Status {
    Push-Location;gci . -Directory|%{Set-Location $_.FullName;Write-Host $_.Name; git status;Write-Host};Pop-Location
}
new-alias gitstatus Git-Status
