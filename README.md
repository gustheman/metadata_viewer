# metadata_viewer
Just a simple script to inspect TF Lite metadata

# usage
simple use:
```bash
python model_viewer.py \
    model_file=./some_tf_lite_model.tflite
```

to visualize metadata
```bash
python model_viewer.py \
    model_file=./some_tf_lite_model.tflite \
    appended_resource_id=0
```

where appended_resource_id should be the index (0 based) of the appended resource file


