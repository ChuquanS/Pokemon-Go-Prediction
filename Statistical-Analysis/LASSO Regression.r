y = d$result
x = model.matrix(result~.,d)
dgn = glmnet(x,y,family="binomial",intercept=FALSE,alpha=1)
cvdgn = cv.glmnet(x,y,nfolds=10,family="binomial",alpha=1,intercept=FALSE)
minlam = cvdgn$lambda.min
minlam1 = cvdgn$lambda.1se
minlamT = paste("minlam and minlam (1se) are: ",round(minlam,4),round(minlam1,4))
bhatL = coef(dgn,s=minlam)[,1]
print(bhatL[bhatL!=0])
bhatL = bhatL[which(bhatL != 0)]
plot(cvdgn$glmnet.fit)
xvars = names(bhatL)
test = model.matrix(result~.,dtest)
pred = test[,xvars] %*% bhatL
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
