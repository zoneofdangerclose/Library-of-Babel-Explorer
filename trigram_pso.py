import numpy as np
import matplotlib.pyplot as plt
import os
import re
import subprocess
from multiprocessing import Pool
import random
import logging
import time

current_time = time.localtime()
current_time = time.strftime("%Y%m%d_%H_%M_%S", current_time)
logfile = f'C:/Users/cgzho/OneDrive/Documents/Python Scripts/Partical Swarm Optimization/log_{current_time}.txt'

logger = logging.getLogger(__name__)
logging.basicConfig(filename=logfile, encoding='utf-8', level=logging.INFO)

logger.info('Start')


vol_range = range(40,50)
shelf_range = range(1,10)

pso_iterations_dir = "C:/Users/cgzho/OneDrive/Documents/Python Scripts/Partical Swarm Optimization/pso_iterations"
file_dir = os.getcwd().replace(os.path.basename(os.getcwd()),"")
file_dir = f'{file_dir}cgzho\\OneDrive\\Documents\\GitHub\\'
explorer_dir = f'{file_dir}Library-of-Babel-Explorer/'
pybel_cli = f'{file_dir}Library-Of-Pybel/library_of_babel.py'

trigram_file = f'{explorer_dir}data_dir/trigram_abbrv.txt'
trigram_set = set()
for trigram in open(trigram_file).readlines():
    trigram = trigram.replace('\n','')
    # trigram_dict.update({trigram: 0})
    trigram_set.add(trigram)

def word_filter(words: list[str]) -> list[str]:
    word_list = []
    for word in words:
        # if re.match("\n", word):
        word_len_temp = len(word)
        #average word size between 4 and 8 letters
        #bumped up to 3 and 14 for trigram filter
        if word_len_temp < 3 or word_len_temp > 14:
            continue
        #handled ealier
        # if word == '\n':
        #     continue
        #allowance for one special character per word, contractions and sentence punct
        ##a more agressive filter would allow none
        if len(re.findall('[^a-z]',word)) > 1:
            continue
        #average consonant to vowel ratio 60:40, expected random ratio 50:50 a little too close to be useful
        word_list.append(word)

    return word_list

def page_score(body_list: list[str]):
    page_score = 0

    

    for word in body_list:

        if len(word) > 3:
            word_prefix = word[0:3]
            word_suffix = word[len(word)-3:len(word)]
        else:
            word_prefix = word
            word_suffix = word

        if word_prefix in trigram_set:
            page_score +=1

        if word_suffix in trigram_set:
            page_score +=1
        # for tri_key in trigram_set:

        #     if word.find(tri_key) != -1:

        #         page_score += 1
    
    page_tri_ratio = page_score/len(body_list)
    
    page_score_dict = {'page_score': page_score,
                        'page_tri_ratio': page_tri_ratio,
                        }
    return page_score_dict

hex_var = 0
wall = 0
shelf = 0
vol = 0
# page = 0

series = range(0,10)

def wordgen(series=0,shelf=0,hex_var=0,wall=0):
    vol = series
    
    # for vol in series:
    query_dict = {}
    complete_freq_list = []
    defined_list = []

    page_score_sum = 0

    # pages_list = range(410)

    # print(f'{hex_var}:{wall}:{shelf}:{vol}:')
    # logger.info(f'particle hex:wall:shelf {hex_var}:{wall}:{shelf}')

    pages_list = random.sample(range(410), 4)

    query_dict.update({'query_string': f'{hex_var}:{wall}:{shelf}:{vol}:{pages_list}'})
    for page in pages_list:

        query_string = f'{hex_var}:{wall}:{shelf}:{vol}:{page}'
        # print(query_string)
        body = subprocess.run(["python.exe", pybel_cli, '--checkout', query_string], capture_output=True, text=True)
        body = body.stdout

        body = re.sub('Title:.*\n', '', body)
        body = re.sub('\n', ' ', body)
        
        body_list = body.split(' ')

        word_list_filtered = word_filter(body_list)

        # assert len(word_list_filtered) > 0, f'Assertion Error, no words pass filter: {query_string}'

        if len(word_list_filtered) == 0:
            # prevent divzero
            page_score_sum = 0.1
        else:
            page_score_dict = page_score(word_list_filtered)

            page_score_sum = page_score_sum + page_score_dict['page_score']

    if page_score_sum == 0:
        # prevent divzero
        page_score_sum = 0.1

    query_dict.update({'page_score_sum':page_score_sum })

    return query_dict


# if __name__ == '__main__':
    

#     Pool(2).map(wordgen, list(series))



def fitness_function(x, y):

    query_dict_temp = wordgen(hex_var=int(x), wall=int(y))
    # page_score_sum = query_dict_temp['page_score_sum']
    return query_dict_temp




# PSO parameters
max_iterations = 10
grid_size = max(vol_range)*max(shelf_range)
num_particles = int(grid_size/1)
w = 1     # Inertia weight - controls influence of previous velocity
c1 = 2     # Cognitive weight - controls influence of personal best
# c2 = 2     # Social weight - controls influence of global best
c2 = 1

logger.info(f'Weights: Inertia weight w {w}, Cognitive weight c1 {c1}, Social weight c2 {c2}')

# Normalize grid coordinates to appropriate range for fitness function
# For the example function, values between -3 and 3 work well
def normalize_position(pos):
    return (pos / grid_size) * 6 - 3
    # return pos

# Particle class
class Particle:
    def __init__(self):
        # Random initial position (0 to grid_size-1)
        self.position = np.asarray([np.random.randint(min(vol_range),max(vol_range)) , np.random.randint(min(shelf_range),max(shelf_range))])  # [x, y]
        # Random initial velocity
        self.velocity = np.random.uniform(-5, 5, 2)
        # Initialize personal best to initial position
        self.best_position = self.position.copy()
        # Calculate fitness of initial position
        particle_dict = self.evaluate()
        self.best_score = particle_dict['page_score_sum']
    
    def evaluate(self):
        # Normalize position to fitness function domain
        # normalized_pos = normalize_position(self.position)
        return fitness_function(self.position[0], self.position[1])
    
    def update_velocity(self, global_best_position):
        r1 = np.random.random(2) * 10
        r2 = np.random.random(2) * 10
        
        # Update velocity using PSO formula
        cognitive_component = c1 * r1 * (self.best_position - self.position)
        social_component = c2 * r2 * (global_best_position - self.position)
        
        self.velocity = (w* random.randint(1, 2)) * self.velocity + cognitive_component + social_component
        
        # Limit velocity to prevent excessive movement
        self.velocity = np.clip(self.velocity, -15, 15)
    
    def update_position(self):
        # Update position based on velocity
        self.position = self.position + self.velocity.astype(int)
        
        # Keep particles within bounds
        self.position = np.clip(self.position, 0, grid_size-1)
        
        # Evaluate new position
        particle_dict = self.evaluate()
        score = particle_dict['page_score_sum']

        logger.info(f'particle {f'query_sting {particle_dict['query_string']}'}, score {particle_dict['page_score_sum']}')

        
        # Update personal best if current position is better
        if score > self.best_score:
            self.best_score = score
            self.best_position = self.position.copy()
        
        return score

# Main PSO algorithm
def run_pso():
    # Initialize particles
    particles = [Particle() for _ in range(num_particles)]
    
    # Initialize global best
    global_best_position = particles[0].position.copy()
    global_dict = particles[0].evaluate()
    global_best_score = global_dict['page_score_sum']
    
    # Update global best based on all particles' initial positions
    for particle in particles:
        if particle.best_score > global_best_score:
            global_best_score = particle.best_score
            global_best_position = particle.best_position.copy()
    
    
    # Run PSO iterations
    for iteration in range(max_iterations):
        # Create a new figure for this iteration
        plt.figure(figsize=(10, 8))
        
        # Plot fitness landscape as a contour
        # try:
        #     plt.contourf(X, Y, Z, 50, cmap='viridis', alpha=0.5)
        # except:
        #     print(f'X: {X} Y: {Y}, Z: {Z}')
        # plt.colorbar(label='Fitness Value')
        
        # Update all particles
        current_positions = []
        for particle in particles:
            particle.update_velocity(global_best_position)
            score = particle.update_position()

            # Update global best if this particle found a better solution
            if score > global_best_score:
                global_best_score = score
                global_best_position = particle.position.copy()
            
            # Store normalized positions for plotting
            norm_pos = normalize_position(particle.position)
            current_positions.append(norm_pos)

        
        # Convert to numpy array for plotting
        current_positions = np.array(current_positions)
        
        # Plot current particle positions
        plt.scatter(current_positions[:, 0], current_positions[:, 1], 
                   c='red', s=30, alpha=0.7, label='Particles')
        
        # Plot global best position
        norm_global_best = normalize_position(global_best_position)
        plt.scatter(norm_global_best[0], norm_global_best[1], 
                   c='yellow', s=200, marker='*', label='Global Best')
        
        plt.title(f'PSO Iteration {iteration+1}, Best Score: {global_best_score:.4f}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Save the figure
        plt.savefig(f'{pso_iterations_dir}/iteration_{iteration+1:03d}.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Iteration {iteration+1}: Best Score = {global_best_score:.4f} at position {global_best_position}")
    
    print(f"\nOptimization completed.")
    print(f"Best solution found at grid position: {global_best_position}")
    print(f"Normalized position: {normalize_position(global_best_position)}")
    print(f"Best fitness score: {global_best_score:.6f}")

    logger.info(f"\nOptimization completed.")
    logger.info(f"Best solution found at grid position: {global_best_position}")
    logger.info(f"Normalized position: {normalize_position(global_best_position)}")
    logger.info(f"Best fitness score: {global_best_score:.6f}")

    logging.shutdown()


if __name__ == "__main__":
    run_pso()
