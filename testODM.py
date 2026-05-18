import os
from pyodm import Node

import aspose.threed as a3d


n = Node('localhost', 3000)
images = []
directory = os.fsencode('Images')
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
        print(os.path.join('Images/', filename))
        images.append(os.path.join('Images/', filename))
        continue
    else:
        continue
task = n.create_task(images, {'dsm': True})
task.wait_for_completion()
os.listdir(task.download_assets("results"))[0:2]


a3d.TrialException.set_suppress_trial_exception(True)
scene = a3d.Scene.from_file("results/odm_texturing/odm_textured_model_geo.obj")
scene.save("World.dae")