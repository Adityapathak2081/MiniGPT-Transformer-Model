# MiniGPT-Transformer-Model
This is a ML based project. I've created this ML model that is similar to ChatGPT, but my pre trained model is focused solely to mental health support. This limitation is due to lack of extensive GPU facility that is required in order to build an advanced level GPT system.
I've distributed the dataset into training and testing sets. When model is trained with the actual dataset(80%), then the loss function in each epoch keeps reducing and forms a hyperparabolic curve and ends up minimising the cost.
The testing dataset is used when model is showing overfitting which actually happened while building this project.
The LLM gives predictions with an accuracy of 0.792 (R^2).
