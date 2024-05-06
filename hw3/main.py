
import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    """
    Parses a log line and returns a dictionary containing the date/time, level, and message.

    Args:
        line (str): The log line to be parsed.

    Returns:
        dict: A dictionary containing the parsed log information with the following keys:
            - 'date_time': The date and time of the log entry.
            - 'level': The log level.
            - 'message': The log message.
    """
    parts = line.split(" ", 2)

    return {
        'date_time': parts[0] + ' ' + parts[1],
        'level': parts[2].split(" ", 1)[0],
        'message': parts[2].split(" ", 1)[1]
    }

def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r') as file:
        logs = [parse_log_line(line.strip()) for line in file]
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()] # Filter logs by level

def count_logs_by_level(logs: list) -> dict:
    count = Counter(log['level'] for log in logs) # Count the logs by level
    return count

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

def main():
    """
    The main function of the program.
    
    This function is responsible for loading logs from a file, counting logs by level,
    and displaying the log counts. If a log level is provided as a command-line argument,
    it also filters and displays the logs for that level.
    
    Usage: python main.py path/to/logfile.log [log_level]
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/logfile.log [log_level]")
        return
    
    file_path = sys.argv[1] # Path to the log file
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None # Optional log level filter
    
    try:
        logs = load_logs(file_path)
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)
        
        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level)
            print(f"\nДеталі логів рівня '{log_level}':")
            for log in filtered_logs:
                print(f"{log['date_time']} - {log['message']}")
    
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
