#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path


def main():
    root_dir = Path(__file__).parent
    day_dirs = sorted([d for d in root_dir.iterdir() if d.is_dir() and d.name.startswith("day-")])
    
    if not day_dirs:
        sys.exit(1)
    
    print(f"Found {len(day_dirs)} days to test")
    
    failed_days = []
    passed_days = []
    for day_dir in day_dirs:
        print(f"Running {day_dir.name}...", end=" ", flush=True)

        env = os.environ.copy()
        env["SKIP_INPUT"] = "1"
        
        try:
            result = subprocess.run(
                ["uv", "run", "main.py"],
                cwd=day_dir,
                env=env,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print("✅ PASSED")
                passed_days.append(day_dir.name)
            else:
                print("❌ FAILED")
                print(f"  stdout: {result.stdout}")
                print(f"  stderr: {result.stderr}")
                failed_days.append(day_dir.name)
                
        except subprocess.TimeoutExpired:
            print("❌ TIMEOUT")
            failed_days.append(day_dir.name)
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed_days.append(day_dir.name)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"✅ Passed: {len(passed_days)}")
    print(f"❌ Failed: {len(failed_days)}")
    
    if failed_days:
        print(f"\nFailed days: {', '.join(failed_days)}")
        sys.exit(1)
    else:
        print("\nAll tests passed")
        sys.exit(0)


if __name__ == "__main__":
    main()
