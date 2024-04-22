from vetiver import VetiverModel, VetiverAPI
from dotenv import load_dotenv, find_dotenv
import pins
import uvicorn 

load_dotenv(find_dotenv())

b = pins.board_folder('project/data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240408T094437Z-a6f9b')

app = VetiverAPI(v, check_prototype = True)
app.run(port = 8080)

