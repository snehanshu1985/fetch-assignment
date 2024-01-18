import argparse
import logging
import os
import sys
import yaml
import requests
import time
from urllib.parse import urlparse
from collections import defaultdict

# Code block to declare constant
RESPONSE_TIME_CHECK = 500
TIMER_RUN = 15

timer = 0
cycle = 1
domain_out = defaultdict(list)


# Function to take the file as input, validate it and convert it to a list.
def file_input():
    filepath = input("Please provide the file path. It should be in format C:\\Users\\input.yaml or /home/input.yaml "
                     "and should be an yaml file :")
    if os.path.exists(filepath):
        with open(filepath, 'r') as stream:
            input_data = yaml.safe_load(stream)
        return input_data
    else:
        logging.error("File does not exist. Script execution will be stopped.")
        sys.exit(1)


# Function to parse the list, make calls and generate result.
def generate_result(input_list, domain_output):
    i = 0
    for i in range(0, len(list(input_list))):
        name = input_list[i].get('name')
        url = input_list[i].get('url').replace("https", "http")
        method = input_list[i].get('method')
        headers = input_list[i].get('headers')
        body = input_list[i].get('body')
        domain_name = urlparse(url).netloc  # Fetches domain name from URL.
        if name is None or url is None:
            logging.error("Input request is not in correct format. Script execution will be stopped.")
            sys.exit(1)
        else:
            url_response = ""
            start_time = time.perf_counter()
            if method == "GET" or method is None:
                url_response = requests.get(url, headers=headers, params=body)
            elif method == "POST":
                url_response = requests.post(url, headers=headers, json=body)
            elif method == "DELETE":
                url_response = requests.delete(url, json=body, headers=headers)
            elif method == "PUT":
                url_response = requests.put(url, json=body, headers=headers)
            response_time = (time.perf_counter() - start_time) * 1000
        if (200 <= url_response.status_code <= 299) and response_time < RESPONSE_TIME_CHECK:  # Logic to generate the
            # response status.
            response_status = "UP"
        else:
            response_status = "DOWN"
        logging.info(
            "Endpoint with name {} and domain {} has HTTP response code {} and response latency {} => {}".format(name,
                                                                                                                 domain_name,
                                                                                                                 url_response.status_code,
                                                                                                                 response_time,
                                                                                                                 response_status))
        domain_output[domain_name].append(response_status)
        i += 1
    return domain_output


# Function to generate final result.
def generate_final_result(output_dict):
    logging.info(dict(output_dict))
    for (k, v) in output_dict.items():
        result = (v.count("UP") / len(v)) * 100
        print("{} has {}% availability percentage".format(k, round(result)))


if __name__ == '__main__':
    url_list = file_input()
    parser = argparse.ArgumentParser()
    parser.add_argument('-log',
                        '--loglevel',
                        default='warning',
                        help='Provide logging level. Example --loglevel debug, default=warning')
    args = parser.parse_args()
    logging.basicConfig(format='%(message)s', level=args.loglevel.upper())
    while True:
        logging.info("Test cycle #{} begins at time = {} seconds".format(cycle, timer))
        output = generate_result(url_list, domain_out)
        logging.info("Test cycle #{} ends.".format(cycle))
        generate_final_result(output)
        timer += TIMER_RUN  # Increases timer by 15s.
        cycle += 1
        time.sleep(timer)
