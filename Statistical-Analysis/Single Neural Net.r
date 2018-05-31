library(doParallel) 
registerDoParallel()
dtrain$result = as.logical(dtrain$result)
dtest$result = as.logical(dtest$result)
library(nnet)
set.seed(5*i)
nnfit = nnet(result~.,dtrain,size=5,decay=0.01,linout=T,maxit=100)
pred = predict(nnfit,dtest)
rocR = roc(response=dtest$result,predictor=pred) 
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
cat("RMSE:",sqrt(mean((pred - dtrain$result)^2)))
cat("sensitivity:",sen,"\tspecificity:",spe)
