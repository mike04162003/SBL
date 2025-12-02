

Slim Bootloader support platform list
=====================================


FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
12th, 13th, & 14th Generation Intel Core processors and chipsets (formerly Alder Lake, Raptor Lake, & Raptor Lake Refresh) | RaptorlakeFspBinPkg | v2.3

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-6884|688400S|0x1D|RaptorlakeBoardPkg|LLDR;UEFI|Bring up to OS
SOM-C350|C35000S|0x1C|AlderlakeBoardPkg|LLDR;UEFI|Bring up to uefi shell



FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
11th Generation Intel Core processors and chipsets (formerly Tiger Lake) | TigerLakeFspBinPkg | v2.2


Porject Name | Porject ID | Platform ID | Directory Name  | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------
SOM-7583|758300S|0x10|TigerlakeBoardPkg|LLDR;UEFI|Ready



Build Environment
-----------------

    set PYTHON_HOME=C:\Python36
    set NASM_PREFIX=C:\Nasm
    set IASL_PREFIX=C:\ASL
    set OPENSSL_PATH=C:\Openssl

  Usage:
    
    python Sbl.py -p $(Porject ID)

License
-------
Slim Bootloader is released under the terms of the BSD-2-Clause Plus Patent License.
