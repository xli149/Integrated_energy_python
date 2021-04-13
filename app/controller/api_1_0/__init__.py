from flask import Blueprint

Api = Blueprint("api_1_0", __name__)

from . import EnergyController
