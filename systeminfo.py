import platform
import psutil
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

def get_system_info():
    system_info = {}

    # Platform information
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    # CPU information
    system_info['Physical Cores'] = str(psutil.cpu_count(logical=False))
    system_info['Total Cores'] = str(psutil.cpu_count(logical=True))
    cpu_freq = psutil.cpu_freq()
    system_info['Max Frequency'] = f"{cpu_freq.max}Mhz"
    system_info['Min Frequency'] = f"{cpu_freq.min}Mhz"
    system_info['Current Frequency'] = f"{cpu_freq.current}Mhz"
    system_info['CPU Usage Per Core'] = [str(percent) for percent in psutil.cpu_percent(percpu=True)]

    # Memory information
    mem = psutil.virtual_memory()
    system_info['Total Memory'] = f"{mem.total // (1024 ** 3)}GB"
    system_info['Available Memory'] = f"{mem.available // (1024 ** 3)}GB"
    system_info['Used Memory'] = f"{mem.used // (1024 ** 3)}GB"
    system_info['Memory Percentage'] = f"{mem.percent}%"

    # Disk information
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            system_info[f"Drive {partition.mountpoint} Total Size"] = f"{partition_usage.total // (1024 ** 3)}GB"
            system_info[f"Drive {partition.mountpoint} Used"] = f"{partition_usage.used // (1024 ** 3)}GB"
            system_info[f"Drive {partition.mountpoint} Free"] = f"{partition_usage.free // (1024 ** 3)}GB"
            system_info[f"Drive {partition.mountpoint} Percentage"] = f"{partition_usage.percent}%"
        except PermissionError:
            continue

    return system_info

if __name__ == "__main__":
    system_info = get_system_info()
    for key, value in system_info.items():
        key_output = Fore.CYAN + key + Style.RESET_ALL
        value_output = Fore.GREEN + str(value) + Style.RESET_ALL
        print(f"{key_output}: {value_output}")
