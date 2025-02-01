import subprocess

def run_script(script_name):
    """Run a Python script and check for errors."""
    try:
        print(f"Running {script_name}...")
        result = subprocess.run(["python", script_name], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e.stderr}")
        exit(1)

def main():
    # Step 1: Fetch tweets
    run_script("main.py")

    # Step 2: Parse and extract contract addresses
    run_script("parser.py")

    # Step 3: Fetch token info using GMGN API
    run_script("load-info.py")

    print("Workflow completed successfully!")

if __name__ == "__main__":
    main()
