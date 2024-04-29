import os
import subprocess
import curses
import time

def generate_keys(stdscr, key_count=500):
    """
    Function to generate SSH keys and display their randomart images using curses for real-time UI updates.

    Parameters:
    stdscr (curses.window): The default window object used by curses which represents the whole screen.
    key_count (int): The number of SSH keys to generate.

    The stdscr window is used extensively here to manage real-time display updates.
    """

    # Initially, clear the screen and hide the cursor to prepare for a clean UI output.
    curses.curs_set(0)
    stdscr.clear()

    # Prepare the directory where the keys will be stored with a unique timestamp.
    datestamp = time.strftime("%Y%m%d_%H%M%S")
    key_dir = f"./ssh-keys-{datestamp}/"
    os.makedirs(key_dir, exist_ok=True)  # Ensure the directory exists.

    # Initialize a list to keep track of the time taken for each key generation.
    times = []

    for i in range(1, key_count + 1):
        key_name = f"id_rsa_MINED_{i}"
        full_key_path = os.path.join(key_dir, key_name)

        # Record the start time of the key generation process.
        start_time = time.time()

        # Generate the SSH key using subprocess to call ssh-keygen.
        result = subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-f', full_key_path, '-N', ''],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Record the end time immediately after the key generation finishes.
        end_time = time.time()
        time_diff = end_time - start_time
        times.append(time_diff)

        # Calculate cumulative statistics: total time and average time per key generation.
        total_time = sum(times)
        avg_time = total_time / len(times)

        # Extract the randomart from the standard output of the subprocess call.
        random_art_lines = result.stdout.split('\n')[-13:-1]

        # Use stdscr to move the cursor to the top of the screen and display each line of the randomart.
        stdscr.move(0, 0)
        for line in random_art_lines:
            stdscr.addstr(line + '\n')

        # Move the cursor to the last line of the terminal to display status information about the process.
        # This ensures it doesn't scroll with the randomart display.
        stdscr.move(curses.LINES - 1, 0)
        stdscr.clrtoeol()  # Clear anything previously on this line to avoid display artifacts.
        status_message = f"Keys generated: {i}, Average Speed: {avg_time:.3f} s/key, Latest Speed: {time_diff:.3f} s/key"
        stdscr.addstr(status_message)
        stdscr.refresh()  # Refresh the screen to show the updated info.

def main():
    """
    Main function to handle the curses screen setup and run the key generation function.
    The curses.wrapper is a high-level routine that initializes curses and calls another function, handling exceptions and cleanup actions.
    """
    curses.wrapper(generate_keys)

if __name__ == "__main__":
    main()
