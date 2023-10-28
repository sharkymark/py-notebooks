# Jupyter Notebook machine learning and data science example

This repo shows 2 sample Jupyter Notebooks and Python code.  

###### coder-oss.demo.coder.com
[![Open in Coder](https://coder-oss.demo.coder.com/open-in-coder.svg)](https://coder-oss.demo.coder.com/templates/pod-with-jupyter/workspace?mode=auto&param.Jupyter+IDE+type=lab&param.Dotfiles+URL+%28optional%29=)

###### eks-v2.demo.coder.com
[![Open in Coder](https://eks-v2.demo.coder.com/open-in-coder.svg)](https://eks-v2.demo.coder.com/templates/pod-with-jupyter/workspace?mode=auto&param.Jupyter+IDE+type=lab&param.Dotfiles+URL+%28optional%29=)

* generic.ipydb are generic Pandas commands to analyze datasets. e.g., number of rows, columns, column names, distribution of values in a column, read in a csv.

* autogluon_tabular.ipynb uses an OSS autoML framework autoGluon from Amazon, to generate supervised machine learning models.  

* You need to pip3 install the packages for these to work ( or do this within an image )

* The sets folder has publicly available datasets used by the notebooks.


###### Notes / To run this app after cloning, we recommend:

* Install anaconda or a Python environment with Jupyter Notebook  https://www.anaconda.com/products/individual

* install autogluon from here: https://autogluon.mxnet.io/index.html#installation