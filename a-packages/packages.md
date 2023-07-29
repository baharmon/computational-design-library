# Packages

## Miniconda
Download and install [minconda](https://docs.conda.io/en/latest/miniconda.html).
On Windows open the Anaconda Prompt. On Mac or Linux open Terminal.

## Spyder
Install the Spyder IDE in a dedicated environment.
```
conda init bash
conda update -n base conda
conda config --env --set channel_priority strict
conda create -c conda-forge -n spyder-env spyder numpy scipy pandas matplotlib sympy cython
conda activate spyder-env
```

Activate the environment and run Spyder.
```
conda activate spyder-env
spyder
```

## Computational Design
Create a new environment and install the neccessary packages.
```
conda create -n computational-design -c conda-forge spyder-kernels scipy seaborn rasterio lazrs-python laspy pyntcloud pyvista viscm colorspacious cmcrameri cmasher colorcet cmocean
```

Then use Pip to install packages that are not available through Conda. The package [pyfastnoisesimd](https://pypi.org/project/pyfastnoisesimd/) requires Microsoft Visual C++ 14.0 or greater. Go to [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Download and run Visual Studio Build Tools installer. In the installer, check `Desktop development with C++` and then install.
```
conda activate computational-design
pip install lidario pyfastnoisesimd cellpylib
```

Set this environment as the Python interpreter for Spyder. First find the Python path of the environment with `where python`. Activate the Spyder environment, start Spyder, open its preferences, and set this path for the Python interpreter. Restart Spyder.
```
where python
conda deactivate
conda activate spyder-env
spyder
```

## Open3D
Create a dedicated environment for Open3D.
```
conda create -n open3d -c conda-forge -c open3d-admin open3d spyder-kernels
```


