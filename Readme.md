

Sample script for submitting [ray](https://docs.ray.io/en/latest/index.html) jobs on biowulf
======================================================================

- The submit script was adapted from the submit script in the [ray documentation](https://docs.ray.io/en/latest/cluster/slurm.html#submitting-your-script). The example python scripts are from the ray repository.
- I could not get ray to work properly with more than one task per node.
  The task doesn't have to be exclusive but in realistic examples it probably
  would be. In this example it is not.
- Use `--tasks-per-node` and `--nnodes` to determine the number of worker
  processes.
- Use `--cpus-per-task` and `--gpus-per-task` to determine the number of CPUs
  and GPUs. If you allocate exclusively, please also allocate all resources.
- For real multinode jobs submit to the multinode partition. This simple example
  is fine on the quick partition.


To submit:

```
git clone https://github.com/NIH-HPC/biowulf_ray.git
sbatch submit-ray
```
