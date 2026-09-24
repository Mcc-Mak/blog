function y=dataprocess(x)
a=textread('SignalTest1.txt');
plot(1:length(a),a(:,1));
y=randi(1);
end



