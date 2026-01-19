## Escape The Castle


## Overview
A multi-path interactive story game in Python using branch decision trees, modular multi-file structure, and dynamic randomized events. This game features user-input handling, 
clear state transitions, and a terminal-based interface that takes players on a narrative journey filled with meaningful choices and multiple outcomes. 

## Installation
### Requirements
- Python 3.8 or higher
- Command-line / terminal access
- No third-party libraries required


## Usage
### File Responsibilities 
#### escape.py
- Contains all game states
- No executable top-level code
- Each function represents a node in the state graph
- Transitions occur through explicit function calls
#### final.py
- Serves as the program entry point
- Handles user readiness and startup flow
- Imports and invokes Escape_From_The_Castle()
- Protected by if __name__ == "__main__" guard

### Mechanics
#### Input Handling
- All player input is normalized using .lower(), validated against known options, and re-prompted on invalid entry. This ensures valid state transitions and predictable program behavior.
#### State Design
- Each situation_ function describes the current narrative state, presents valid player options, validates user input using a while True loop, and transitions explicitly to the
next state.
#### Randomization
- Uses Python's built in random module to increase replayability and to avoid guranteed outcomes for the "narratively unsafe" choices
#### Error Prevention
- Infinite loops are intentionally used for input validation only
- Narrative dead-ends are explicit and intentional
- Execution logic is isolated from importable modules
- Naming conventions enforce predictable flow
## Authors and acknowledgment
VezioK


