#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2018 January. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : gui-clock - Simple gui clock using python and tkinter
    Script Name  : utils.py
    License      : GNU General Public License v3.0


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

"""


def get_run_info(running_file_name):
    """
    This routine returns a tuple containing three things.
    1. Current Working Folder path
    2. Path of the scrip that is running
    3. Script Name
    """

    from inspect import currentframe, getframeinfo
    from pathlib import Path, PurePath
    import os

    curr_working_dir = PurePath(os.getcwd())
    if running_file_name is not None:
        script_name = PurePath(running_file_name)
        script_path = PurePath(Path(script_name).resolve().parent)
    else:
        script_name = PurePath(getframeinfo(currentframe()).filename)
        script_path = PurePath(Path(script_name).resolve().parent)

    return curr_working_dir, script_path, script_name

