"""
TF Lite Metadata viewer
author: gustheman
"""

import os
import zipfile
from tflite_support import metadata as _metadata
from absl import app, flags

FLAGS = flags.FLAGS


def define_flags():
    """
    description:
    """
    flags.DEFINE_string("model_file", None,
                        "Path and file name of the TFLite model file.")
    flags.DEFINE_integer("appended_resource_id", None,
                         "Appended resource file to print")
    flags.mark_flag_as_required("model_file")
    flags.register_validator("model_file",
                             lambda value: os.path.exists(value),
                             message="model_file does not exists")


def show_json_metadata(model_file):
    """
    description:
    """
    try:
        displayer = _metadata.MetadataDisplayer.with_model_file(model_file)
        json_file = displayer.get_metadata_json()
        print(json_file)
        associate_files = displayer.get_packed_associated_file_list()
        print(associate_files)
    except ValueError as exp:
        print(exp)


def show_appended_resource(model_file, resource_id):
    """
    description:
    """
    try:
        displayer = _metadata.MetadataDisplayer.with_model_file(model_file)
        associate_files = displayer.get_packed_associated_file_list()
        if resource_id > len(associate_files) - 1:
            raise ValueError(
                ("resource id not valid ({}). this model has only {}" +
                 " resources (0 based index)").
                format(resource_id, len(associate_files)))
        resource_file = associate_files[resource_id]
        archive = zipfile.ZipFile(model_file, 'r')
        labels0 = archive.read(resource_file)
        print(labels0.decode())
    except ValueError as exp:
        print(exp)


def main(_):
    """
    description: The main function
    """
    model_file = FLAGS.model_file

    if FLAGS.appended_resource_id is not None:
        show_appended_resource(model_file, FLAGS.appended_resource_id)
    else:
        show_json_metadata(model_file)


if __name__ == "__main__":
    define_flags()
    app.run(main)
