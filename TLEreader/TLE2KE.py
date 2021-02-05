# Using files given in 3(a) since I was unable to output to serial monitor in HW 1.
# Using python.
# Name: Paul Bischoff

import numpy as np
import math

def main():
	file = open("TLE.txt", "rt")
	ballistic_C, d2n_dt, inc, RAAN, e, w, M, n, rev = set_Elements(file)
	pos_V, vel_V = compute_Pos_Vel_in_ECI(ballistic_C, d2n_dt, inc, RAAN, e, w, M, n, rev)
	new_file = open("KERV.TXT", "w+")
	line = new_file.readlines()
	file.close()
	L1 = [ballistic_C, d2n_dt, inc, RAAN, e, w, M, n, rev]
	L2 = [pos_V, vel_V]
	new_file.write(str(L1))
	new_file.write(str(L2))


# Format for the TLE set was found through "https://www.celestrak.com/NORAD/documentation/tle-fmt.php"
# For line1, I only get first (ballistic coefficient) and second derivative of mean motion and drag term (radiation coefficient)
# For line2, I get everything except line number, satellite number and checksum.
def set_Elements(file):
	lines = file.readlines()
	file.close()
	line1 = lines[0]
	line2 = lines[1]
	ballistic_C = line1[34:43]
	d2n_dt = line1[45:52]
	inc = float(line2[9:16])
	RAAN = float(line2[18:25])
	e = float(line2[27:33]) # eccentricity
	w = float(line2[35:42]) # argument of perigree
	M = float(line2[44:51]) # Mean anomaly
	n = float(line2[55:63]) # Mean motion
	rev = float(line2[64:68]) # revoultion # at epoch
	return ballistic_C, d2n_dt, inc, RAAN, e, w, M, n, rev

def compute_Pos_Vel_in_ECI(ballistic_C, d2n_dt, inc, RAAN, e, w, M, n, rev):
	mu = 398600
	a = np.cbrt(mu/(np.square((n*2*np.pi/(24*3600)))))
	err = np.exp(1e-10)
	E0 = M
	t = 1
	i = 0
	while(t):
		E = M + e*np.sin(E0)
		if (np.abs(E - E0) < err):
			t = 0
		E0 = E
		i += i
	v = np.arccos((np.cos(E) - e)/(1 - e*np.cos(E))) # Following the starter code for calculating true anomaly (v)
	r_C = a*(1 - E*np.cos(e)) # distance to central body
	vel_Coeff = (np.sqrt(mu*a)/r_C)
	pos_V = [r_C*np.cos(v), r_C*np.sin(v), 0] # To make these state vectors, I used the algoritm from "https://downloads.rene-schwarz.com/download/M001-Keplerian_Orbit_Elements_to_Cartesian_State_Vectors.pdf"
	vel_V = [vel_Coeff*(-np.sin(E)), vel_Coeff*((1 - e)*np.cos(E)), 0]
	return pos_V, vel_V









if __name__ == "__main__":
	main()

# %%
# % Two-line element set
# close all
# clear all
# clc
#
# mu = 398600; %  Standard gravitational parameter for the earth
#
# % TLE file name
# fname = 'TLE.txt';
#
# % Open the TLE file and read TLE elements
# fid = fopen(fname, 'rb');
# L1c = fscanf(fid,'%69c',1); % L1c contains the first line of the TLE as CHARACTERS
# L2c = fscanf(fid,'%*2c %67c',1);  % L2c contains the second line of the TLE as Characters
#
# % Close the TLE file
# fclose(fid);
#
# % EXAMPLE: inclination is located on character count 09-16 in Line 2 of the TLE. https://en.wikipedia.org/wiki/Two-line_element_set "WikiPEdia Is NOt a CrEDIble SOUrcE"
# inc = str2num(L2c(1,9:16));
#
#
# % Calculating the true anomaly requires Newton Rhapson mehtod, uncomment the following to calculate true anomaly from Eccentric anomaly (E)
# % Calculate the eccentric anomaly using Mean anomaly (M). True anomaly can then be calculated form the Eccentric Anomaly.
# %err = 1e-10;            %Calculation Error
# %E0 = M; t =1;
# %itt = 0;
# %while(t)
# %       E =  M + ecc*sind(E0);
# %      if ( abs(E - E0) < err)
# %          t = 0;
# %      end
# %      E0 = E;
# %      itt = itt+1;
# %end
# %trueAnom = acosd((cosd(E)-ecc)/(1-ecc*cosd(E)));
