d = read.delim2('python/test.txt',sep = '\t', header = FALSE)
d2 = read.csv('python/combination.csv')
scoreChu = cbind(d2$A_B_Scores,d2$B_A_Scores)
str = '#1,Name1,TypeA1,TypeB1,HP1,Attack1,Defense1,spAtk1,spDef1,Speed1,Generation1,LegendaryA,#2,Name2,TypeA2,TypeB2,HP2,Attack2,Defense2,spAtk2,spDef2,Speed2,Generation2,LegendaryB,cattribute1,cattribute2,y1'
colo = strsplit(str,',')
colnames(d) = colo[[1]]
scorexuchu = cbind(d2$A_B_Scores+as.numeric(as.character(d$cattribute1)),d2$B_A_Scores+as.numeric(as.character(d$cattribute2)))
d = d[,-1:-4]
d = d[,-9:-12]
d$Legendary1[d$LegendaryA == 'False'] = FALSE
d$Legendary1[d$LegendaryA == 'True'] = TRUE
d$Legendary2[d$LegendaryB == 'True'] = TRUE
d$Legendary2[d$LegendaryB == 'False'] = FALSE
d = d[,-8]
d = d[,-15]
d2 = d[,-which(colnames(d) == 'cattribute1')]
d2 = d2[,-which(colnames(d2) == 'cattribute2')]
d3 = cbind(d2,scorexuchu)
d2 = cbind(d2,scoreChu)
colnames(d2)[which(colnames(d2) == '1')] = 'cattribute1'
colnames(d2)[which(colnames(d2) == '2')] = 'cattribute2'
colnames(d3)[which(colnames(d3) == '1')] = 'cattribute1'
colnames(d3)[which(colnames(d3) == '2')] = 'cattribute2'
d$result[d$y1 == 'False'] = FALSE
d$result[d$y1 == 'True'] = TRUE
d = d[,-which(colnames(d) == 'y1')]
d2$result[d2$y1 == 'False'] = FALSE
d2$result[d2$y1 == 'True'] = TRUE
d2 = d2[,-which(colnames(d2) == 'y1')]
d3$result[d3$y1 == 'False'] = FALSE
d3$result[d3$y1 == 'True'] = TRUE
d3 = d3[,-which(colnames(d3) == 'y1')]
d$result = as.factor(d$result)
d2$result = as.factor(d2$result)
d3$result = as.factor(d3$result)
train = sample(1:nrow(d),floor(nrow(d)/2))
#dtrain = d[train,]
#dtest = d[-train,]
dtrain = d2[train,]
dtest = d2[-train,]
d=d2
#dtrain = d3[train,]
#dtest = d3[-train,]
