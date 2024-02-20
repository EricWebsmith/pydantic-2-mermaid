# Changelog

This file documents all notable changes to this project.

## [x.x.x] - TBD
### Changed
- use strict mypy

## [0.6.0] - 2024-01-14

### Changed
- Support typing.Literal
- Support type redefine in subclasses
- Support for Relations arguments in argparse

## [0.5.3] - 2023-12-10

### Changed
- Add CLI parameter check.
- Restore class by order in a list instead of using dict keys.
- Push test case coverage to 100%.
- Use `ruff` to lint project.
- Refactor charts comparing in unit test.

## [0.5.2] - 2023-11-26

### Changed
- Downgrade requirement from python 3.8.1 to python 3.8

## [0.5.0] - 2023-11-25

### Changed
- Downgrade requirement from python 3.10 to python 3.8.1

## [0.4.0] - 2023-07-30

### Changed
- Support inheritance in command line.
- Exact pydantic parser.

## [0.3.0] - 2023-07-30

### Changed
- Split into two projects, supporting pydantic 1 and 2.
- `generate_chart` now only accepts name parameters.

## [0.2.0] - 2023-03-20

### Added
- Command-line interface for improved usability.
- Inheritance handling: classes now hide properties inherited from parent classes.

### Changed
- Modified the codebase to support Python 3.7, increasing compatibility with older Python versions.

## [0.1.0] - 2023-03-18

### Added
- Initial release of the project, featuring core functionality for generating Mermaid charts from Pydantic models.
