# Breast Cancer Prediction

## About Dataset:
* Features are computed from a digitized image of a fine needle aspirate  (FNA) of a breast mass.  They describecharacteristics of the cell nuclei present in the image.

### Features information:

* Radius (mean of distances from center to points on the perimeter): This feature represents the average distance from the center of the tumor to points on its perimeter.

* Texture (standard deviation of gray-scale values): This feature measures the variation in gray-scale intensities of the pixels in the image of the tumor.

* Perimeter: This feature represents the total length of the tumor's perimeter.

* Area: This feature denotes the area enclosed by the tumor's perimeter.

* Smoothness (local variation in radius lengths): This feature captures the variation in the local radius lengths of the tumor.

* Compactness (perimeter^2 / area - 1.0): This feature is calculated by dividing the square of the perimeter by the area of the tumor and subtracting 1.0. It represents how compact or tightly packed the tumor is.

* Concavity (severity of concave portions of the contour): This feature measures the severity of concave portions of the tumor's contour.

* Concave points (number of concave portions of the contour): This feature counts the number of concave portions in the tumor's contour.

* Symmetry: This feature represents the symmetry of the tumor, specifically the symmetry of the shape formed by dividing the tumor into two halves.

* Fractal dimension ("coastline approximation" - 1): This feature is calculated based on the "coastline approximation" of the tumor, which captures the complexity of the tumor's shape.

### We have 30 indpendent/input features:
1 - 'mean radius' 
2 - 'mean texture' 
3 - 'mean perimeter' 
4 - 'mean area'
5 - 'mean smoothness' 
6 - 'mean compactness' 
7 - 'mean concavity'
8 - 'mean concave points' 
9 - 'mean symmetry' 
10 -'mean fractal dimension'
11 -'radius error' 
12 -'texture error' 
13 -'perimeter error' 
14 -'area error'
15 -'smoothness error' 
16 -'compactness error' 
17 -'concavity error'
18 -'concave points error' 
19 -'symmetry error' 
20 -'fractal dimension error'
21 -'worst radius' 
22 -'worst texture' 
23 -'worst perimeter' 
24 -'worst area'
25 -'worst smoothness' 
26 -'worst compactness' 
27 -'worst concavity'
28 -'worst concave points' 
29 -'worst symmetry' 
30 -'worst fractal dimension'

### We have 1 dependent/output features:
* These output feature has 2 classes:
* >>  WDBC-Malignant - represented by 1
* >>  WDBC-Benign    - represented by 0

* WDBC-Malignant : This class represents malignant tumors, which are cancerous and can invade surrounding tissues. Malignant tumors have the potential to spread to other parts of the body, a process known as metastasis.

* WDBC-Benign : This class represents benign tumors, which are non-cancerous and do not invade surrounding tissues. Benign tumors do not spread to other parts of the body.

