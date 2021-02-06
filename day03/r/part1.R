library(dplyr)
library(stringr)
library(ggplot2)
library(gganimate)
library(gifski)

rm(list=ls())

input = read.csv("../input.txt",header=FALSE,stringsAsFactors = FALSE)

myvec=c()#I originally did this so I could write out a csv that could be imported by scratch
for(i in 1:nchar(input)){
  #print(substr(input,i,i))
  myvec = c(myvec,substr(input,i,i))
}

position=allpositions=data.frame(x=0,y=0)
cnt=0
for(i in myvec){
  #print(i)
  if(i=="^"){position[["y"]]=position[["y"]]+1}
  else if(i==">"){position[["x"]]=position[["x"]]+1}
  else if(i=="v"){position[["y"]]=position[["y"]]-1}
  else if(i=="<"){position[["x"]]=position[["x"]]-1}
  allpositions=rbind(allpositions,position)
  cnt=cnt+1
}

nrow(distinct(allpositions)) #part 1 solution

#Lets plot the path
png(filename="path.png")
plot(x=allpositions,type="S",pch = 20,cex=.01)
points(x=0,y=0,col="green",pch=19,cex=1.5)
points(tail(allpositions,1),col="red",pch=19,cex=1.5)
dev.off()

#Lets do an animated gif od the path
#This took a long time to render, maybe 30min
#I also used an online tool to speed up the gif
allpositions = allpositions %>% mutate(order=row_number())
theorigin=allpositions[1,]

p=ggplot(data=allpositions,
       aes(x=x, y=y)) +
  geom_point(color="red",size=5) +
  transition_time(order) +
  geom_line() +
  transition_reveal(along = order)
p=p+geom_point(aes(x = x, y = y), theorigin, size=5,color = "green")
out=animate(p,nframes=nrow(allpositions)+10,fps=100,end_pause = 10,renderer=gifski_renderer("thepath.gif"))
