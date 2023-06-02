import logging

# set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# handler = logging.FileHandler("extension.log")
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)


def sanitize_text(text):
    import re
    return re.sub(r"[\"${}]", "",text)