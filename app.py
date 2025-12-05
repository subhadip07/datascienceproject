from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET']) ## route to display the home page
def homepage():
    return render_template("index.html")
