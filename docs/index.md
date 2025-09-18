# Axiom Void Project Documentation

Welcome to the comprehensive documentation for the Axiom Void project.

## Overview

The Axiom Void project is a cutting-edge initiative focused on building a **Sovereign AI Reasoning Engine**. It leverages a multi-language architecture to achieve hardware-agnostic performance, deterministic intelligence, and infinite extensibility.

### Core Components:

1.  **Axion-Core (Rust Universal AI Brain):**
    *   A production-grade, hardware-agnostic Rust core serving as the universal AI brain.
    *   Features a Hardware Abstraction Layer (HAL) for dynamic quantization and optimization across ARM, x86, and GPU architectures.
    *   Designed for high-performance, low-latency operations and modular extensibility.

2.  **Euclid-Zero Geometric Reasoning Engine (JavaScript/React):**
    *   A hardened and operational geometric reasoning engine integrated as a web-based UI.
    *   Demonstrates sequential reasoning, problem-solving objectives, a structured axiom library, and symbolic grounding.
    *   Provides intuitive visualization of abstract geometric concepts.

3.  **Python Control Plane:**
    *   Manages project configuration, core logic orchestration, and testing infrastructure.
    *   Features robust error handling, comprehensive logging, and modular design.

## Getting Started

Refer to the main [README.md](../README.md) for quick setup instructions and project overview.

## Development

This section details how to set up your development environment, run tests, and build the project components.

### 1. Clone the Repository

First, clone the Axiom Void repository from GitHub:

```bash
git clone https://github.com/devdollzai/-axiomhive-identity-ecosystem.git
cd -axiomhive-identity-ecosystem # Or your project's root directory
```

### 2. Python Development Environment

The Python control plane requires a virtual environment for dependency management.

```bash
# Navigate to the project root if not already there
# cd /path/to/axiom_void

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install pytest

# Set PYTHONPATH for module discovery
export PYTHONPATH=$PWD

# Run Python tests
pytest tests/
```

### 3. Rust Development Environment

The Axion-Core is built with Rust. Ensure you have Rust and Cargo installed (e.g., via `rustup`).

```bash
# Navigate to the axion-core directory
cd axion-core

# Build the Rust core
cargo build

# Run Rust tests
cargo test
```

### 4. JavaScript/React Development (Euclid-Zero Engine)

The Euclid-Zero engine is a single-file HTML/JavaScript application. It can be opened directly in a web browser.

```bash
# Open the Euclid-Zero engine in your browser
open docs/euclid_zero_engine.html # macOS
# or
# xdg-open docs/euclid_zero_engine.html # Linux
```

## Architecture

In-depth explanations of the multi-language architecture, component interactions, and design principles.

## Licensing & Monetization

Information regarding the AxiomHive Licensing Protocol (AHLP) and the Sovereign Compute Unit (SCU) model.
