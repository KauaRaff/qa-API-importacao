import logging
import os

#garantir log, salvando em logs/app.log
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | [%(levelname)s] | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding= "utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("api_importacao")