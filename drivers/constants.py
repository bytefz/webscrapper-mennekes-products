# Constants for paths
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)

# Path Executable
EXEC_PATH = BASE_DIR/"executables"


# Path Drivers: Firefox
FIREFOX_DRIVER_DIR_LINUX = EXEC_PATH/"linux"
FIREFOX_DRIVER_DIR_WINDOWS = EXEC_PATH/"windows"

FIREFOX_DRIVER_LINUX = FIREFOX_DRIVER_DIR_LINUX/"geckodriver"
FIREFOX_DRIVER_WINDOWS = FIREFOX_DRIVER_DIR_WINDOWS/"geckodriver.exe"

# Windows Path
CHROME_DRIVER_DIR_LINUX = EXEC_PATH/"linux"
CHROME_DRIVER_DIR_WINDOWS = EXEC_PATH/"windows"

CHROME_DRIVER_LINUX = CHROME_DRIVER_DIR_LINUX/"chromedriver"
CHROME_DRIVER_WINDOWS = CHROME_DRIVER_DIR_WINDOWS/"chromedriver.exe"