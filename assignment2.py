#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Summer 2026
Program: assignment2.py
Author: Ssingh1488

The Python code in this file is original work written by Aakash.
No code in this file is copied from any other source except those
provided by the course instructor.

Description:
Memory Visualiser - Milestone 1

Date: July 2026
'''

import argparse
import os
import sys


def parse_command_args() -> object:
    """Set up argparse here. Call this function inside main."""
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )

    parser.add_argument(
        "program",
        type=str,
        nargs="?",
        help="if a program is specified, show memory use of all associated processes. Show only total use if not."
    )

    return parser.parse_args()


def percent_to_graph(percent: float, length: int = 20) -> str:
    """Turn a percent (0.0-1.0) into a bar graph."""
    filled = round(percent * length)
    empty = length - filled
    return "#" * filled + " " * empty


def get_sys_mem() -> int:
    """Return total system memory in KiB."""
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])
    return 0


def get_avail_mem() -> int:
    """Return available system memory in KiB."""
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])
    return 0


def pids_of_prog(app_name: str) -> list:
    """Milestone 2"""
    pass


def rss_mem_of_pid(proc_id: str) -> int:
    """Milestone 2"""
    pass


def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """Convert KiB into human-readable format."""
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suf_count = 0
    result = kibibytes

    while result > 1024 and suf_count < len(suffixes) - 1:
        result /= 1024
        suf_count += 1

    return f"{result:.{decimal_places}f} {suffixes[suf_count]}"


if __name__ == "__main__":
    args = parse_command_args()

    if not args.program:
        pass
    else:
        pass
