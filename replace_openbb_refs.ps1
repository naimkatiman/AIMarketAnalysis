$files = Get-ChildItem -Path "d:\test\AIMarketAnalysis" -Recurse -Filter "README.md"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Replace OpenBB with AIMarketAnalysis
    $updatedContent = $content -replace "OpenBB", "AIMarketAnalysis"
    
    # Replace openbb with aimarketanalysis in package names and commands
    $updatedContent = $updatedContent -replace "openbb-", "aimarketanalysis-"
    $updatedContent = $updatedContent -replace "pip install openbb", "pip install aimarketanalysis"
    $updatedContent = $updatedContent -replace "from openbb import obb", "from aimarketanalysis import ama"
    $updatedContent = $updatedContent -replace "obb\.", "ama."
    
    # Replace URLs
    $updatedContent = $updatedContent -replace "openbb\.co", "aimarketanalysis.co"
    $updatedContent = $updatedContent -replace "OpenBB-finance/OpenBB", "naimkatiman/AIMarketAnalysis"
    
    # Only update if changes were made
    if ($content -ne $updatedContent) {
        Set-Content -Path $file.FullName -Value $updatedContent -NoNewline
        Write-Host "Updated: $($file.FullName)"
    }
}
