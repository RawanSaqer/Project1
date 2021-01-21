
### Swarm Optimization  Optimization(PSO)
<br>
<font color='purple' size='3.5'>
In computational science, particle swarm optimization (PSO)[1] is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according to simple mathematical formulae over the particle's position and velocity. Each particle's movement is influenced by its local best known position, but is also guided toward the best known positions in the search-space, which are updated as better positions are found by other particles. This is expected to move the swarm toward the best solutions.</font>

![Screen%20Shot%202020-11-03%20at%2011.44.47%20AM.png](attachment:Screen%20Shot%202020-11-03%20at%2011.44.47%20AM.png)

![Screen%20Shot%202020-11-03%20at%2011.39.53%20AM.png](attachment:Screen%20Shot%202020-11-03%20at%2011.39.53%20AM.png)

![Screen%20Shot%202020-11-03%20at%2011.51.16%20AM.png](attachment:Screen%20Shot%202020-11-03%20at%2011.51.16%20AM.png)

![Screen%20Shot%202020-10-28%20at%2010.07.01%20AM.png](attachment:Screen%20Shot%202020-10-28%20at%2010.07.01%20AM.png)

### For more details:
- Research paper: https://reader.elsevier.com/reader/sd/pii/S0898122111004299?token=FBDD045726FCB6A6EB52C4ABE434511AFAE5D435CD413894BACBC584E5A784D0009C7A33B0EA45B36E4A1B2ED2FFCFBD
- powerpoint:
https://www.slideshare.net/raafiubrian/particles-swarm-optimization
- video:
https://www.youtube.com/watch?v=uwXFnzWaCY0

#### <font color='red'> Write Python program for applying PSP for solving any n variable optmization problem. Your program must follow the following:</font>

from __future__ import division
import random
import math

def func1(x): #COST FUNCTION 
    total=0
    for i in range(len(x)):

      
      total=((x[i]+10*x[i])**2)+(5*(x[i]-x[i])**2)+((x[i]-2*x[i])**4) +(10*(x[i]-x[i])**4)
    
    return total
# function we are attempting to optimize (minimize)
    

import random
import numpy as np 
W = 0.5
c1 = 0.7
c2 = 0.9 

n_iterations = int(input("The number of iterations is: "))
target_error = float(input("The target error is: "))
n_particles = int(input("The number of particles is: "))

class Particle:
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random()*50, (-1)**(bool(random.getrandbits(1))) * random.random()*50])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([1,1])

    def __str__(self):
        print("The position is ", self.position, " And the pbest is ", self.pbest_position)
    
    def move(self):
        self.position = self.position + self.velocity

class pso():

    def __init__(self, target, target_error, n_particles):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random()*50, random.random()*50])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()
   
    def fitness(self, particle):
        return particle.position[0] ** 2 + particle.position[1] ** 2 + 1

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            global W
            new_velocity = (W*particle.velocity) + (c1*random.random()) * (particle.pbest_position - particle.position) + \
                            (random.random()*c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
            

search_space = pso(1, target_error, n_particles)
particles_vector = [Particle() for _ in range(search_space.n_particles)]
search_space.particles = particles_vector
search_space.print_particles()

iteration = 0
while(iteration < n_iterations):
    search_space.set_pbest()    
    search_space.set_gbest()

    if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break

    search_space.move_particles()
    iteration += 1
    
print("The best solution is --> ", search_space.gbest_position, " in the iterations --> ", iteration)


