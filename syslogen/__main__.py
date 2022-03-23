"""
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

#!/opt/ziem/venv/bin/python
import os
import sys
import argparse
import pkg_resources

from syslogen.syslogen import main

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

if __name__ == "__main__":
    version = pkg_resources.get_distribution('syslogen').version
    print('Syslogen {} Simple Syslog Generator\n'
          'Copyright (C) 2021 Bengart Zakhar\n'
          'This program comes with ABSOLUTELY NO WARRANTY\n'
          'This is free software, and you are welcome to redistribute it\n'
          'under certain conditions; type `--license` for details.\n'.format(version))
    print('   _______  _______ __    ____  _____________   __\n'\
          '  / ___/\ \/ / ___// /   / __ \/ ____/ ____/ | / /\n'\
          '  \__ \  \  /\__ \/ /   / / / / / __/ __/ /  |/ / \n'\
          ' ___/ /  / /___/ / /___/ /_/ / /_/ / /___/ /|  /  \n'\
          '/____/  /_//____/_____/\____/\____/_____/_/ |_/   \n')
    parser = argparse.ArgumentParser(
        prog='syslogen', 
        usage='%(prog)s [options] -i input_file -c count')
    parser.add_argument(
        "-i", 
        "--input",
        help="File used to generate messages",
        action="store_true")
    parser.add_argument(
        "-c", 
        "--count", 
        help="Number of generated messages per second",
        action="store_true")
    args = parser.parse_args()
    if args.input and args.count:
        main(args.input, args.count)
    else:
        print("Not enough arguments, '--help' for more info")
        sys.exit(1)
