% debug_signal_plot.m
% Debug helper: read a captured signal file, plot it, and return a dummy
% value for the caller (knock_detection.py used this while prototyping).
function y=debug_signal_plot(x)
% Read the raw sample values from the text file.
a=textread('SignalTest1.txt');
% Plot the first column against the sample index.
plot(1:length(a),a(:,1));
% Placeholder output for the caller.
y=randi(1);
end
