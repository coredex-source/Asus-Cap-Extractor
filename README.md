# BiosUtils-Core
- A python program which aims to automate the process of extracting various BIOS file types.

## Currently supports:
- A .cap to .bin converter tested for ASUS cap files, might work with other manufacturers as well.

## Download:
- Download from the releases tab or:
- Windows x64 : [Download](https://github.com/coredex-source/BiosUtils-Core/releases/download/v0.2/biosutils.exe)
- For other operating systems use the python files from the source code.

## For Usage instructions and other information:
- [Refer to the Wiki](https://github.com/coredex-source/BiosUtils-Core/wiki)

## I need support and suggestions.
- To be able to make this a big success I would appriciate the help of the community, anyone who can, open an issue in the "Issues" tab with a link to the bios "setup" file which you are unable to extract from the vendor.
- I would recommend using [BiosUtilities by platomav](https://github.com/platomav/BIOSUtilities) first, if you are still unable to get an extracted file then please open an issue here.
- Any useful opened "issue" will be appriciated and your github username will be added to the list of contributors below.

## Contributors:
- Be the first one to be added to the list!

## Build an EXE from source:
- Install python.
- Install pyinstaller using pip install pyinstaller.
- Open the directory of the code files and execute the following command:
       - pyinstaller -F biosutils.py
- Grab the exe from the dist folder.