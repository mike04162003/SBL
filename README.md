

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
Intel Core Ultra Processors for IoT Edge (Formerly known as Meteor Lake-UH and Meteor Lake-PS). | MeteorlakeFspBinPkg | v2.3

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-A350|A35000S|0x01|MeteorlakeBoardPkg|LLDR;UEFI|Bring up sbl shell


FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
Intel XeonR D-1700 and D-2700 Processor Family (formerly Ice Lake-D LCC and HCC) | IdavilleFspBinPkg | v2.1

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-5993|599300S|0x0F|IdavilleBoardPkg|LLDR;UEFI|Bring up to OS


FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
11th Generation Intel Core processors and chipsets (formerly Tiger Lake) | TigerLakeFspBinPkg | v2.2

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-7583|758300S|0x10|TigerlakeBoardPkg|LLDR;UEFI|Ready to OS


FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
Intel Atom x6000E series, and Intel PentiumR and CeleronR N and J Series processors | ElkhartLakeFspBinPkg | v2.1

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-2532|253200S|0x10|ElkhartlakeBoardPkg|LLDR;UEFI|Bring up to uefi shell


FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
9th & 8th Generation Intel Core processors and chipsets (formerly Coffee Lake Refresh, Coffee Lake, and Whiskey Lake) | CoffeeLakeFspBinPkg | v2.0

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-6882|688200S|0x10|CoffeelakeBoardPkg|LLDR;UEFI|Bring up to OS


FSP Project Name | Directory Name | FSP Specification Version
:--------------- | :------------- | :------------------------
Intel Atom processor E3900 product family (formerly Apollo Lake) | ApolloLakeFspBinPkg | v2.0

Porject Name | Porject ID | Platform ID | Directory Name | Payload Type | Status
:----------- |:----------- |:-------------- | :---------- | :----------  | :----------
SOM-7569|756900S|0x13|ApollolakeBoardPkg|LLDR;UEFI|Bring up to OS


Build Environment
-----------------

    set PYTHON_HOME=C:\Python36
    set NASM_PREFIX=C:\Nasm
    set IASL_PREFIX=C:\ASL
    set OPENSSL_PATH=C:\Openssl

  Usage:
    
    python Sbl.py -p $(Porject ID)
    
    or
    
    slim -p $(Porject ID)

License
-------
Slim Bootloader is released under the terms of the BSD-2-Clause Plus Patent License.
