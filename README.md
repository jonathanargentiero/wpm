# WPM
*Wakanda Package Manager*
* * *
 
A package management tool made with Python.

** WARNING! This software is experimental. It works only in lazy mode without caring much about your modifications. To be used with caution! **


## Requirements

* [Python 2.7.x](https://www.python.org/downloads/)

## Installation
1. Dowload the latest distribution from [dist/wpm](https://github.com/jonathanargentiero/wpm/blob/master/dist/wpm?raw=true).
2. Copy it wherever you like. Depending on your OS, if you configure correctly your `$PATH` variable you will be able to invoke it without the relative path.
3. Navigate in the command line in your `Wakanda/Extension` folder. If you want to install widgets for a projects navigate in your `Solution/Project/Widgets` directory instead.
4. Run on the command line:
   
   (if you have set the $PATH variable)
   
   ````
   $ python wpm
   ````
   
   (otherwise)
   
   ````
   $ python /path/to/wpm
   ````
   
   If everything is fine you will be given a description of the utility.
   
5. Update to the latest version:
   
   ````
   $ python wpm update --self
   ````
   


## How to use

In the command line run:

````
$ python wpm --help
````

to see a list of the enabled commands like:


````
$ python wpm list
$ python wpm list --all
$ python wpm install [package-name ..]
$ python wpm update 
$ python wpm update --self
$ python wpm remove [package-name ..]
$ python wpm purge
````

## Contribute

The project is just a POC and require some works. You can contribute by making pull-requests to the repository.
Distribution will be released once required.