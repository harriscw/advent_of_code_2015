library(dplyr)
library(tidyr)
library(ggplot2)
library(gganimate)
rm(list=ls())

input = read.table("../input.txt",header=FALSE,stringsAsFactors = FALSE) %>% 
  select(name=V1,distance=V4,duration=V7,rest=V14)


getposition=function(reindeer,seconds){
  cnt=1
  thesum=0
  myvec=c()
  for(i in 1:seconds){
    if(cnt<=input[input$name==reindeer,"duration"]){
      thesum=thesum+input[input$name==reindeer,"distance"]
    }else if(cnt==input[input$name==reindeer,"duration"]+input[input$name==reindeer,"rest"]){
      cnt=0
    }
    myvec=c(myvec,thesum)
    cnt=cnt+1
  }
  return(myvec)
}

print(getposition("Comet",1000))


df=data.frame(order=1:2503)
for(name in input$name){
  df[[name]]=getposition(name,2503)
}

df %>% select(-order) %>% tail(1) %>% max()#part 1 solution

dflong= df %>% pivot_longer(!order, names_to = "name", values_to = "x") %>% mutate(y=(length(unique(name))+1)-as.numeric(as.factor(name))) %>% arrange(order,y)

dflong= dflong %>% 
  group_by(order) %>% 
  mutate(max=max(x)) %>% 
  ungroup() %>%
  mutate(winner=ifelse(x==max,name,NA))

table(dflong$winner)#part 2 solution

###
# Animated barchart
###

getpoints=function(reindeer){#This function gets each reindeer's current points at every timepoint
  points=c()
  totalpoints=0
  for(i in 1:nrow(dflong)){
    if(!is.na(dflong$winner[i]) & dflong$winner[i]==reindeer){
      totalpoints=totalpoints+1
    }
    if(dflong$name[i]==reindeer){
    points[i]=totalpoints
    }
    else{
      points[i]=NA
    }
  }
  return(points)
}

mylist=list()#iterate over each reindeer and combine them into a list
for(name in unique(dflong$name)){
  mylist[[name]]=getpoints(name)
}

#combine all point status into a single variable
#I am a bad person for doing combining things this way
dflong$points=ifelse(!is.na(mylist[[1]]),mylist[[1]],
       ifelse(!is.na(mylist[[2]]),mylist[[2]],
              ifelse(!is.na(mylist[[3]]),mylist[[3]],
                     ifelse(!is.na(mylist[[4]]),mylist[[4]],
                            ifelse(!is.na(mylist[[5]]),mylist[[5]],
                                   ifelse(!is.na(mylist[[6]]),mylist[[6]],
                                          ifelse(!is.na(mylist[[7]]),mylist[[7]],
                                                 ifelse(!is.na(mylist[[8]]),mylist[[8]],
                                                        ifelse(!is.na(mylist[[9]]),mylist[[9]],
                                                               NA)))))))))


p=ggplot(dflong, aes(fill=name, y=points, x=name)) + 
  geom_bar(position="dodge", stat="identity")+
  theme(
        axis.title.x=element_blank(),
        legend.title = element_blank()
  ) +
  transition_time(order)

animate(p
        # ,nframes=(nrow(allpositions)/2)+10
        ,nframe=130
        # ,fps=100
        ,end_pause = 30
        ,renderer=gifski_renderer("part2.gif")
)

