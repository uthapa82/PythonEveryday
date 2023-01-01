# A Polar coordinates are an alternative way of 
# representing Cartesian Coordinates of complex Numbers 
import cmath as c

def main():
    user_cnumber = complex(input())
    modulus_r = c.phase(user_cnumber)
    phase_angle = abs(user_cnumber)
    
    print(phase_angle)
    print(modulus_r)
    
     
if __name__ == '__main__':
    main()