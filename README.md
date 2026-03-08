# Retirement Timer

A simple retirement calculator that estimates years to financial independence based on your savings and spending.

## How It Works

The calculator uses two key assumptions:
- **7% annual growth rate** on investments
- **4% safe withdrawal rate** (your target = annual spending / 0.04)

## Installation

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
make install
```

## Usage

```bash
make run
```

Enter your:
- **Current Savings** - Total invested assets
- **Annual Savings** - How much you save per year
- **Annual Spending** - Your yearly expenses

The calculator will show years until you reach your target retirement number.

## Development

```bash
# Run tests
make test

# Lint and type check
make check

# Format code
make format
```

## Building

```bash
# macOS
make build-mac-arm64
make build-mac-intel

# Windows
make build-windows
```

Built executables are placed in the `dist/` directory.
