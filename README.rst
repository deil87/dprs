Discounted Permutation Relevance Score
=========================================

This package provides methods to compute ranking quality metric called Discounted Permutation Relevance Score (DPR score)

.. image:: https://img.shields.io/pypi/v/myawesomepackage.svg
   :target: https://pypi.org/project/dprs/
   :alt: PyPI version


Installation
------------

You can install `dprs` using pip:

.. code-block:: bash

   pip install dprs

Usage
-----

Here’s a simple example:

.. code-block:: python

   from dprs import dprs

   ranking_list = range(10)
   predictad_ranked_list = random.sample(ranking_list, len(ranking_list))
   dprs(ranking_list,predictad_ranked_list)

Documentation
-------------

For full documentation, visit the `project page <https://github.com/deil87/dprs>`_.

Note this package is work in progress. See `./Learning to rank/LTR with custom loss function.ipynb` for examples of applying it as optimisation target for NeuralNetworks.

License
-------

Apache 2.0 License

----

*Copyright (c) 2025 Andrey Spiridonov*
