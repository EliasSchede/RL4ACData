import os
import argparse
import numpy as np
import random

#from wrapper.GenericWrapper4AC_master.domain_specific.satwrapper import SatWrapper


class Glucose_Wrapper():

    def get_command_line_args(self, runargs, config):
            
        instance = runargs["instance"]
        configuration =""
    
        for param, value in config.items():
                if isinstance(value, str):
                    value = value.replace(" ", "")
                if value == True and isinstance(value, (bool, np.bool_)):
                    value = "true"
                elif value == False and isinstance(value, (bool, np.bool_)):
                    value = "false"
                configuration += f" --{param}={value}"

        instance_p = f'"./input/{instance}"'
        exc = "./input/target_algorithms/kissat-master/build/kissat"

        
        cmd = f'stdbuf -oL {exc} {instance_p} ' \
              f'{configuration} --quiet --definitioncores=1 --seed={random.randint(1,10000)}'
        return cmd

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=dict)
    parser.add_argument("--runargs", type=dict)


    wrapper = GLucoseWrapper()
    print(wrapper.get_command_line_args(parser.runargs, parser.config))

