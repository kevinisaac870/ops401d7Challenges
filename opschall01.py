# Script:                       Ops401d7 Ops Challenge 01
# Author:                       Kevin Isaac
# Date of latest revision:      20230118
# Purpose:      Automate Screen Lock

# Attribution: https://quickbytesstuff.blogspot.com/2014/10/lock-computer-using-powershell.html

Echo “Computer locking due to inactivty....”

$WShell = New-Object -com “Wscript.Shell”


while ($true)


{


Start-Sleep -Seconds 10

$xCmdString = {rundll32.exe user32.dll,LockWorkStation}

Invoke-Command $xCmdString



Exit
}

# End
