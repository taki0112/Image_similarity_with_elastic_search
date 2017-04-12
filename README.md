# Image_match
## Find the original image of the converted image
* Python implementation of [image_match](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.2585&rep=rep1&type=pdf) papers

## Requirements
* Python 3.5
* [Elasticsearch 5.3.0](https://www.elastic.co/kr/downloads/elasticsearch)
* image_match
* numpy+mkl
* scipy

## library download
* [link](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

## How to install the library
Please follow the order
```bash
use "pip install"
1. pip install elasticsearch
2. pip install scipy~.whl
3. pip install numpy+mkl~.whl
4. pipinstall image_match
```

# Code (Similarity between 2 images)
```bash
from image_match.goldberg import ImageSignature

gis = ImageSignature()
a = gis.generate_signature(image_path_1)
b = gis.generate_signature(image_path_2)
print(gis.normalized_distance(a, b))
```

If you want to get similarity between many images, See github code

## Reference
* [image-match](http://image-match.readthedocs.io/en/latest/)

