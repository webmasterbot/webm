from flask import Flask, render_template
try:
	import os, discord, tracemalloc, time, datetime
	from discord.ext import commands
	from dotenv import load_dotenv
	status = "Succeeded"
except Exception as inst:
	status = f"An error occured: \n {str(type(inst))} \n {inst}"

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("main.html", botStatus=status)

