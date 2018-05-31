library(glmnet)
mGlm = glm(result~.,dtrain,family = binomial)
phat = predict(mGlm,dtest,type="response")
source("lift-loss.R")
lift.plot(phat,dtest$result)
library(pROC)
rocR = roc(response=dtest$result,predictor=phat) 
AUC = auc(rocR)
plot(rocR)
title(main=paste("model AUC= ",round(AUC,2)))
s = 0
sen = 0
spe = 0
for(i in 1:length(rocR$sensitivities)){
  t = rocR$sensitivities[i] + rocR$specificities[i]
  if(t>s){
    s = t
    sen = rocR$sensitivities[i]
    spe = rocR$specificities[i]
  }
}
cat("sensitivity:",sen,"\tspecificity:",spe)
sqrt(mean((phat - dtest$result)^2))
