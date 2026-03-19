# PsychoPy Template

A robust, modular boilerplate for building psychological experiments in PsychoPy. This skeleton provides a standardized structure for session management, hardware configuration, and data logging, allowing you to focus on the core logic of your experiment.

## Key Features

- **YAML-based Configuration**: Manage all experiment parameters (colors, timings, keys) in a single `config.yaml` file.
- **Automated Session Management**: Integrated participant info dialogs and shared timestamps for all output files.
- **Robust Logging**: Automatic logging of session events, monitor parameters, and full configuration content for perfect reproducibility.
- **Monitor & Hardware Setup**: Automatic screen resolution detection and easy custom monitor profile configuration.
- **Safe Exit Handling**: Global `F7` emergency exit that ensures data is saved even if the experiment is interrupted.
- **Instruction Helpers**: Flexible functions to present text, images, or numbered sequences of instructions.
- **Data Export**: Automatic CSV saving of behavioral results with error handling.

## Project Structure

```text
├── main.py                 # Entry point of the experiment
├── config.yaml             # Global configuration parameters
├── messages/               # Folder for instruction files (.txt, .png, etc.)
├── results/                # Output folder for CSV data and logs
└── src/                    # Source code modules
    ├── experiment_setup.py # Participant info and logging initialization
    ├── monitor_setup.py    # Monitor profiles and resolution detection
    ├── load_data.py        # YAML loading and text file processing
    ├── exit_handler.py     # Emergency exit and data saving logic
    └── present_info.py     # Stimulus drawing and instruction screens
```

## Getting Started

### Prerequisites

- Python 3.8+
- PsychoPy
- PyYAML

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ociepkam/psychopy-template.git
   ```
2. Install dependencies:
   ```bash
   pip install psychopy pyyaml
   ```

### Usage

1. Modify `config.yaml` to suit your experiment's needs.
2. Add your instruction files to the `messages/` folder.
3. Implement your trial logic in `main.py` using the provided helpers.
4. Run the experiment:
   ```bash
   python main.py
   ```

## Core Functions

- `present_sequence()`: Automatically displays `instr_1.txt`, `instr_2.txt`, etc.
- `check_exit()`: Call this inside your loops to allow the participant to exit via `F7`.
- `show_feedback()`: Display accuracy-based feedback using dictionary mapping from config.
- `draw_stim()`: A recursive helper to toggle `autoDraw` for single stimuli, lists, or dictionaries.

## License

This project is open-source and available under the [MIT License](LICENSE).
```