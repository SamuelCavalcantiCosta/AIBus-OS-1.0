# Contributing to AIBus-OS

Thank you for your interest in contributing to the AIBus-OS project! This guide will help you get started with contributing to our open-source autonomous bus system.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue tracker to avoid duplicates. When creating a bug report, include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Describe the behavior you observed and why it is a problem
- Include screenshots or videos if possible
- Include system information (OS, hardware, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful to the project
- Include examples of how the feature would work
- Specify which component(s) it would affect

### Pull Requests

- Fill in the required template
- Follow the coding style guidelines
- Include appropriate tests
- Update documentation for any changed functionality
- Ensure all tests pass before submitting

## Development Process

### Setting Up the Development Environment

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/AIBus-OS.git`
3. Set up upstream remote: `git remote add upstream https://github.com/SamuelCavalcantiCosta/AIBus-OS.git`
4. Install dependencies: `pip install -r requirements.txt`
5. Install pre-commit hooks: `pre-commit install`

### Branching Strategy

- `main` - Latest stable release
- `develop` - Current development branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `release/*` - Release preparation branches

Always create your working branches from `develop`.

### Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use descriptive variable and function names
- Write docstrings for all public functions, classes, and modules
- Keep functions focused on a single responsibility
- Add type hints to function parameters and return values
- Write unit tests for new functionality

### Testing

All code changes should be accompanied by appropriate tests:

- Unit tests for individual components
- Integration tests for component interactions
- Simulation tests for system-level behavior

Run tests with: `pytest tests/`

### Documentation

Update documentation for any changes you make:

- Update docstrings for modified code
- Update relevant `docs/` files
- Add examples for new functionality
- Update architecture diagrams if needed

## Contribution Areas

We welcome contributions in various areas:

### Perception System

- Sensor processing algorithms
- Object detection and tracking
- Sensor fusion techniques
- Localization improvements

### Decision Making

- Path planning algorithms
- Behavior prediction models
- Traffic rule compliance
- Edge case handling

### Control Systems

- Smoother control algorithms
- Fault-tolerant control
- Passenger comfort optimization
- Energy efficiency

### Infrastructure Integration

- V2X communication protocols
- Smart city integration
- Fleet management
- Public transit coordination

### Safety

- Safety case development
- Fault detection and handling
- Safety validation methods
- Regulatory compliance

### Simulation

- More realistic environments
- Automated testing scenarios
- Performance benchmarks
- Hardware-in-the-loop testing

### Documentation

- User guides
- Developer documentation
- Architecture documentation
- Installation guides

## Review Process

All submissions go through a review process:

1. Automated checks (linting, tests, etc.)
2. Code review by at least one maintainer
3. Additional reviews for safety-critical components
4. Final approval and merge

## Recognition

All contributors will be recognized in our [CONTRIBUTORS.md](CONTRIBUTORS.md) file. Significant contributions may be highlighted in release notes and on the project website.

## Questions?

If you have any questions, feel free to:

- Open an issue with your question
- Contact the maintainers directly
- Join our community discussion forums

Thank you for contributing to AIBus-OS!