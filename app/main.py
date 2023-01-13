import pickle
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load the trained model
iris_classifier = pickle.load(open('iris_classifier.pkl', 'rb'))
iris_classes = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']


class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(data: IrisData):
    """This function predicts the iris flower class.

    Args:

        data (IrisData): 
            sepal_length: float
            sepal_width: float
            petal_length: float
            petal_width: float

    Returns:

        result:
            class: int
            class_name: string
    """

    datas = [data.sepal_length, data.sepal_width,
             data.petal_length, data.petal_width]
    # Make a prediction using the model
    prediction = int(iris_classifier.predict([datas])[0])
    result = {"class": prediction, "class_name": iris_classes[prediction]}
    return result
