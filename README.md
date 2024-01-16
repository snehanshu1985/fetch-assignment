# Overview
Implement a program to check the health of http endpoints. End user will provide a config file, which code will use to check the status. Script will continue to check the status till user presses Ctrl + C.

## Language used
Python

## How to install
Install python3 and required libraries for it to work
```
MAC OS
    Install python3 and pip3
        https://iboysoft.com/howto/install-python-on-mac.html
    Once python3 is installed install the following libraries
        pip3 install pyyaml
        pip3 install requests. 
    Pull the code into local and execute.
        git pull 
        python3 fetch-assignment/url.py
WINDOWS
LINUX
```

### How code works.
| Name | Type | Usage |
| ---- | ---- | ----- |
| RESPONSE_TIME_CHECK | Constant  | This will store the latency threshold post which the end point call will be declared as DOWN. |
| TIMER_RUN | Constant | This will ensure the script re-runs after 15s. |
| file_input | Function  | This will take the file location as input, validates whether file is present in the location and then generate the list from it. |
| generate_result | Function | This will take the list as input, make the http calls and generate the result in a dictionary for a single run. |
| generate_final_result | Function | This will take the generated dictionary as input and will generate the expected final result for the complete run. |



