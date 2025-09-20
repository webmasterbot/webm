from flask import Flask, render_template
from bot import v2
import tracemalloc, asyncio,  os, logging

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode="w")
logger = logging.getLogger(__name__)
logger.info("Log started")

app = Flask(__name__)

asyncio.run(v2.startFromFlask())


@app.route('/')
def main():
	return render_template("main.html", botStatus=status)

