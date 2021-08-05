if(Get-Process -Name windbg -ErrorAction SilentlyContinue){
    Stop-Process -Name windbg
    Start-Sleep -Seconds 10
    }
    if ((Get-Service -Name 'Disk Pulse Enterprise').Status -ne 'running'){
    Start-Service -Name 'Disk Pulse Enterprise'
    Start-Sleep -Seconds 10
    }
& "C:\Program Files\Windows Kits\10\Debuggers\x86\windbg.exe" -WF C:\windbg_custom.WEW -p (Get-Process -Name diskpls).Id -c "g"