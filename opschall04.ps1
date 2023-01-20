# Script:                       Ops Challenge 04
# Author:                       Kevin Isaac
# Date of latest revision:      20230119
# Purpose:     Automate Change Password Complexity

# Attribution: 
# https://www.reddit.com/r/PowerShell/comments/6mebpt/enforce_password_complexity_via_powershell/
# https://social.technet.microsoft.com/Forums/office/en-US/50c827f8-0b8f-4b07-a90f-582948187ccb/disabling-password-complexity-via-powershell?forum=winserverpowershell


secedit /export /cfg c:\secpol.cfg
(GC C:\secpol.cfg) -Replace "PasswordComplexity = 0","PasswordComplexity = 1" | Out-File C:\secpol.cfg
secedit /configure /db c:\windows\security\local.sdb /cfg c:\secpol.cfg /areas SECURITYPOLICY
Remove-Item C:\secpol.cfg -Force

# End
