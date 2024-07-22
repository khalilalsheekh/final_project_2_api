import logging


class LoggingSetup:
    """
    this function is to call the setUp in every page rather the building it everytime.
    """
    logging.basicConfig(filename='../final_project_2.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')
