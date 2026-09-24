%% MATLAB
% jk.m - passthrough helper for prototyping the Python<->MATLAB bridge.
function lol = jk(args)
    arg1 = args.arg1;  % unwrap the struct passed by pymatbridge
    lol = arg1;        % simply return the input unchanged
end