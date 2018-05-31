We tried 3 different methods from our Machine Learning class. We firstly tried to find the most proper score system with high sensitivity and specificity among three systems (“Resistant-Minus”, “Weak-Minus”, and the combination) and to set a baseline model for later analysis. So we chose Logistic Regression to achieve this basic goal. Then Forward Stepwise and Lasso Regression were performed to choose highly related variables. Finally, we tuned Single Layer Neural Net (N-net) and discuss the corresponding results.

## Baseline: Generalized Linear Models -- Logistic Regression

To give us a baseline model, we chose Logistic Regression by the R package glm . As mentioned earlier, we tried three different score systems for the model construction. The results of Logistic Regression can also give us a direct comparison of the Sensitivity and Specificity of each score system which are shown as follow. It’s easy to see that the “Weak-Minus” Score is the best score system with the obvious highest sensitivity among all systems while the specificity also presents good. We’ll use this score system to refine the original datasets for later modeling progress.

                                         Sensitivity           Specificity
     “Resistant-Minus” Score Results      0.8783247             0.8899445
     “Weak-Minus” Score Results           0.8962081             0.8851736
     Combination Score-System Results     0.8905146             0.8751144
     
By using “Weak-Minus” Score Results, we reached a pretty high model AUC which is 0.93(shown in Figure 1). The baseline model (with the RMSE is 0.3161057) from Logistic Linear Regression is given by Figure 2 (the combats between two pokemons).

![image](https://github.com/ChuquanS/Pokemon-Go-Prediction/blob/Statistical-Analysis/Figure1.png)

              Figure 1. The AUC score of our baseline model (pretty good!) in chosen scoring system

![image](https://github.com/ChuquanS/Pokemon-Go-Prediction/blob/Statistical-Analysis/Figure2.png)

              Figure 2. The given baseline model (shown by coefficients of each variables)


## Variables Decision -- Forward Stepwise & LASSO Regression

We performed R package leaps for Forward Stepwise which got the sensitivity was 0.8716405 and the specificity was 0.8984476. All the predictions reflect the potential situation when Pokemon 1 attacks Pokemon 2. The model is used to predict the results whether the first pokemon (Pokemon 1) could win the combat. As Forward Stepwise could show us how powerful a variable could affect the results, according to Figure 3(a), there must a variable that counts a lot. Nearly two to three variables could decide the final result. Based on Figure 3(b), it’s obviously that speed is the most influential factor as the coefficient of Speed1 (the speed of the first pokemon) is the largest one (7.97625 x 10-3). To our surprise, the Generation is the second important factor (which indicates that the newer pokemons could be more powerful -- a typical promotion method: the newer, the better). 

![image](https://github.com/ChuquanS/Pokemon-Go-Prediction/blob/Statistical-Analysis/Figure3(a).png)

                                   Figure 3(a) The linear graph of Forward Stepwise

![image](https://github.com/ChuquanS/Pokemon-Go-Prediction/blob/Statistical-Analysis/Figure3(b).png)

                    Figure 3(b) The coefficients of each variables given by Forward Stepwise
                      

Comparing with Forward Stepwise, LASSO Regression gave us a much higher sensitivity, which was 0.894362, as well as specificity, which was 0.8844377.  As we comparing all potential factors of two pokemons (for each combat), there are 18 variables (9 variables of each pokemon) in total. LASSO also helped us delete one of the variables, that is to say the “spDef1” factor,  which has the least power to affect the combat results, shown in Figure 4. This is because in our first process which decided the scoring system, we finally chose the “Weak-Minus” system which completely ignored the “Resistant To” level of pokemons’ attributes effectiveness, thus resulting in the “Resistant To” relationship having no influence on the first pokemon at all. On the other hand, the extremely small “spAtk2” is also a reverse evidence to prove this. But in general, the results from LASSO are similar to Forward Stepwise with Speed and Generation making a lot of sense.

![image](https://github.com/ChuquanS/Pokemon-Go-Prediction/blob/Statistical-Analysis/Figure4.png)

                                      Figure 4. Results from LASSO Regression
 
 
## Single Layer Neural Net

We utilized “nnet” R package to perform neural net. Size and decay have been tuned in nnet function. The interesting is that neural net works amazingly well in this dataset. With size = 5, decay = 0.01, we achieved a RMSE of 0.6690407 together with sensitivity of 0.9582026 and  specificity of 0.938281 (shown blow).

                                      size	        decay	           RMSE
                                       45	           0.01	        0.6779564
                                       45	          0.001	        0.6772778
                                       30	           0.01	        0.6728255
                                       20	           0.01	        0.6754876
                                       10	           0.01	        0.6727617
                                       5	           0.01	        0.6690407
                                       1	           0.01	        0.6875044


## KNN

The R package ‘kknn’ was made use of to achieve KNN. Despite the fact that knn took a lot of time, it did not work very well in this dataset. The sensitivity is 0.8888512 and specificity is 0.8212041 under k=17, which is the most optimal k using cross-validation.

![image](https://github.com/ChuquanS/Pokemon-Go-Prediction/blob/Statistical-Analysis/Figure5.png)

                                             Figure 5
                                             
