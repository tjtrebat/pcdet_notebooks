# OpenPCDet Notebooks

This repository contains a collection of exploratory Jupyter notebooks for working with the OpenPCDet 3D object detection framework. The goal is to provide a clear, hands-on environment for understanding dataset structure, visualization utilities, and model behavior when working with the KITTI 3D detection benchmark.

These notebooks are not part of the OpenPCDet codebase itself. Instead, they sit alongside it and allow for easier experimentation without modifying the core project.

## Key Features

- Loading and inspecting KITTI dataset samples
- Visualizing point clouds using Open3D
- Rendering ground-truth 3D bounding boxes with class-based colors
- Understanding data preprocessing and augmentation steps used in OpenPCDet models
- Reproducible experiments separate from the main project source tree

--

## Requirements

- Python ≥ 3.8  
- Packages listed in `requirements.txt`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Notebook

1. Set environment variable for X11 (Wayland workaround)

If you are on Linux with Wayland, Open3D’s native rendering may fail. To fix this, set the following environment variable before launching Jupyter:

```bash
export XDG_SESSION_TYPE=x11
jupyter notebook
```

This workaround is described in the Open3D GitHub Issue: [#6872](https://github.com/isl-org/Open3D/issues/6872).

2. Open the Notebook

- Navigate to the notebook in Jupyter.
- Make sure the paths to the KITTI .bin files and images are correct.
- Run the cells. The notebook will load and display the point clouds.
