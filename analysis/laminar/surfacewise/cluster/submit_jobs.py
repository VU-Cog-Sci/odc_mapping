from itertools import product
import os
import os.path as op


subject_session = [('bm', 'odc'), 
                   ('eo', 'odc'),
                   ('de', 'odc1'),
                   ('ms', 'odc2'),
                   ('ns', 'odc'),
                   ('tk', 'odc2'),
                   ('tk', 'odc3'),
                   ('tr', 'odc')]

n_vertices = [12, 25, 50, 100, 200, 400, 800, 1600]
masks = ['V1', 'V1l', 'V1r', 'V1_shortwl', 'V1l_shortwl', 'V1r_shortwl']


for (subject, session), n_vertex, mask in product(subject_session[:], n_vertices, masks):
    print(subject, session, n_vertex)

    job_file = op.join(os.environ['HOME'],
                       'batch_scripts',
                       '{subject}_{session}_{n_vertex}.sh').format(**locals())

    name = '{subject}_{session}_{n_vertex}_{mask}.sh'.format(**locals())

    with open(job_file, 'w') as fh:
        fh.writelines("#!/bin/bash\n")
        fh.writelines("#SBATCH --job-name=%s.job\n" % name)
        fh.writelines("#SBATCH --output=%s/.out/%s.out\n" % (os.environ['HOME'], name))
        fh.writelines("#SBATCH --error=%s/.out/%s.err\n" % (os.environ['HOME'], name))
        fh.writelines("#SBATCH --time={}:00:00\n".format(int(1 + 2 * 12./400. * n_vertex)))

        if n_vertex > 100:
            fh.writelines("#SBATCH --partition=gpu\n")
        #fh.writelines("#SBATCH --mail-type=ALL\n")
        #fh.writelines("#SBATCH --mail-user=gilles.de.hollander@gmail.com\n")

        fh.writelines("source $HOME/.bashrc\n")
        if n_vertex > 100:
            fh.writelines("conda activate tf_gpu\n")
        else:
            fh.writelines("conda activate tf_cpu\n")

        fh.writelines("export MKL_NUM_THREADS=20\n")
        fh.writelines("python $HOME/git/odc_mapping/analysis/laminar/surfacewise/test_encoding_model.py {subject} {session} --sourcedata $HOME/sourcedata --derivatives $HOME/derivatives --n_vertices {n_vertex} --description {mask}_{n_vertex} --no-progressbar --masks {mask}\n".format(**locals()))

    os.system("sbatch %s" %job_file)
