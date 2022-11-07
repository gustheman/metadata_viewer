# Description
Just a simple script to inspect TF Lite metadata

# Usage
simple use:
```bash
python metadata_viewer.py \
    model_file=./some_tf_lite_model.tflite
```

to visualize metadata
```bash
python metadata_viewer.py \
    model_file=./some_tf_lite_model.tflite \
    appended_resource_id=0
```

where appended_resource_id should be the index (0 based) of the appended resource file

# Helper function 
If you just want to get the label names that are embedded within the .tflite file (*i.e like for edge models trained in Google Cloud AutoML*) then you can use this helper function:

```python
import zipfile
from tflite_support import metadata

def get_labels_from_tflite(model_file_name, format=0):
  '''
  Unpack the metadata from a tflite model and return and parse the first 
  associated file which is assumed to be the label file.
  input : str (model file name), int (format 0=list, 1=dict)
  output : str (text from labels file)
  '''

  displayer = metadata.MetadataDisplayer.with_model_file(model_file_name)
  associate_files= displayer.get_packed_associated_file_list()
  resource_file = associate_files[0]
  archive = zipfile.ZipFile(model_file_name, 'r')
  labels = archive.read(resource_file).decode().split('\n')

  if format == 1:
    labels = {i:label  for (i, label) in enumerate(labels)}

  return labels
  
  
# Example usage
# get labels as  list >> ["cat", "dog", "mouse"]
labels_list = get_labels_from_tflite('my_model.tflite', format=0)

# get labels as  dict >> {0:"cat", 1:"dog", 2:"mouse"}
labels_dict = get_labels_from_tflite('my_model.tflite', format=1)
 
```


# Resources
Oficial documentation for [TF Lite metadata](https://www.tensorflow.org/lite/convert/metadata)

