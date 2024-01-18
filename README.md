# Overview
Implement a program to check the health of http endpoints. End user will provide a config file, which code will use to check the status. Script will continue to check the status till user presses Ctrl + C.

## Language used
Python

## How to install
Install python3 and required libraries for it to work
```
MAC OS
1. Check whether git, python3 and pip3 is installed.
   git --version
   python3 --version
   pip3 --version
2. Install git, python3 and pip3 if not present. 
   https://git-scm.com/download/mac
   Install python3 and pip3
   https://iboysoft.com/howto/install-python-on-mac.html
3. Once required softwares are installed please check python packages are present. 
   pip3 show pyyaml
   pip3 show requests. 
4. If above python packages are not present please install it.
   pip3 install pyyaml
   pip3 install requests
5. Pull the code.
   git pull https://github.com/snehanshu1985/fetch-assignment.git
6. Excution
   cd {localdirectory where code is pulled}/fetch-assignment
   python3 url.py
   
LINUX
Ubuntu
1. Check whether git, python3 and pip3 is installed.
   git --version
   python3 --version
   pip3 --version
2. Install git, python3 and pip3 if not present. 
   apt install git
   apt install python3
   apt install python-pip3
3. Once required softwares are installed please check python packages are present. 
   pip3 show pyyaml
   pip3 show requests. 
4. If above python packages are not present please install it.
   pip3 install pyyaml
   pip3 install requests
5. Pull the code.
   git pull https://github.com/snehanshu1985/fetch-assignment.git
6. Excution
   cd {localdirectory where code is pulled}/fetch-assignment
   python3 url.py

RedHat/CentOS
1. Check whether git, python3 and pip3 is installed.
   git --version
   python3 --version
   pip3 --version
2. Install git, python3 and pip3 if not present. 
   yum install git
   yum install python3
   yum install python-pip3
3. Once required softwares are installed please check python packages are present. 
   pip3 show pyyaml
   pip3 show requests. 
4. If above python packages are not present please install it.
   pip3 install pyyaml
   pip3 install requests
5. Pull the code.
   git pull https://github.com/snehanshu1985/fetch-assignment.git
6. Excution
   cd {localdirectory where code is pulled}/fetch-assignment
   python3 url.py
   
WINDOWS
1. Check whether python is present using powershell.
   python --version
2. If not present then install it from the below documents and add to the path.
   https://www.python.org/downloads/windows/
3. Check whether git is present. 
   git --version
4. If not please install from the below document(Check or windows)
   https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
5. Check and install python packages.
   pip show pyyaml
   pip show requests
   pip install pyyaml
   pip install requests
6. Pull the code.
   git pull https://github.com/snehanshu1985/fetch-assignment.git
7. Excution
   cd {localdirectory where code is pulled}/fetch-assignment
   python3 url.py
```

### Program execution
```
1. To run the program without the info logs
   python3 url.py
2. To run the program with the info logs
   python3 url.py --loglevel info
   python3 url.py --log info
3. The program will ask for the config file location. It will check if file is present.
4. If present it will convert to a list, make calls and generate the result.
5. If file is not present it will stop the execution.
```

### How code works.
| Name | Type | Usage |
| ---- | ---- | ----- |
| RESPONSE_TIME_CHECK | Constant  | This will store the latency threshold post which the end point call will be declared as DOWN. |
| TIMER_RUN | Constant | This will ensure the script re-runs after 15s. |
| file_input | Function  | This will take the file location as input, validates whether file is present in the location and then generate the list from it. |
| generate_result | Function | This will take the list as input, make the http calls and generate the result in a dictionary for a single run. |
| generate_final_result | Function | This will take the generated dictionary as input and will generate the expected final result for the complete run. |



