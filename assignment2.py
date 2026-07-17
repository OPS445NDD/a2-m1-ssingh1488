def percent_to_graph(percent, total_chars):
    """Convert a percentage between 0.0 and 1.0 into a bar graph."""
    hash_count = int(percent * total_chars)
    space_count = total_chars - hash_count

    return "#" * hash_count + " " * space_count


def get_sys_mem():
    """Return total system memory in kilobytes."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])

    return 0


def get_avail_mem():
    """Return available system memory in kilobytes."""
    mem_free = 0
    swap_free = 0

    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])

            if line.startswith("MemFree:"):
                mem_free = int(line.split()[1])

            if line.startswith("SwapFree:"):
                swap_free = int(line.split()[1])

    return mem_free + swap_free
