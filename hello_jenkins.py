import os
import platform
from datetime import datetime
def main():
    print("Welcome to jenkins and docker setup")
    print("=" * 60)
    print("JENKINS PYTHON CI TEST")
    print("=" * 60)
    print(f"Python version : {platform.python_version()}")
    print(f"Operating system: {platform.system()}")
    print(f"Build number   : {os.getenv('BUILD_NUMBER', 'Not available')}")
    print(f"Job name       : {os.getenv('JOB_NAME', 'Not available')}")
    print(f"Build URL      : {os.getenv('BUILD_URL', 'Not available')}")
    print(f"Job URL        : {os.getenv('JOB_URL', 'Not available')}")
    print(f"Run URL        : {os.getenv('RUN_DISPLAY_URL', 'Not available')}")
    print(f"Time           : {datetime.now()}")
    print("\nJenkins is running this Python script successfully!")
    print("Connection is success")
    
if __name__ == "__main__":
    main()
