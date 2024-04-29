import os
import subprocess
import curses
import time

def generate_keys(stdscr, key_count=500):
    # Clear screen and hide cursor
    curses.curs_set(0)
    stdscr.clear()
    
    # Prepare key directory
    datestamp = time.strftime("%Y%m%d_%H%M%S")
    key_dir = f"./ssh-keys-{datestamp}/"
    os.makedirs(key_dir, exist_ok=True)

    # Initialize variables for timing
    times = []

    for i in range(1, key_count + 1):
        key_name = f"id_rsa_MINED_{i}"
        full_key_path = os.path.join(key_dir, key_name)
        
        # Start time
        start_time = time.time()
        
        # Generate SSH key
        result = subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-f', full_key_path, '-N', ''],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # End time
        end_time = time.time()
        time_diff = end_time - start_time
        times.append(time_diff)

        # Calculate stats
        total_time = sum(times)
        avg_time = total_time / len(times)

        # Prepare output
        random_art_lines = result.stderr.split('\n')[-13:-1]  # Last lines include the randomart
        
        # Display randomart
        stdscr.move(0, 0)
        for line in random_art_lines:
            stdscr.addstr(line + '\n')
        
        # Display stats at the bottom
        status_message = f"Keys generated: {i}, Average Speed: {avg_time:.3f} s/key, Latest Speed: {time_diff:.3f} s/key"
        stdscr.move(curses.LINES - 1, 0)
        stdscr.clrtoeol()
        stdscr.addstr(status_message)
        stdscr.refresh()

def main():
    curses.wrapper(generate_keys)

if __name__ == "__main__":
    main()
