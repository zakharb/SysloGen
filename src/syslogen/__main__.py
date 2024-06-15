"""
    SYSLOGEN
    Simple Log Generator
    Copyright (C) 2021 Bengart Zakhar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Description:

    Author:
        Bengart Zakhar
"""
import os

import argparse
from syslogen.core import Syslogen

def showlicense():
    license = ('Simple Syslog Generator\n'
               'Copyright (C) 2021 Bengart Zakhar\n\n'
               'This program is free software: you can redistribute it and/or modify\n'
               'it under the terms of the GNU General Public License as published by\n'
               'the Free Software Foundation, either version 3 of the License, or\n'
               '(at your option) any later version.\n\n'
               'This program is distributed in the hope that it will be useful,\n'
               'but WITHOUT ANY WARRANTY; without even the implied warranty of\n'
               'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n'
               'GNU General Public License for more details.\n\n'
               'You should have received a copy of the GNU General Public License\n'
               'along with this program.  If not, see <https://www.gnu.org/licenses/>.')
    print(license)

def main():
    print('Syslogen Simple Syslog Generator\n'
          'Copyright (C) 2021 Bengart Zakhar\n'
          'This program comes with ABSOLUTELY NO WARRANTY\n'
          'This is free software, and you are welcome to redistribute it\n'
          'under certain conditions; type `--license` for details.\n')
    print('   _______  _______ __    ____  _____________   __\n'\
          '  / ___/\ \/ / ___// /   / __ \/ ____/ ____/ | / /\n'\
          '  \__ \  \  /\__ \/ /   / / / / / __/ __/ /  |/ / \n'\
          ' ___/ /  / /___/ / /___/ /_/ / /_/ / /___/ /|  /  \n'\
          '/____/  /_//____/_____/\____/\____/_____/_/ |_/   \n')
    parser = argparse.ArgumentParser(
        prog='syslogen', 
        usage='%(prog)s [options]')
    parser.add_argument(
        "server_ip", 
        type=str, 
        help="IP address of Syslog server where to send messages")
    parser.add_argument(
        "-p", 
        "--port",
        type=int, 
        help="Port of Syslog server")
    parser.add_argument(
        "-i", 
        "--input",
        type=str, 
        help="File used to generate messages")
    parser.add_argument(
        "-c", 
        "--count",
        type=int, 
        help="Number of generated messages per second")
    args = parser.parse_args()
    if args.input and args.count:
        port = args.port if args.port else 514
        syslogen = Syslogen(args.server_ip, port, args.input, args.count)
        syslogen.start()
    else:
        print("Not enough arguments, '--help' for more info")

if __name__ == "__main__":
    main()