# Iris says!:cherry_blossom:  

### A minimalist platform for learning, understanding and realising Iris Flower Classification.
This is an **educational tool to encourage learning Iris Flower Classification** with inbuilt *graphical visualisations* and *on-spot prediction system*. We have loaded the platform with 7 highly optimized, pretrained models of different algorithms namely,  
- Decision Tree Classifier
- Gaussian Naive Bayes
- K-Neighbors Classifier
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine
- Multinomial Naive Bayes.  
> The architecture of the model are saved and are reused for **faster prediction.**  
<hr>  

### Algorithm :cherry_blossom:  
Due to continuous prediction calls, we devised a simple algorithm for **isolated prediction**.  
- Each time a user wants to predict with a particular model, the measurands along with the model key is sent to the server.
- The model is searched and when found, loaded as an object file with all the architecture expanded and ready for prediction.
- The expanded object takes in the measurands via the predict function. (The functions are stored within the object's architecture).
- Values are predicted and then return to the DOM.
- Then a javascript function call deletes all the prior data, to avoid unexpected object expansion errors during the process.
 
## To Get Started:cherry_blossom: 
### Production
```bash
git clone https://github.com/j0fiN/Iris-Says.git
cd Iris-Says
pip install -r requirements.txt
python run.py
```  
### Testing (algorithm test)
```bash
python -m unittest discover tests
```  
<hr>

## Learn it!:cherry_blossom:  
> A full description available about the **dataset and the models.**
<img src="https://github.com/j0fiN/Iris-Says/blob/master/iris/static/images/home_page_snap.PNG" alt="Home page" width="800" height="400">
<hr>  

## Interact with it!:cherry_blossom:  
> Loaded with major graphs which are useful and not very complex to grasp. **Simplicity had been maintained!**
<img src="https://github.com/j0fiN/Iris-Says/blob/master/iris/static/gif/graph_page_gif.gif" alt="GIF" width="800" height="400">
<hr>  

## Realise how it works!:cherry_blossom:  
> **With robust, yet flexible configurations**, users can select his own settings and get wonderful predictions.
<img src="https://github.com/j0fiN/Iris-Says/blob/master/iris/static/images/predict_page_snap.PNG" alt="Predict page" width="800" height="400">
<hr>  

## Major Reach:cherry_blossom:
This platform is majorily developed for **beginners in Data Analytics/Machine Learning**. Giving a strong foundation in these topics enhances them to move forward faster in this ever-growing field. They will understand how to approach any data and analyze them and then use it to build powerful machine learning models.  
The platform can play a major part in **showcasing AI and machine learning for students in high schools and other bootcamps**.  

## Higher Optimizations:cherry_blossom:
- The tool can **grow in size** to explore various other famous datasets and the usage of machine learning in each of them and not only iris(A good example would be Boston says!).  
- The tool can become a platform for users to **develop their own models on that dataset and upload them**. They can also write content about the database.
- The Graphical visualisations can be **enhanced** using various tools of javascript.

## Tools used to develop the project:cherry_blossom:
- Flask (Python)
- Scikit-Learn (Python)
- Plotly-Express (Python)
- Basic webtools(HTML, CSS, JS(some JQuery too!))

## Contribution:cherry_blossom: 
Do contribute if you have ideas, **:star: the repo** if you find it impressive!  
 
> Made with :heart: => **PYTHON**
