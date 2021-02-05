library(dplyr)

input = read.csv("../py/input.txt",header=FALSE,stringsAsFactors = FALSE)

myvec=c()#I did this so I could write out a csv that could be imported by scratch
for(i in 1:nchar(input)){
  print(substr(input,i,i))
  myvec = c(myvec,substr(input,i,i))
}

write.table(myvec,file="input.csv",row.names = FALSE,col.names=FALSE,sep=",")

cnt=0 #I counted to make sure I didn't make an error somewhere (because scratch wasn't getting the right answer)
x=0
myout=data.frame(x=0,y=0)
for(i in 1:nchar(input)){
  if(substr(input,i,i)=="("){
    cnt=cnt+1
  }else{
    cnt=cnt-1
  }
  x=x+1
  myout=rbind(myout,
              data.frame(
                x=x,
                y=cnt
              ))
}



png(filename="part1.png")
plot(myout$x,myout$y,xlab="Step",ylab="Floor",cex=.1)

text(head(myout[myout$y==-1,"x"],1)+250,0,as.character(head(myout[myout$y==-1,"x"],1)))
abline(v=head(myout[myout$y==-1,"x"],1))

text(tail(myout[,"x"],1)+150,tail(myout[,"y"],1),as.character(tail(myout[,"y"],1)))
abline(v=tail(myout[,"x"],1))

dev.off()

