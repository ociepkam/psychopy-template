import time
from psychopy import visual, event, core

from src.experiment_setup import part_info, init_logging
from src.monitor_setup import create_monitor
from src.load_data import load_config
from src.exit_handler import register_save_beh_results



def main():
    session_time = time.strftime("%Y_%m_%d_%H_%M", time.gmtime())
    results_beh = []

    info, part_id = part_info()

    init_logging(part_id=part_id, timestamp=session_time)
    register_save_beh_results(results=results_beh, part_id=part_id, timestamp=session_time)

    config = load_config()
    win = visual.Window(fullscr=True,
                        monitor=create_monitor(config),
                        units='pix',
                        screen=0,
                        color=config["screen_color"])

    mouse = event.Mouse(visible=False)
    clock = core.Clock()


if __name__ == '__main__':
    main()