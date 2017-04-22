#!/usr/bin/env python
import os
from app import app

if os.geteuid() != 0:
    print('\033[93m' + 'You need to have root privileges to run this script\n' + '\033[0m')
    print('\033[94m' + "Please try again, this time using 'sudo'. Exiting.\n"  + '\033[0m')
    exit

def main():
    app.run(debug=True, host='0.0.0.0', port=80)

if __name__ == '__main__':
    main()
