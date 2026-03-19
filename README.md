# PsychoPy Template

A modular boilerplate for building psychological experiments in PsychoPy. The project is designed to separate **reusable experiment infrastructure** from **procedure-specific code**, so you can focus on implementing the logic of a new study without rewriting the same setup code each time.

## Key Features

- **YAML-based Configuration**: Store experiment parameters in `config.yaml`.
- **Automated Session Setup**: Built-in participant info dialog and shared timestamping for output files.
- **Robust Logging**: Automatic session logging, including monitor parameters and full configuration content.
- **Monitor & Timing Utilities**: Automatic screen resolution detection and optional frame rate validation.
- **Safe Exit Handling**: Emergency `F7` exit with automatic behavioral data saving on termination.
- **Instruction Helpers**: Present text, images, or numbered instruction sequences from the `messages/` folder.
- **BioSemi Trigger Support**: Trigger handling with dummy mode, trigger history, and CSV export of trigger maps.
- **Modular Architecture**: Shared code lives in `src/`, while experiment-specific logic belongs in `procedure_code/`.

## Project Structure

```text
├── main.py
├── config.yaml
├── README.md
├── messages/               # Instruction files (.txt, .png, etc.)
├── results/                # Output folder for CSV data and logs
├── src/                    # Reusable modules shared across experiments
│   ├── experiment_setup.py
│   ├── monitor_setup.py
│   ├── load_data.py
│   ├── exit_handler.py
│   ├── present_info.py
│   └── trigger_handler_biosemi.py
└── procedure_code/         # Experiment-specific code
    └── triggers_biosemi.py
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

1. Adjust `config.yaml` for your experiment settings.
2. Add instruction files to the `messages/` folder.
3. Implement your procedure-specific logic in `procedure_code/`.
4. Use `main.py` as the experiment entry point.
5. Run the experiment:
   ```bash
   python main.py
   ```

## Core Functions

- `load_config()`: Loads YAML configuration and logs its contents.
- `part_info()`: Collects participant information at session start.
- `create_monitor()`: Creates a PsychoPy monitor using config values and detected screen resolution.
- `get_frame_rate()`: Measures and validates display refresh rate.
- `present_text()`, `present_image()`, `present_sequence()`: Present instruction screens from files.
- `show_feedback()`: Displays accuracy-based feedback.
- `check_exit()`: Allows safe termination using `F7`.
- `register_save_beh_results()`: Saves behavioral results automatically on exit.
- `TriggerHandler`: Sends BioSemi triggers, stores trigger history, and exports trigger maps to CSV.

## License

This project is open-source and available under the [MIT License](LICENSE).