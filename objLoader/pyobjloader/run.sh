set -e

# original obj
# python obj2pov.py tmp/model_normalized.obj tmp/model.inc
# cd tmp
# povray -H900 -W1200 +A +D +omycar.png  mycar.pov
# cd ..

# obj with overlapped triangles removed
python rm_overlapped_meshes.py tmp/model_normalized.obj
python obj2pov.py tmp/model_normalized.obj.rm.obj tmp/model.inc
cd tmp
povray -H900 -W1200 +A +D +omycar.rm.png  mycar.pov
cd ..

# obj from voxel.npy
python vox2obj_gsemantic.py tmp/model_normalized.obj.64.labpoints.npy tmp/model_normalized.obj.rm.obj tmp/model_from_vox
python obj2pov.py tmp/model_from_vox.obj tmp/model.inc
cd tmp
povray -H900 -W1200 +A +D +omycar.vae.png  mycar.pov
cd ..