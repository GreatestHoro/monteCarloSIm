import matplotlib.pyplot as plt
import random
import numpy as np
import csv
import math
import scipy.integrate as si


class monte_carlo():
    time = 46800
    x = []
    time_x = 0
    time_y = 0
    period = 1
    planes = 1
    k = 0
    l = 0
    total = 0
    prob = 0 
    number_of_planes = [0,16,33,61,41,25,10,8,6,0]
    start = [0,31,61,91,121,151,181,211,241,271]
    end = [30,60,90,120,150,180,210,240,270,300]

    def get_total(self):
        for i in range(len(self.number_of_planes)):
            self.total += self.number_of_planes[i]
        a = self.total
        return a


    def get_k(self, time):
        self.l = self.total/time
        self.k = time * self.l
        print (self.l, self.k, self.total)

    def probality_distribution(self):
        """
        This method calculates the poisson probability distribution, which is given by:
            .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}
        >>> m.get_total()
        200
        >>> m.probality_distribution()
        0.0042552804023591835

        Expecting:
            200
        ok
        Trying:
            m.probality_distribution()
        Expecting:
            0.0042552804023591835
        ok
        """
        self.prob = ((self.total * self.period/self.time)**self.planes)/(np.math.factorial(self.planes)) * 1/np.exp((self.total*self.planes)/self.time)
        a = self.prob
        np.random.poisson()
        return a

    def simulation(self):
        prob_list = []
        arrival = []
        queue = []
        landing_times = []
        count = 0
        no = 0
        for i in range(0, self.time):
            prob_list.append(np.random.choice((1,0), p=(self.prob, 1-self.prob)))
            if prob_list[i] == 1:
                arrival.append(i)
                count += 1
            else:
                no += 1

        prob_interval = []
        prob_interval_adjusted = []
        u = np.random.uniform(0,1)
        for i in range(len(self.number_of_planes)):
            temp = (self.number_of_planes[i])/(30 * self.total)
            temp2 = (self.number_of_planes[i])/self.total
            prob_interval.append(temp)
            prob_interval_adjusted.append(temp2)
            print("[", self.start[i],":", self.end[i],"]:", prob_interval_adjusted[i])

        for i in range(len(prob_list)):
            if prob_list[i] == 1: 
                temp = np.random.choice((1,2,3,4,5,6,7,8,9,10), p=(prob_interval_adjusted))
                prob_list[i] = temp    
        landing_times.extend(prob_list)
        print ("count:", count, no)

        for i in range(len(landing_times)):
            if landing_times[i] == 2:
                temp = np.random.uniform(31,60)
                landing_times[i] = int(temp)
            elif landing_times[i] == 3:
                temp = np.random.uniform(61,90)
                landing_times[i] = int(temp)
            elif landing_times[i] == 4:
                temp = np.random.uniform(91,120)
                landing_times[i] = int(temp)
            elif landing_times[i] == 5:
                temp = np.random.uniform(121,150)
                landing_times[i] = int(temp)
            elif landing_times[i] == 6:
                temp = np.random.uniform(151,180)
                landing_times[i] = int(temp)
            elif landing_times[i] == 7:
                temp = np.random.uniform(181,210)
                landing_times[i] = int(temp)
            elif landing_times[i] == 8:
                temp = np.random.uniform(211,240)
                landing_times[i] = int(temp)
            elif landing_times[i] == 9:
                temp = np.random.uniform(241,270)
                landing_times[i] = int(temp)
        can_land = True
        que_size = []
        waiting_time = []
        for i in range(self.time):
            if len(queue) != 0:
                if queue[0] == i : 
                    queue.pop(0)
                    que_size.append(len(queue))
            if landing_times[i] !=0:
                if len(queue) == 0: 
                    self.time_x = i
                    self.time_y = self.time_x + landing_times[i]
                    queue.append(self.time_y)
                elif len(queue) != 0:
                    if queue[-1] >= i: 
                        diff = queue[-1] - i
                        wait = diff + landing_times[i]
                        waiting_time.append(wait)
                        q = diff + i + landing_times[i]
                        queue.append(q)
                    else: 
                        q = landing_times[i]+ i 
                        queue.append(q)
                
            print("queue length:", len(queue))
        for i in range(len(queue)):
            print ("q", queue[i])


        plt.xlabel("Time")
        plt.ylabel("Probality")
        plt.plot(que_size)
        plt.show()

    def run(self):
        self.get_total()
        self.probality_distribution()
        # self.simulation()


if __name__ == '__main__':
    import doctest 
    doctest.testmod(extraglobs={'m':monte_carlo()})
    m = monte_carlo()
    m.run()