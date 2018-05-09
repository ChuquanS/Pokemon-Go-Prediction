# Pokemon-Go-Prediction
2018 Spring 

## Purpose
A statistical model using machine learning to predict the winner pokemon for each combat. The final model will also allow players to choose proper pokemon to improve their win rate

## The Data
Our data came from Kaggle datasets (https://www.kaggle.com/datasets), including “Pokemon with stats” datasets ( https://www.kaggle.com/abcsds/pokemon/data ) and “Pokemon-Weedle’s Cave” datasets ( https://www.kaggle.com/terminus7/pokemon-challenge/data ).

## Processing Data

### Data Source Combination
After comparing the sources of pokemon basic datasets from “Pokemon with stats” and “Pokemon-Weedle’s Cave”, we decided to combine the two main datasets with the “Total” factor deleted since the values in “Total” columns are the sum of all countable factors. 

### Game Rules
We also had deep discussion on the calculation of two types. According to official introduction, not all pokemons have the second type. In order to quantify all the types for later calculation, we use Type I to fill the blanks which means all the pokemon have two type attributes while some of them the Type I and Type II are the same as Type I . There will be only one attribute counted each time for each pokemon during one turn of combat according to the game rule.

### Three Score Systems
Furthermore, to refine the attributes, we established a detailed scoring system to numeric the effectiveness and weakness among different types based on the “Pokemon Go type Chart” (https://www.eurogamer.net/articles/2018-01-15-pokemon-go-type-chart-effectiveness-weaknesses ) between all match-up. There are four different levels among two type (for example, type A and type B): Strong Against (effect of A hitting B is great), Weak Against (effect of A hitting B is very poor), Resistant To (not so much effect when A hits B, this is different from Weak Against), Vulnerable To (effect of A hitting B is great). We considered the level “Vulnerable To” as a reverse situation of “Strong Against” thus it’s not counted in.

During the process scoring type attributes, a consensus has been reached that if type A is “Strong Against” type B, the A-B score will gain “1” point while B-A score will be “-1”. But we had some disputations among “Weak Against” and “Resistant To”, so we set two scoring systems: 
    1). “Weak-Minus” scoring: If type A is “Weak Against” B, the A-B score will be “-1”, other score will be counted; 
    2). “Resistant-Minus” scoring:   If type A is “Resistant To” type B, the A-B score will be “-1”, no other score will be counted. 

We also tried to run generalized linear regression on these two score systems as well as combining the two system together to
find the best score system model . Finally we chose the “Weak-minus” system (system 1) for our datasets. Details will be discussed and shown in the later modules. 

### Python
After the determination of the score system, we then pre-processed all the data by Python including the importing of data,
the construction of scoring system based on training datasets (the “combats.csv” file) and the results of scores , so that all the data could be further processed in R to construct our ideal model for prediction.
