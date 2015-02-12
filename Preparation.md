Preparation for the CUCaTS coding workshop

<!-- MarkdownTOC autolink=true bracket=round -->

- [Installing Python](#installing-python)
    - [Windows](#windows)
    - [Mac](#mac)
    - [Linux](#linux)
- [Installing the package installer](#installing-the-package-installer)
    - [Windows](#windows-1)
    - [Mac and Linux](#mac-and-linux)

<!-- /MarkdownTOC -->


# Installing Python

Python is both a programming language and a piece of software. There are two popular versions of Python: Python 2 and Python 3. We are going to be using Python 3, which is more modern.

It will save time if you can install Python 3 on your laptop before the workshop - instructions on how to do so follow.

## Windows

* Download the [Windows x86-64 MSI installer](https://www.python.org/ftp/python/3.4.2/python-3.4.2.amd64.msi) for 64 bit Windows or [Windows x86 MSI installer](https://www.python.org/ftp/python/3.4.2/python-3.4.2.amd64.msi) for 32 bit Windows. If in doubt, choose 32 bit.
    * The choice between 64 and 32 bit only matters if you want to install libraries in the future, as you will need to install the same version as your Python version.
* Run it and follow instructions.
* To test if your installation is successful. You can press `windows + R`, type `cmd` and press enter to launch the command prompt (a black box into which you can type commands), and type `python3` and press enter. The Python console should start - you should see something like:
```
Python 3.4.2 (default, Dec 27 2014, 13:16:08) 
[Something] on Windows
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
You can then close the window.

## Mac

* For OS X 10.6 and above, Download and run [this](https://www.python.org/ftp/python/3.4.2/python-3.4.2-macosx10.6.pkg).
* Open your terminal by pressing `cmd + space` and entering `terminal`. Type `python3`

## Linux

* Start your terminal and install it using your package manager. For example, `sudo apt-get install python3` or `sudo yum install python3`

# Installing the package installer

Python comes with many useful libraries which you can install easily with a package manager. Here we will be using [pip](https://pip.pypa.io/en/latest/installing.html). 

## Windows
* Download the [installer script](https://bootstrap.pypa.io/get-pip.py) and save it somewhere (e.g. your desktop). 
* Browse to your desktop, hold down `shift` and right click on an empty space, select `Open command window here`.
* Type `py get-pip.py` and press enter.

## Mac and Linux
* You might want to check if you have pip installed. Open your terminal and type `pip` or `python3 -m pip`. If you don't get an error, then you already have it installed. 
    * In that case, run `python3 -m pip install --upgrade pip`. This will update pip and you can run it in the future with `pip` rather than `python3 -m pip`
* If you don't have pip, you can run the following command which is a script to download the installer and installing it.
    - `curl -OL https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py`
    - If it complains about permission denied, you can try running `sudo python3 get-pip.py`
