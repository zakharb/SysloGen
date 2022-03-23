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
        Main module for ZLOG

    Author:
        Bengart Zakhar
"""

import os
import random

from time import sleep
from datetime import datetime
from datetime import timedelta 

class Syslogen():
    def __init__(self, output_file, input_file, count):
        self.output_file = output_file
        self.input_file = input_file
        self.count = count

    def append_file(self):
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
        t1 = datetime.now()
        send_mes = 0
        sum_mes = 0
        while True:
            message = lines[random.randrange(0, len(lines) - 1)]
            with open(self.output_file, 'a+') as f:
                f.write(message)
            t2 = datetime.now()
            if t2 - t1 > timedelta(seconds=1):
                sum_mes += send_mes
                print('{} Messages writen: {}, total {}'.format(t2, send_mes, sum_mes))
                t1 = datetime.now()
                send_mes = 0
            send_mes += 1
            sleep(1/self.count)

def main(output_file, input_file, count):
    generator = Syslogen(output_file, input_file, count)
    generator.append_file()
