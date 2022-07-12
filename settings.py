#creates json file with settings for multiple clicker runs
import json
from re import I
from threading import local
from time import localtime, strftime

job_type = 'multiple simulation setup'
time_string = strftime('%Y-%m-%d %H:%M:%S', localtime())

joblist = {
    'type': job_type,
    'time': time_string,
    'jobs': []
}

def add_job(procedure = 'test.txt', vtk = 'M0', flow = 're150', mesh_size = 0, curvature_refinement = False, 
    num_steps = 0, step_size = 0, residual_control = False, step_construction = False, influx_coefficient = 0):
    joblist['jobs'].append(
        {
            'procedure': procedure,
            'vtk': vtk,
            'flow': flow,
            'mesh': { 
                'mesh_size': mesh_size,
                'curvature_refinement': curvature_refinement
            },
            'solver': {
                'num_steps': num_steps,
                'step_size': step_size,
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