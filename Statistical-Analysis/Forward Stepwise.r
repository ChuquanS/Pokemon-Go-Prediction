library(leaps)
c<-regsubsets(result~.,data=d)
c=summary(c)
dovalbest = function(object,newdata,ynm)
{
  form = as.formula(object$call[[2]])
  p=ncol(newdata)-1
  rmsev = rep(0,p)
  test.mat = model.matrix(form,newdata)
  for(k in 1:p) {
    coefk = coef(object,id=k)
    xvars = names(coefk)
    pred = test.mat[,xvars] %*% coefk
    y = rep(10,length(newdata[[ynm]]))
    y[newdata[[ynm]] == TRUE] = 2
    y[newdata[[ynm]] == FALSE] = 1
    rmsev[k] = sqrt(mean((y-pred)^2))
  }
  return(rmsev)
}
ntry=100
p=ncol(d)-1
resmat = matrix(0,p,ntry)
set.seed(14)
for(i in 1:ntry) {
  train = sample(1:nrow(d),floor(nrow(d)/2)) 
  regfit.best=regsubsets(result~.,data=d[train,],nvmax=18,nbest=1,method="exhaustive")
  resmat[,i]=dovalbest(regfit.best,d[-train,],'result')
}
mresmat = apply(resmat,1,mean)
plot(mresmat,xlab='num vars',ylab='rmse',type='b',col='blue',pch=19,cex.lab=1.5)
kopt = 18
c.best=regsubsets(result~.,data=dtrain,nvmax=kopt,nbest=1,method="exhaustive")
form = as.formula(c.best$call[[2]])
test.mat = model.matrix(form,dtest)
coefk = coef(c.best,id=18)
xvars = names(coefk)
pred = test.mat[,xvars] %*% coefk
ypred = rep(FALSE,length(dtest[['result']]))
for(i in 1:nrow(pred)) {
   if(pred[i]>=1.5){ypred[i]=TRUE}
}
senspe = function(dtest,ypred){
  tp=tn=fp=fn=0
  for(i in 1:length(ypred)){
   b = ypred[[i]]
   a = dtest$result[i]
   if(b==TRUE){
      if(a==TRUE){
        tp = tp + 1
     }else{
       fp = fp + 1
      }
    }
   if(b==FALSE){
      if(a==FALSE){
        tn = tn + 1
      }else{
        fn = fn + 1
     }
    }
  }
  sen = tp/(tp+fn)
  spe = tn/(tn+fp)
  t = cbind(sen,spe)
  colnames(t) = c('sensitivity','specificity')
  return(t)
}
a = senspe(dtest,ypred)
