library(dplyr)
library(stringr)
library(ggplot2)
library(gganimate)
library(gifski)

rm(list=ls())

input = read.csv("../input.txt",header=FALSE,stringsAsFactors = FALSE)

myvec=c()#copied code from d1
for(i in 1:nchar(input)){
  #print(substr(input,i,i))
  myvec = c(myvec,substr(input,i,i))
}

santaposition=data.frame(who="SANTA",x=0,y=0,order=0)
roboposition=data.frame(who="ROBOT",x=0,y=0,order=0)
allpositions=rbind(santaposition,roboposition)
cnt=1
for(i in myvec){
  #print(i)
  if(cnt %% 2==1){#odd
    if(i=="^"){santaposition[["y"]]=santaposition[["y"]]+1}
    else if(i==">"){santaposition[["x"]]=santaposition[["x"]]+1}
    else if(i=="v"){santaposition[["y"]]=santaposition[["y"]]-1}
    else if(i=="<"){santaposition[["x"]]=santaposition[["x"]]-1}
    santaposition$order=cnt
  }else{
    if(i=="^"){roboposition[["y"]]=roboposition[["y"]]+1}
    else if(i==">"){roboposition[["x"]]=roboposition[["x"]]+1}
    else if(i=="v"){roboposition[["y"]]=roboposition[["y"]]-1}
    else if(i=="<"){roboposition[["x"]]=roboposition[["x"]]-1}
    roboposition$order=cnt
  }
  allpositions=rbind(allpositions,santaposition,roboposition)
  cnt=cnt+1
}

allpositions %>% select(-order) %>% distinct() %>% nrow() #part 2 solution




###
#Lets plot the path
###

santa=allpositions %>% filter(who=="SANTA")
robot=allpositions %>% filter(who=="ROBOT")

theorigin=head(allpositions,1)
santafinal=tail(santa,1)
robotfinal=tail(robot,1)

png(filename="path_pt2.png")
ggplot(data=allpositions,
       aes(x=x, y=y,color=who,group=who)) +
  geom_path() +
  geom_point(aes(x = x, y = y), theorigin, size=5,color = "green") +
  geom_point(aes(x = x, y = y), santafinal, size=5,color = "red") +
  geom_point(aes(x = x, y = y), robotfinal, size=5,color = "blue")
dev.off()

###
#Lets do an animated gif of the path
###

p=ggplot(data=allpositions,
         aes(x=x, y=y,color=who,group=who)) +
  geom_point(size=5) +
  transition_time(order) +
  geom_path() +
  transition_reveal(along = order)+
  geom_point(aes(x = x, y = y), theorigin, size=5,color = "green")

animate(p
        # ,nframes=(nrow(allpositions)/2)+10
        ,nframe=200
        # ,fps=100
        ,end_pause = 30
        ,renderer=gifski_renderer("path_pt2.gif")
        )
