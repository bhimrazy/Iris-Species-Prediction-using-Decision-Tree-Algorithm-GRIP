<p align="center">
<a href="" rel="noopener">
<img src="https://user-images.githubusercontent.com/46085301/212309825-fb31ef54-8b2d-4907-a39d-59e479234797.png" height="100" width="100"/>
<a/>
<br>
<a href="" rel="noopener">
 <img src="https://user-images.githubusercontent.com/46085301/212293448-4a4694ed-635a-4023-800b-636de8477bf9.png" alt="TSF | Graduate Rotational Internship Program "></a>
</p>
<h2 align="center">Iris Species Prediction using Decision Trees | The Sparks Foundation: GRIP</h2>

---

## 📝 Table of Contents
- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Deployment](#deployment)
- [Author](#author)

## 🧐 Problem Statement <a name = "problem_statement"></a>
- Create the Decision Tree classifier and visualize it graphically.
  The purpose is if we feed any new data to this classifier, it would be able to
  predict the right class accordingly.
  
  Dataset : https://bit.ly/3kXTdox

  Sample Solution : https://bit.ly/2G6sYx9
  
## 💡 Idea / Solution <a name = "idea"></a>
<p align="left"> Iris Species Prediction using Decision Tree Algorithm is a machine learning task of classifying the species of Iris flowers based on their physical characteristics. This task involves training a Decision Tree model on the Iris dataset, which includes measurements of sepal length, sepal width, petal length, and petal width for 150 Iris flowers of three different species: Iris setosa, Iris virginica, and Iris versicolor. The trained model is then used to predict the species of new, unseen Iris flowers based on their measurements.
    <br> 
</p>
To create a model to classify the Iris dataset, the following tasks were performed:
For more detail, please chekout the 

[Notebook](/Prediction%20using%20Decision%20Tree%20Algorithm.ipynb)

### Data Preparation
![image](https://user-images.githubusercontent.com/46085301/212305130-abc63824-7726-4f2b-9f27-62a178114157.png)

### Data Visualization
![image](https://user-images.githubusercontent.com/46085301/212305229-0aadbaff-c901-4a34-b8e3-99cbd3733e43.png)

![image](https://user-images.githubusercontent.com/46085301/212305272-5fdfd34b-e035-4152-9022-ffbd3ed17efb.png)

![image](https://user-images.githubusercontent.com/46085301/212305186-5d1d4511-ccd8-4150-a81e-10561d9a8623.png)

### Model Training
![image](https://user-images.githubusercontent.com/46085301/212306136-45ce3a19-7c13-4fa9-a112-24379a4cdc43.png)

### Evaluating Model
![image](https://user-images.githubusercontent.com/46085301/212305512-2ab831db-308b-4d80-b092-df5aeb8fa674.png)

![image](https://user-images.githubusercontent.com/46085301/212305540-1a0c09f1-0609-4b54-aed2-1c3be1ef754f.png)

![image](https://user-images.githubusercontent.com/46085301/212305625-97c88c38-bc9a-4bbf-92d7-08052be63903.png)

### Visualizing and Saving the model
![image](https://user-images.githubusercontent.com/46085301/212305418-2ab6065a-5d16-446a-847d-afa8a995e7ea.png)

![image](https://user-images.githubusercontent.com/46085301/212305826-16ce2b59-3c45-4930-9d13-e1867b2974a5.png)

## 🎈 Usage <a name="usage"></a>
Run my Project

```bash
  git clone https://github.com/bhimrazy/Iris-Species-Prediction-using-Decision-Tree-Algorithm-GRIP.git
  cd Iris-Species-Prediction-using-Decision-Tree-Algorithm-GRIP/app
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  uvicorn main:app 
```
## ⛏️ Built With <a name = "tech_stack"></a>
- [scikit-learn](https://scikit-learn.org/) - Machine Learning Library
- [Pandas](https://pandas.pydata.org/) - Python Data Analysis Library
- [Matplotlib](https://matplotlib.org/) - Visualization with Python
- [Seaborn](https://seaborn.pydata.org/) - Statistical Data Visualization
- [FastAPI](https://fastapi.tiangolo.com/)- Python Web Framework for building APIs

## 🎉 Deployment <a name = "deployment"></a>
[![Deployment of Iris Classifier](https://user-images.githubusercontent.com/46085301/212294874-329be9b4-80b6-4364-8ebe-58c972fc0cee.png)](https://iris-classifier-production.up.railway.app)

## ✍️ Author <a name = "author"></a>
- [@bhimrazy](https://github.com/bhimrazy)

