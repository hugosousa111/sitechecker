import sys
import csv
import os 
import datetime

from sitechecker.cli import read_user_cli_args, display_check_result
from sitechecker.checker import site_is_online

PATH_PROJECT = '/home/hugosousa111/lighthouse/sitechecker/'

def main():
    """Run Site Checker."""

    user_args = read_user_cli_args()
    urls = user_args.urls
    file = user_args.file
    if not urls and not file:
        print("Erro: sem URLs ou File para analisar.", file=sys.stderr)
        sys.exit(1)
    if not urls:
        _site_check_file(file[0])
    else:
        _site_check_urls(urls)

def _site_check_urls(urls):
    with open(os.path.join(PATH_PROJECT, 'sitechecker.log'),mode='a') as log_file:
        now = datetime.datetime.now()
        log_file.write(str(now))
        log_file.write("\n") 

    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        log = display_check_result(result, url, error)
        
        with open(os.path.join(PATH_PROJECT, 'sitechecker.log'),mode='a') as log_file:
            log_file.write(log)
            log_file.write("\n") 

    with open(os.path.join(PATH_PROJECT, 'sitechecker.log'),mode='a') as log_file:
        log_file.write(log)
        log_file.write("\n\n\n") 

def _site_check_file(file):
    with open(os.path.join(file), newline='') as csv_file:
        reader = csv.reader(csv_file)
        urls = []
        for row in reader:
            urls.append(''.join(row))
        urls.pop(0) #column name
    _site_check_urls(urls)

if __name__ == '__main__':
    main()
