import os

import config

Executable_file = 'run%d.sh' % (config.version)
submit_config_file = """+Group="GRAD"
+Project="AI_ROBOTICS"
+ProjectDescription="3d-colorization"
+GPUJob=true
Requirements=(TARGET.GPUSlot) && (TARGET.MACHINE=="eldar-11.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-12.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-13.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-14.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-15.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-17.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-18.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-19.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-20.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-21.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-22.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-23.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-24.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-25.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-26.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-27.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-28.cs.utexas.edu" \\
             || TARGET.MACHINE=="eldar-29.cs.utexas.edu")
Rank=memory
Environment=PATH=/lusr/opt/condor/bin/:/lusr/opt/condor/bin/:/opt/cuda-8.0/bin:$PATH
Environment=PYTHONPATH=/u/leonliu/.local/lib/python2.7/site-packages:$PYTHONPATH
Environment=LD_LIBRARY_PATH=/u/leonliu/repos/cuDNN:/u/leonliu/repos/cuDNN/lib64:/opt/cuda-8.0/lib:/opt/cuda-8.0/lib64:$LD_LIBRARY_PATH

Universe=vanilla
Getenv=True

Log=../../outputs/log/log.$(Cluster).$(Process) 
Output=../../outputs/log/out.$(Cluster).$(Process) 
Error=../../outputs/log/err.$(Cluster).$(Process)
Executable=%s


Queue 1
""" % (Executable_file)


with open('condor_submit', 'w') as f:
	f.write(submit_config_file)
print 'condor_submit generated'

with open(Executable_file, 'w') as f:
	f.write("""#!/bin/bash
# python train.py
python visNet.py
""")
print Executable_file, 'generated'
os.system('chmod 755 %s'%(Executable_file))

print 'submit'
os.system("condor_submit condor_submit")






