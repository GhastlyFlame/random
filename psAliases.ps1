<#
    .Description
    Runs git pull for every repo in the dir
#>
function Git-Update {
    Push-Location;gci . -Directory|%{Set-Location $_.FullName;Write-Host $_.Name; git pull;Write-Host};Pop-Location
}
new-alias pull Git-Update

<#
    .Description
    Runs git status for every repo in the dir
#>
function Git-Status {
    Push-Location;gci . -Directory|%{Set-Location $_.FullName;Write-Host $_.Name; git status;Write-Host};Pop-Location
}
new-alias status Git-Status
<#
    .Description
    Runs git fetch for every repo in the dir
#>
function Git-Fetch {
    Push-Location;gci . -Directory|%{Set-Location $_.FullName;Write-Host $_.Name; git status;Write-Host};Pop-Location
}
new-alias fetch Git-Fetch