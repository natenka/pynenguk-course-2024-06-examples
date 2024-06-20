
import logging

logging.basicConfig(
    # filename="log_01.log",
    level=logging.DEBUG,
    style="{",
    format="{asctime} {name} {levelname:20} {lineno} {funcName} {message}"
)




logging.warning("MSG WARN")
