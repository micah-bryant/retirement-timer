#!/usr/bin/env python3
"""Retirement Calculator - Calculate years to financial independence.

This is the main entry point for the Retirement Calculator GUI application.
It calculates years to retirement based on current savings, annual savings,
and annual spending using a 7% growth rate and 4% safe withdrawal rate.

Usage:
    python main.py
    # or
    make run
"""

from src.gui import run_app


def main() -> None:
    """Launch the Retirement Calculator GUI application."""
    run_app()


if __name__ == "__main__":
    main()
