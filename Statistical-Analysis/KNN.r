library(kknn)
dtest$result = as.numeric(dtest$result)
c = rep(0,30)
kv = 1:30
for(i in kv){
kf20 = kknn(result~.,dtrain,dtest,k=i,kernel = "rectangular")
pred = kf20$fitted.values
rocR = roc(response=dtest$result,predictor=pred) 
cat("k:",i," RMSE:",sqrt(mean((pred - dtest$result)^2)))
c[i] = sqrt(mean((pred - dtest$result)^2))
}
plot(c,xlab = 'k',ylab = 'RMSE')
k=17
kf17 = kknn(result~.,dtrain,dtest,k=k,kernel = "rectangular")
pred = kf17$fitted.values
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
cat("sensitivity:",sen,"\tspecificity:",spe)
