# Preparation for CUCaTS coding workshop

<!-- MarkdownTOC autolink=true bracket=round depth=5 -->

- [Installing Python](#installing-python)
    - [Windows](#windows)
    - [Mac](#mac)
    - [Linux](#linux)
- [Installing package installer](#installing-package-installer)
    - [Windows](#windows-1)
    - [Mac and Linux](#mac-and-linux)

<!-- /MarkdownTOC -->


## Installing Python

https://www.python.org/downloads/release/python-342/

### Windows

* Choose [Windows x86-64 MSI installer](https://www.python.org/ftp/python/3.4.2/python-3.4.2.amd64.msi) for 64 bit or [Windows x86 MSI installer](https://www.python.org/ftp/python/3.4.2/python-3.4.2.amd64.msi) for 32 bit. If in doubt, choose 32 bit.
    * This only matters if you want to install libraries in the future as you need to install the same version as your Python version.
* Run it and follow instructions.
* To test if your installation is successful. You can press `win + R`, enter `cmd` to launch the command prompt, and enter `py` and it should start a python console.

### Mac

* For OS X 10.6 and above, Download and run [this](https://www.python.org/ftp/python/3.4.2/python-3.4.2-macosx10.6.pkg).
* Open your terminal by pressing `cmd + space` and entering `terminal`. Type `python3`

### Linux

* Start your terminal, and install it using your package manager. For example, `sudo apt-get install python3` or `sudo yum install python3`

## Installing package installer

Python comes with many useful libraries which you can install easily with a package manager. Here we will be using [pip](https://pip.pypa.io/en/latest/installing.html). 

### Windows
* Download the [installer script](https://bootstrap.pypa.io/get-pip.py) and save it somewhere (say desktop). 
* Browse to your desktop, hold down `shift` and right click on an empty space, select `Open command window here`.
* Enter `py get-pip.py`

### Mac and Linux
* You might want to check if you have pip installed. Open your terminal and type `pip` or `python3 -m pip`. If you don't get an error, then you already have it installed. 
    * In that case, run `python3 -m pip install --upgrade pip`. This will update pip and you can run it in the future with `pip` rather than `python3 -m pip`
* If you don't have pip, you can run the following command which is a script to download the installer and installing it.
    - `curl -OL https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py`
    - If it complains about permission denied, you can try running `sudo python3 get-pip.py`