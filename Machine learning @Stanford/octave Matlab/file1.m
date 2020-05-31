subplot(1,2,1) %create 1 row 2 column plot and operate on 1st
plot(t,y1,"g:*")
xlabel("Time")
ylabel("Value")
title("Sin Function")

subplot(1,2,2)
plot(t,y2,"r:s")
xlabel("Time")
ylabel("Value")
title("Cosine Function")
print "mpplot.png" % to save the plot

pwd
%operating on 2nd plot, change its axis by

axis([ 0 0.5 -1 1])

%similarly changing axis on 1st plot
subplot(1,2,1)
axis([0, 0.5, -1, 1])
print "myplot.png"
close %Close the graph

% ------------------------------------------------------
%Visualising a matrix using colors 
m = magic(5);
imagesc(m), colorbar, colormap gray;
display(m)