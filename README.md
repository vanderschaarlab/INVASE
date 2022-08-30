# INVASE: Instance-wise Variable Selection

[![Tests](https://github.com/vanderschaarlab/INVASE/actions/workflows/test.yml/badge.svg)](https://github.com/vanderschaarlab/INVASE/actions/workflows/test.yml)
[![Downloads](https://img.shields.io/pypi/dd/invase)](https://pypi.org/project/invase/)
[![arXiv](https://img.shields.io/badge/arXiv-2206.07769-b31b1b.svg)](https://openreview.net/pdf?id=BJg_roAcK7)
[![Test In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11PZ6gk46lprhoDR30ZCpdLVB7WNn3pFj?usp=sharing)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


![image](https://github.com/vanderschaarlab/invase/raw/main/docs/arch.png "INVASE")

Authors: Jinsung Yoon, James Jordon, Mihaela van der Schaar

Paper: Jinsung Yoon, James Jordon, Mihaela van der Schaar, "IINVASE: Instance-wise Variable Selection using Neural Networks," International Conference on Learning Representations (ICLR), 2019. (https://openreview.net/forum?id=BJg_roAcK7)

## :rocket: Installation

The library can be installed from PyPI using
```bash
$ pip install invase
```
or from source, using
```bash
$ pip install .
```
## :boom: Sample Usage
```python
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from invase import INVASE

X, y = load_iris(return_X_y=True, as_frame = True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

## Load the model
model = LogisticRegression()

model.fit(X_train, y_train)

## Load INVASE
explainer = INVASE(
    model, 
    X_train, 
    y_train, 
    n_epoch=1000, 
    prefit = True, # the model is already trained
)

## Explain
explainer.explain(X_test.head(5))
```


## :hammer: Tests

Install the testing dependencies using
```bash
pip install .[testing]
```
The tests can be executed using
```bash
pytest -vsx
```

## Citing
If you use this code, please cite the associated paper:
```
@inproceedings{
    yoon2018invase,
    title={{INVASE}: Instance-wise Variable Selection using Neural Networks},
    author={Jinsung Yoon and James Jordon and Mihaela van der Schaar},
    booktitle={International Conference on Learning Representations},
    year={2019},
    url={https://openreview.net/forum?id=BJg_roAcK7},
}
```
