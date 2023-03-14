library(gganimate)

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


library(gganimate)
library(gifski)

df$n = 1:nrow(df)
p = ggplot(df, aes(x=x, y=y)) +
  geom_point() +
  transition_time(n) +
  shadow_mark(past = T, future=F, alpha=0.3)


animate(
  plot = p, 
  nframes = nrow(df)/5, 
  fps = 50, 
  end_pause = 8
)


p = ggplot(df, aes(x=0, y=y, label=y)) +
  geom_point() +
  geom_text(hjust=0, vjust=1) +
  transition_time(n)

animate(
  plot = p, 
  nframes = nrow(df)/40, 
  fps = 50, 
  end_pause = 8
)
