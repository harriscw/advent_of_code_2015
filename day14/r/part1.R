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

p=ggplot(data=dflong,
         aes(x=x, y=y,color=name,group=name)) +
  geom_point(size=5) +
  theme(axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank(),
        axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        ) +
  transition_time(order) +
  geom_path() +
  transition_reveal(along = order)

animate(p
        # ,nframes=(nrow(allpositions)/2)+10
        ,nframe=130
        # ,fps=100
        ,end_pause = 30
        ,renderer=gifski_renderer("part1.gif")
)