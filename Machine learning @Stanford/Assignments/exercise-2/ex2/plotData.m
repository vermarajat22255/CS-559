function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%
xpos = find(y==1);
xneg = find(y==0);
plot(X(xpos,1),X(xpos,2), 'ks','LineWidth',2, 'MarkerSize',7,'MarkerFaceColor','g');
plot(X(xneg,1),X(xneg, 2),'ko','LineWidth',2, 'MarkerSize',7,'MarkerFaceColor','r');

% =========================================================================



hold off;

end
