# ntroduction

I love cats! They are my favorite animals in the entire world. Because of this big love, I have watched a lot of videos about cat's health. And a lot of them said cats are very suspicious about what kind of water we put for them to drink.

# Goals

The objective of this model is to determine if the water meets the criteria for safe consumption by living beings.

# Methodology

The model was analyzed using pandas. It was imbalanced and had many missing values. So, oversampling was applied, and a pipeline for imputing missing values and standardizing the data was used.

For model training, I selected classification models.

The primary metric was accuracy, with a target score of over 70%.

To compare and record the training, the MLflow API was used.

# Results

The models are simple, but Random Forest was able to achieve a prediction accuracy of around 80%.

![](video.gif)