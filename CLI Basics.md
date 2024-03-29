# Getting Familiar with CLI

## Navigation

`cd` is the command to navigate through the **File System**. `cd` stands for *Change Directory* and it will allow you to change your location from on directory to another back and forth. `cd` command expects you to provide a **PATH** to navigate into. `cd` is a command in *Linux* and *MacOS*, it is an *Alias* in *Windows PowerShell* for `Get-Location`.

There are a few charactor symobls that represents certain directories in the File System. 
* The tilde:  `~`
* The single dot:  `.`
* The double dot:  `..`

and 

* `~` stands for current user's **home directoy**.
* `.` stands for current directory
* `..` stands for parent directory

## Creating Directory or Folders

To create a directory use `mkdir` command in all *Windows*, *Linux/Unix* or *MacOS* by supplying absolute or relative path, for example (Mac Terminal):

```bash
> mkdir /Users/dilshad/Desktop/MyProjects
```
 
Example for Windows PowerShell:

```PowerShell
> mkdir C:\Users\dilshad\Desktop\MyProjects
```

## Creating a File

Creating a file in *Linux* or *MacOS* is same as it is using `bash`. However, it is different in `PowerShell`. 

In `PowerShell` we uses `CmdLets` (CommandLets):

```PowerShell
> New-Item -ItemType File -Name Hello.py -Path C:\Users\dilshad\Desktop\MyProjects
```

In `Bash`, however, much shorter, we use command `touch`:

```bash
> touch /Users/dilshad/Desktop/Hello.py
```