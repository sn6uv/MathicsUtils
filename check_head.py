# -*- coding: utf8 -*-

u"""
    Mathics: a general-purpose computer algebra system
    Copyright (C) 2011-2013 The Mathics Team

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys

head_pattern = [
    '# -*- coding: utf8 -*-',
    '',
    'u"""',
    '    Mathics: a general-purpose computer algebra system',
    '    Copyright (C) 2011-2013 The Mathics Team',
    '',
    '    This program is free software: you can redistribute it and/or modify',
    '    it under the terms of the GNU General Public License as published by',
    '    the Free Software Foundation, either version 3 of the License, or',
    '    (at your option) any later version.',
    '',
    '    This program is distributed in the hope that it will be useful,',
    '    but WITHOUT ANY WARRANTY; without even the implied warranty of',
    '    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the',
    '    GNU General Public License for more details.',
    '',
    '    You should have received a copy of the GNU General Public License',
    '    along with this program.  If not, see <http://www.gnu.org/licenses/>.',
    '"""',
    '']

def main(mathics_path):
    pyfiles = []
    for root, dirs, files in os.walk(mathics_path):
        for file in files:
            if file.endswith('.py'):
                pyfiles.append(os.path.join(root, file))

    offending_files = []
    for file in pyfiles:
        with open(file, 'r') as f:
            head = [f.readline()[:-1] for i in xrange(20)]
            if head != head_pattern:
                offending_files.append(file)

    for file in offending_files:
        if raw_input("{0}: [y]/n? ".format(file)).lower() in ('y', ''):
            with open(file, 'r+') as f:
                old = f.read()
                f.seek(0)
                f.write('\n'.join(head_pattern + [old]))
            

def print_usage():
    print 'USAGE: check_head.py path_to_mathics/\n'
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()

    mathics_path = sys.argv[1]

    if not os.path.isdir(mathics_path):
        print_usage()

    main(mathics_path)
