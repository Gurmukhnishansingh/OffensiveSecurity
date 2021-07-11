if(Get-Process -Name windbg -ErrorAction SilentlyContinue){
    Stop-Process -Name windbg
    Start-Sleep -Seconds 10
    }
    if ((Get-Service -Name 'Sync Breeze Enterprise').Status -ne 'running'){
    Start-Service -Name 'Sync Breeze Enterprise'
    Start-Sleep -Seconds 30
    }
    & "C:\Program Files\Windows Kits\10\Debuggers\x86\windbg.exe" -p (Get-Process -Name syncbrs).Id