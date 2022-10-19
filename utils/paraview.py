from paraview.simple import *
import sys
import os

# path = sys.argv[1]
path= '<path to your case.foam output file downloaded from SimScale >'

# directory=sys.argv[2]
directory='<path to your output folder>'

decompose = False # The optional decompose flag means that the project should be open as a decomposed case. 
                # If you don't know if your is, check wether it has multiple "processorN" subfolders. If it does have them, it is decomposed.

# create a new 'OpenFOAMReader'
foamReader = OpenFOAMReader(FileName=path)

# Properties modified on foamReader
if decompose:
    foamReader.CaseType = 'Decomposed Case'

foamReader.UpdatePipeline()
foamReader.UpdatePipelineInformation()

# Properties modified on foamReader
foamReader.MeshRegions = ['internalMesh']
foamReader.CellArrays = ['U']
foamReader.UpdatePipeline()

# create a new 'Cell Centers'
cellCenters1 = CellCenters(Input=foamReader)

# Properties modified on cellCenters1
cellCenters1.VertexCells = 1
cellCenters1.UpdatePipeline()

# save data
if not os.path.exists(directory):
    os.makedirs(directory)

# SaveData(directory+"/"+sys.argv[2]+".csv", proxy=cellCenters1, WriteAllTimeSteps=1)
SaveData(directory+"/"+'wind_at_cell_centers'+".csv", proxy=cellCenters1, WriteAllTimeSteps=1)
