#creates json file with settings for multiple clicker runs
import json
from re import I
#from threading import local
from time import localtime, strftime

job_type = 'multiple simulation setup'
time_string = strftime('%Y-%m-%d %H:%M:%S', localtime())

joblist = {
    'type': job_type,
    'time': time_string,
    'jobs': []
}

def add_job(procedure = 'mesh.txt', vtk = 'M1.vtk', flow = 're150.flow', mesh_size = 0.5, curvature_refinement = False, upper_param = 0.15,
    lower_param = 0.1, num_steps = 70000, step_size = 0.0001, viscosity = 1, density = 0.00094, restart_steps = 1000, residual_control = True,
    step_construction = 2, influx_coefficient = 0.8):
    joblist['jobs'].append(
        {
            'procedure': procedure,
            'vtk': vtk,
            'flow': flow,
            'mesh': { 
                'mesh_size': mesh_size,
                'curvature_refinement': curvature_refinement,
                'upper_param': upper_param,
                'lower_param': lower_param
            },
            'solver': {
                'num_steps': num_steps,
                'step_size': step_size,
                'viscosity': viscosity,
                'density': density,
                'restart_steps': restart_steps,
                'residual_control': residual_control,
                'step_construction': step_construction,
                'influx_coefficient': influx_coefficient
            }
        }
    )

def write_json(name = 'joblist.json'):
    with open(name, 'w') as file:
        json.dump(joblist, file, indent = 4)

if __name__ == '__main__':
    add_job()
    write_json()