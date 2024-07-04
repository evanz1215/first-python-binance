import os
from binance.client import Client
import pandas as pd
import datetime
from matplotlib import pyplot as plt
from dotenv import load_dotenv


load_dotenv()

my_API_Key = os.getenv("BINANCE_API_KEY")
my_API_Secret = os.getenv("BINANCE_API_SECRET")


API_Key = my_API_Key
API_Secret = my_API_Secret

client = Client(API_Key, API_Secret)

print(client.get_exchange_info())
