import os
import argparse
import numpy as np

#from wrapper.GenericWrapper4AC_master.domain_specific.satwrapper import SatWrapper


class Glucose_Wrapper():

    def get_command_line_args(self, runargs, config):
            
        instance = runargs["instance"]
        configuration =""
    
        for param, value in config.items():
            if value == True and isinstance(value, (bool, np.bool_))  : #is True and type(value) == bool
                configuration += f"-{param} "
            elif value == False and isinstance(value, (bool, np.bool_)): #is False and type(value) == bool
                configuration += f"-no-{param} "
            else:
                configuration = configuration + f"-{param}={value} "

        instance_p = f'"./input/{instance}"'
        exc = './input/target_algorithms/Open-WBO-Inc-master/open-wbo-inc'

        
        cmd = f'stdbuf -oL {exc} {instance_p} -verbosity=1 -rnd-seed={runargs["seed"]} {configuration}'
        return cmd

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=dict)
    parser.add_argument("--runargs", type=dict)


    wrapper = GLucoseWrapper()
    print(wrapper.get_command_line_args(parser.runargs, parser.config))

