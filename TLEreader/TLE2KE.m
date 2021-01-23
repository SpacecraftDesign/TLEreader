%%
% Two-line element set
close all
clear all
clc

mu = 398600; %  Standard gravitational parameter for the earth

% TLE file name
fname = 'TLE.txt';

% Open the TLE file and read TLE elements
fid = fopen(fname, 'rb');
L1c = fscanf(fid,'%69c',1); % L1c contains the first line of the TLE as CHARACTERS
L2c = fscanf(fid,'%*2c %67c',1);  % L2c contains the second line of the TLE as Characters

% Close the TLE file
fclose(fid);

% EXAMPLE: inclination is located on character count 09-16 in Line 2 of the TLE. https://en.wikipedia.org/wiki/Two-line_element_set "WikiPEdia Is NOt a CrEDIble SOUrcE"
inc = str2num(L2c(1,9:16));


% Calculating the true anomaly requires Newton Rhapson mehtod, uncomment the following to calculate true anomaly from Eccentric anomaly (E)
% Calculate the eccentric anomaly using Mean anomaly (M). True anomaly can then be calculated form the Eccentric Anomaly. 
%err = 1e-10;            %Calculation Error
%E0 = M; t =1;
%itt = 0;
%while(t)
%       E =  M + ecc*sind(E0);
%      if ( abs(E - E0) < err)
%          t = 0;
%      end
%      E0 = E;
%      itt = itt+1;
%end
%trueAnom = acosd((cosd(E)-ecc)/(1-ecc*cosd(E)));
