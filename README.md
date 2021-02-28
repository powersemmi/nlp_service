# NLP_SERVICE

For starting prod create venv from req.txt

```console
foo@bar:~$ sudo pacman -S python-virtualenv

resolving dependencies...
looking for conflicting packages...

Packages (2) python-filelock-3.0.12-5  python-virtualenv-20.4.2-1

Total Download Size:   4.82 MiB
Total Installed Size:  7.48 MiB

:: Proceed with installation? [Y/n]  
:: Retrieving packages...
 python-virtualen...     4.8 MiB  11.3 MiB/s 00:00 [######################] 100%
 python-filelock-...    12.0 KiB  0.00   B/s 00:00 [######################] 100%
(2/2) checking keys in keyring                     [######################] 100%
(2/2) checking package integrity                   [######################] 100%
(2/2) loading package files                        [######################] 100%
(2/2) checking for file conflicts                  [######################] 100%
(2/2) checking available disk space                [######################] 100%
:: Processing package changes...
(1/2) installing python-filelock                   [######################] 100%
(2/2) installing python-virtualenv                 [######################] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...

foo@bar:~$ python3 -m venv .venv
```