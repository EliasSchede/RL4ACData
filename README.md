**Supplementary material to the article:**

## Deep reinforcement learning for instance-specific algorithm configuration
<br>

### Configuration scenarios
 
We provide links to the use target algorithms:

+ **[Loandra](https://github.com/jezberg/loandra):** Version 1.0 [1]  
+ **[WBO](https://github.com/sbjoshi/Open-WBO-Inc):** [2]
+ **[CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio):** Version: 22.1.1.0 [3]  
+ **[KISSAT](https://github.com/arminbiere/kissat):** Version 3.1.1 [4]  
+ **[Glucose](https://github.com/audemard/glucose):** Version 4.1  
+ **[CaDiCaL](https://github.com/arminbiere/cadical)** Version: Sc17

Each configuration scenario contains:  
+ Training and test instance files and features;  
+ Scenario and argument files;  
+ Wrapper that is used by the method to create the target algorithm cmds to execute it.

***

### Get the instances

Instances can be obtained from:
+ CVRP [5] and MIP[6]  can be downloaded from [here](https://zenodo.org/records/14515806?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjllNTYwNDBlLThkZjItNGJhOS04Zjc4LTJjODVkMjU4NmY2MSIsImRhdGEiOnt9LCJyYW5kb20iOiIyYmNiYjVmZjFhNWMwMTI1NmI0MjQ5ZGY0NGQ5MTA1YiJ9.p0cZ7dgnbi4oj6rTTztYB3w4_pXStOLlJoKOF9UYX80gCc9t_cpgkUcSYdQsbB03S6bgPCGsLg3tzjCgujp0Yw)
+ [MaxSAT](http://www.cs.toronto.edu/maxsat-lib/maxsat-instances/master-set/unweighted/) [7]  
+ [ACLIB](https://bitbucket.org/mlindauer/aclib2/src/master/) [8]  


### References

[1] Berg, J., Demirović, E., and Stuckey, P. J. (2019). Core-boosted linear search for incomplete MaxSAT. In Integration of Constraint Programming, Artificial Intelligence, and Operations Research, pages 39–56. Springer.

[2] Nadel, A. (2018). Solving MaxSAT with bit-vector optimization. In Theory and Applications of Satisfiability Testing, pages 54–72. Springer.

[3] IBM (2022). ILOG CPLEX optimization studio 22.1.1: User’s manual.

[4] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, and F. Pollitt. "CaDiCaL, Gimsatul, IsaSAT, and Kissat Entering the SAT Competition 2024." In Proceedings of SAT Competition 2024 — Solver, Benchmark and Proof Checker Descriptions, vol. B-2024-1, pp. 8–10. University of Helsinki, 2024.

[5] Kool, W., van Hoof, H., and Welling, M. (2019). Attention, Learn to Solve Routing Problems! In International Conference on Learning Representations, ICLR.

[6] Merschformann, M. (2024). SardineCan. https://github.com/merschformann/sardine-can, commit fa7ccc7.

[7] Bacchus, F., Berg, J., Järvisalo, M., and Martins, R. (2020). MaxSAT evaluation 2020: Solver and benchmark descriptions.

[8] F. Hutter, M. López-Ibáñez, C. Fawcett, M. Lindauer, H. H. Hoos, K. Leyton-Brown, and T. Stützle. "AClib: A Benchmark Library for Algorithm Configuration." In Learning and Intelligent Optimization, pp. 36–40. Springer, 2014.