import matplotlib.pyplot as plt
import random
import copy
import time
import sys
import math
import tkinter
import threading
from functools import reduce
import numpy as np
import pandas as pd
import csv

Start_City = 0
(ALPHA, BETA, RHO, Q) = (1.0,2.0,0.5,100.0)
(city_num, ant_num) = (100,50)
distance_x = [208,66,98,243,301,17,616,16,289,611,538,572,547,47,470,789,731,680,108,644,519,792,104,29,466,406,521,436,461,87,792,133,161,525,528,214,465,106,778,206,724,537,120,81,116,742,781,534,744,386,362,786,177,530,769,168,363,601,265,721,309,590,630,792,336,755,756,592,510,273,391,649,248,428,604,725,791,164,730,257,26,318,294,413,700,508,689,396,230,542,111,282,557,222,793,212,715,499,712,531]
distance_y = [11,754,245,583,369,500,663,498,459,695,65,272,247,494,372,6,267,633,343,371,632,106,408,386,0,385,770,706,114,230,786,172,515,750,28,606,81,245,253,676,573,642,45,565,220,114,193,758,722,624,39,332,330,119,365,278,35,465,158,724,798,62,215,568,153,179,344,139,627,96,89,374,128,552,346,429,515,684,502,752,74,367,632,587,328,394,282,745,678,16,475,377,466,703,145,397,159,617,577,247]

distance_graph = [[0.0 for col in range(city_num)] for raw in range(city_num)]
pheromone_graph = [[1.0 for col in range(city_num)] for raw in range(city_num)]

BASE_EVAPORATION_RATE = 0.5
SENSITIVITY_FACTOR = 0.1

class Ant(object):
    def __init__(self,ID):
        self.ID = ID
        self.__clean_data()

    def __clean_data(self):
        self.path = []
        self.total_distance = 0.0
        self.move_count = 0
        self.current_city = -1
        self.open_table_city = [True for i in range(city_num)]
        city_index = Start_City if Start_City is not None else random.randint(0,city_num-1)
        self.current_city = city_index
        self.path.append(city_index)
        self.open_table_city[city_index] = False
        self.move_count = 1

    def __choice_next_city(self):
        next_city = -1
        select_citys_prob = [0.0 for i in range(city_num)]
        total_prob = 0.0
        for i in range(city_num):
            if self.open_table_city[i]:
                try :
                    select_citys_prob[i] = pow(pheromone_graph[self.current_city][i], ALPHA) * pow((1.0/distance_graph[self.current_city][i]), BETA)
                    total_prob += select_citys_prob[i]
                except ZeroDivisionError as e:
                    print ('Ant ID: {ID}, current city: {current}, target city: {target}'.format(ID = self.ID, current = self.current_city, target = i))
                    sys.exit(1)
        if total_prob > 0.0:
            temp_prob = random.uniform(0.0, total_prob)
            for i in range(city_num):
                if self.open_table_city[i]:
                    temp_prob -= select_citys_prob[i]
                    if temp_prob < 0.0:
                        next_city = i
                        break
        if (next_city == -1):
            next_city = random.randint(0, city_num - 1)
            while ((self.open_table_city[next_city]) == False):
                next_city = random.randint(0, city_num - 1)
        return next_city

    def __cal_total_distance(self):
        temp_distance = 0.0
        for i in range(1, city_num):
            start, end = self.path[i], self.path[i-1]
            temp_distance += distance_graph[start][end]
        end = self.path[0]
        temp_distance += distance_graph[start][end]
        self.total_distance = temp_distance

    def __move(self, next_city):
        self.path.append(next_city)
        self.open_table_city[next_city] = False
        self.total_distance += distance_graph[self.current_city][next_city]
        self.current_city = next_city
        self.move_count += 1

    def search_path(self):
        self.__clean_data()
        while self.move_count < city_num:
            next_city = self.__choice_next_city()
            self.__move(next_city)
        self.__cal_total_distance()

class TSP(object):
    def __init__(self, width=800, height=600, n=city_num, enhanced=False):
        self.width = width
        self.height = height
        self.n = n
        self.__r = 5
        self.__lock = threading.RLock()
        self.best_result = []
        self.avg_result = []
        self.enhanced = enhanced
        self.new()
        for i in range(city_num):
            for j in range(city_num):
                temp_distance = pow((distance_x[i] - distance_x[j]), 2) + pow((distance_y[i] - distance_y[j]), 2)
                temp_distance = pow(temp_distance, 0.5)
                distance_graph[i][j] =float(int(temp_distance + 0.5))

    def new(self, evt=None):
        self.__lock.acquire()
        self.__running = False
        self.__lock.release()
        self.nodes = []
        self.nodes2 = []
        for i in range(city_num):
            for j in range(city_num):
                pheromone_graph[i][j] = 1.0
        self.ants = [Ant(ID) for ID in range(ant_num)]
        self.best_ant = Ant(-1)
        self.best_ant.total_distance = 1 << 31
        self.iter = 1
        self.best_result.append([])
        self.avg_result.append([])

    def search_path(self, csv_filename, evt=None):
        self.__lock.acquire()
        self.__running = True
        self.__lock.release()
        best_result = []
        avg_result = []
        st = time.time()
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['Iteration', 'Best_Distance']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            while self.iter < 1001:
                tmp_avg_result = []
                for ant in self.ants:
                    ant.search_path()
                    tmp_avg_result.append(ant.total_distance)
                    if ant.total_distance < self.best_ant.total_distance:
                        self.best_ant = copy.deepcopy(ant)
                self.avg_result[-1].append(sum(tmp_avg_result) / len(tmp_avg_result))
                self.best_result[-1].append(self.best_ant.total_distance)
                self.__update_pheromone_gragh()
                print(u"迭代次数：", self.iter, u"最佳路径总距离：", int(self.best_ant.total_distance))
                csv_writer.writerow({'Iteration': self.iter, 'Best_Distance': int(self.best_ant.total_distance)})
                self.iter += 1
        print(f'第{len(self.avg_result)}轮跑数结束，耗时：{time.time() - st}s')

    def __calculate_path_length_variance(self):
        path_lengths = [ant.total_distance for ant in self.ants]
        mean_length = sum(path_lengths) / len(path_lengths)
        variance = sum((l - mean_length) ** 2 for l in path_lengths) / len(path_lengths)
        return variance

    def __update_pheromone_gragh(self):
        if self.enhanced:
            path_variance = self.__calculate_path_length_variance()
            dynamic_evaporation_rate = BASE_EVAPORATION_RATE * (1 - math.exp(-SENSITIVITY_FACTOR * path_variance))
            temp_pheromone = [[0.0 for _ in range(city_num)] for _ in range(city_num)]
            for ant in self.ants:
                for i in range(1, city_num):
                    start, end = ant.path[i-1], ant.path[i]
                    temp_pheromone[start][end] += Q / ant.total_distance
                    temp_pheromone[end][start] = temp_pheromone[start][end]
            for i in range(city_num):
                for j in range(city_num):
                    pheromone_graph[i][j] = (pheromone_graph[i][j] * (1 - dynamic_evaporation_rate)) + temp_pheromone[i][j]
        else:
            temp_pheromone = [[0.0 for _ in range(city_num)] for _ in range(city_num)]
            for ant in self.ants:
                for i in range(1, city_num):
                    start, end = ant.path[i - 1], ant.path[i]
                    temp_pheromone[start][end] += Q / ant.total_distance
                    temp_pheromone[end][start] = temp_pheromone[start][end]
            for i in range(city_num):
                for j in range(city_num):
                    pheromone_graph[i][j] = pheromone_graph[i][j] * RHO + temp_pheromone[i][j]

    def write(self, evt=None):
        multi_avg_result = []
        multi_best_result = []
        for j in range(len(self.avg_result[0])):
            tmp_avg = 0
            tmp_best = np.inf
            for i in range(len(self.avg_result)):
                tmp_avg += self.avg_result[i][j]
                if tmp_best > self.best_result[i][j]:
                    tmp_best = self.best_result[i][j]
            multi_avg_result.append(tmp_avg / len(self.avg_result))
            multi_best_result.append(tmp_best)
        df = pd.DataFrame()
        df.loc[:, "avg"] = multi_avg_result
        df.loc[:, "best"] = multi_best_result
        if self.enhanced:
            df.to_csv(f"./{len(self.avg_result)}_rounds_enhanced_result.csv", index=False)
        else:
            df.to_csv(f"./{len(self.avg_result)}_rounds_original_result.csv", index=False)
        plt.figure()
        plt.title(f'{len(self.avg_result)} rounds')
        plt.plot(multi_avg_result)
        plt.plot(multi_best_result)
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    original_tsp = TSP()
    original_tsp.search_path('yqoriginal_algorithm_results.csv')
    original_tsp.write()

    enhanced_tsp = TSP(enhanced=True)
    enhanced_tsp.search_path('yqenhanced_algorithm_results.csv')
    enhanced_tsp.write()

    original_results = pd.read_csv('yqoriginal_algorithm_results.csv')
    enhanced_results = pd.read_csv('yqenhanced_algorithm_results.csv')

    plt.figure()
    plt.plot(original_results['Iteration'], original_results['Best_Distance'], label='Original')
    plt.plot(enhanced_results['Iteration'], enhanced_results['Best_Distance'], label='Enhanced Dynamic Pheromone')
    plt.xlabel('Iteration')
    plt.ylabel('Best Distance')
    plt.title('Comparison of Original and Enhanced Dynamic Pheromone Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

    original_avg_result = pd.read_csv('100_rounds_original_result.csv')
    enhanced_avg_result = pd.read_csv('100_rounds_enhanced_result.csv')

    plt.figure()
    plt.plot(original_avg_result['avg'], label='Original')
    plt.plot(enhanced_avg_result['avg'], label='Enhanced Dynamic Pheromone')
    plt.xlabel('Iteration')
    plt.ylabel('Average Distance')
    plt.title('Comparison of Average Distance')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(original_avg_result['best'], label='Original')
    plt.plot(enhanced_avg_result['best'], label='Enhanced Dynamic Pheromone')
    plt.xlabel('Iteration')
    plt.ylabel('Best Distance')
    plt.title('Comparison of Best Distance')
    plt.legend()
    plt.grid(True)
    plt.show()

    original_best_distance = original_avg_result['best'].min()
    enhanced_best_distance = enhanced_avg_result['best'].min()
    original_avg_distance = original_avg_result['avg'].mean()
    enhanced_avg_distance = enhanced_avg_result['avg'].mean()

    comparison_table = pd.DataFrame({
        'Algorithm': ['Original', 'Enhanced Dynamic Pheromone'],
        'Best Distance': [original_best_distance, enhanced_best_distance],
        'Average Distance': [original_avg_distance, enhanced_avg_distance]
    })

    print("Comparison Table:")
    print(comparison_table)