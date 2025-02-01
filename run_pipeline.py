import subprocess
import sys

def run_script(script_name):
    try:
        print(f"Running {script_name}...")
        result = subprocess.run(["python", script_name], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e.stderr}")
        sys.exit(1)

def main():
    run_script("main.py")
    run_script("parser.py")
    run_script("load-info.py")
    print("Workflow completed successfully!")

if __name__ == "__main__":
    main()
