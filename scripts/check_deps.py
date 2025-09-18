#!/usr/bin/env python3
import subprocess
import sys
import os

def check_python_deps():
    """Check if Python dependencies are installed."""
    required_packages = [
        "fastapi",
        "uvicorn",
        "pydantic",
        "pytest",
        "prometheus_client",
        "requests",
        "numpy",
        "graphviz",
        "flake8"
    ]
    missing = []
    for pkg in required_packages:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"[FAILURE ALERT] Missing Python dependencies: {', '.join(missing)}")
        return False
    print("All Python dependencies are installed.")
    return True

def check_node_deps():
    """Check if Node dependencies are installed."""
    frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
    if os.path.exists(os.path.join(frontend_dir, ".pnp.cjs")):
        print("All Node dependencies are installed.")
        return True
    else:
        print("[FAILURE ALERT] Node dependencies not installed. Run yarn install in frontend directory.")
        return False

if __name__ == "__main__":
    python_ok = check_python_deps()
    node_ok = check_node_deps()
    if not python_ok or not node_ok:
        sys.exit(1)
    print("[PROTOCOL STATUS: OK] Dependencies verified.")
