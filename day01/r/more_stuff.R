rm(list=ls())
library(gganimate)
library(gifski)
library(ggimage)

input = read.csv("../py/input.txt",header=FALSE,stringsAsFactors = FALSE)

#find and replace then sum solution
paste("Part 1 obnoxious one-liner:",sum(as.numeric(gsub("\\)","-1",gsub("\\(","1",unlist(strsplit(input[[1]],"")))))))


### Animation
myvec=unlist(strsplit(unlist(input),""))
df = data.frame()
acc=0
for(i in 1:length(myvec)){
  if(myvec[i]=="("){
    acc=acc+1
  }else{
      acc=acc-1
      }
  df = rbind(df,
             data.frame(x=i,y=acc))
}

df$n = 1:nrow(df)
df$image="santa.jpg"

# x axis is time

p = ggplot(df, aes(x=x, y=y)) +
  geom_point() +
  theme_minimal() +
  transition_time(n) +
  shadow_mark(past = T, future=F, alpha=0.3)

animate(
  plot = p, 
  duration=10,
  end_pause = 30,
  nframes = nrow(df)/10 #can sample frames here to speed up.  But we wont get the right answer at the end if we don't include all frames
)

anim_save("gif1.gif", animation = last_animation())


# now with image


p = ggplot(df, aes(x=x, y=y, image=image)) +
  geom_point() +
  geom_image() +
  theme_minimal() +
  transition_manual(n) 


animate(
  plot = p, 
  duration=10,
  end_pause = 30
)

anim_save("gif2.gif", animation = last_animation())

# X axis is a constant

# df = head(df,1000)

p = ggplot(df, aes(x=0, y=y, label=y,image=image)) +
  geom_point() +
  geom_image(size=.1) +
  geom_text(hjust=0, vjust=1, position = position_nudge(x=.25),size=15) +
  theme_minimal() +
  ylab("Floor") +
  scale_x_continuous(limits = c(-.5, 1)) +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) +
  transition_manual(n) 

animate(
  plot = p,
  duration=10,
  end_pause = 30
)

anim_save("gif3.gif", animation = last_animation())
