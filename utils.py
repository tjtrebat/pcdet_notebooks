import numpy as np


def parse_label_file(label_file_path):
    parsed_labels = []
    with open(label_file_path, "r") as file:
        for line in file:
            line_elements = line.strip().split()
            if len(line_elements) != 15:
                raise ValueError(f"Line does not match expected format: {line.strip()}")
            label = {
                'type': line_elements[0],
                'truncated': float(line_elements[1]),
                'occluded': int(line_elements[2]),
                'alpha': float(line_elements[3]),
                'bbox_2d': tuple(float(bbox_2d_dim) for bbox_2d_dim in line_elements[4:8]),
                'dimensions': tuple(float(dim) for dim in line_elements[8:11]),
                'location': tuple(float(loc) for loc in line_elements[11:14]),
                'rotation_y': float(line_elements[14])
            }
            parsed_labels.append(label)
    return parsed_labels


def parse_calib_file(calib_file_path):
    calib_keys = ['P0', 'P1', 'P2', 'P3', 'R0','Tr_velo_to_cam', 'Tr_imu_to_velo']
    calibration_matrices = dict()
    with open(calib_file_path, "r") as file:
        calib_lines = file.readlines()
        for i, key in enumerate(calib_keys):
            elems = calib_lines[i].split(' ')
            elems = elems[1:]
            calib_matrix = np.array(elems, dtype=np.float32)
            if key == 'R0':
                calib_matrix_shape = (3, 3)
            else:
                calib_matrix_shape = (3, 4)
            calib_matrix = calib_matrix.reshape(calib_matrix_shape)
            calibration_matrices[key] = calib_matrix
    return calibration_matrices
