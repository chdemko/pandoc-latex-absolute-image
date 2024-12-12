Usage
=====

To apply the filter, use the following option with pandoc:

.. code-block:: shell-session

    $ pandoc --filter pandoc-latex-absolute-image

Explanation
-----------

In the metadata block, specific set of classes can be defined to
position an image relatively to each page:

It’s also possible to specify a new image using description by attributes.

The metadata block add information using the ``pandoc-latex-absolute-image``
entry by a list of definitions:

.. code-block:: yaml

   pandoc-latex-absolute-image:
     - classes: [left]
       image: Tux.pdf
       x-coord: 1cm
       y-coord: 1cm
       width: 32pt

The metadata block above is used to position *Tux* on all pages
**1cm** from the left edge and **1cm** from the top edge.

Each entry of ``pandoc-latex-absolute-image`` is a YAML dictionary containing:

-  ``classes``: the set of classes that triggers the position of the image.
   This parameter is mandatory.
- ``image``: the image path
- ``image-odd``: the image path for odd page (default to ``image``),
- ``image-even``: the image path for even page (default to ``image``),
- ``reset``: to remove the image on all subsequent pages
- ``reset-odd``: to remove the image on all subsequent odd pages
  (default to ``reset``)
- ``reset-even``: to remove the image on all subsequent even pages
  (default to ``reset``)
- ``width``: the width of the rendered image
- ``width-odd``: the width of the rendered image for odd pages
  (default to ``width``)
- ``width-even``: the width of the rendered image for odd pages
  (default to ``width``)
- ``height``: the height of the rendered image
- ``height-odd``: the height of the rendered image for odd pages
  (default to ``height``)
- ``height-even``: the height of the rendered image for odd pages
  (default to ``height``)
- ``anchor``: the image anchor
- ``anchor-odd``: the image anchor for odd pages
- ``anchor-even``: the image anchor for even pages
- ``x-coord``:  the x-coordinate
- ``x-coord-odd``: the x-coordinate for odd pages
- ``x-coord-even``: the x-coordinate for even pages
- ``y-coord``:  the y-coordinate
- ``y-coord-odd``: the y-coordinate for odd pages
- ``y-coord-even``: the y-coordinate for even pages
- ``opacity``:  the image opacity
- ``opacity-odd``: the image opacity for odd pages
- ``opacity-even``: the image opacity for even pages

It’s also possible to specify the image using
attribute description:

- ``latex-absolute-image``
- ``latex-absolute-image-odd``
- ``latex-absolute-image-even``
- ``latex-absolute-reset``
- ``latex-absolute-reset-odd``
- ``latex-absolute-reset-even``
- ``latex-absolute-width``
- ``latex-absolute-width-odd``
- ``latex-absolute-width-even``
- ``latex-absolute-height``
- ``latex-absolute-height-odd``
- ``latex-absolute-height-even``
- ``latex-absolute-anchor``
- ``latex-absolute-anchor-odd``
- ``latex-absolute-anchor-even``
- ``latex-absolute-x-coord``
- ``latex-absolute-x-coord-odd``
- ``latex-absolute-x-coord-even``
- ``latex-absolute-y-coord``
- ``latex-absolute-y-coord-odd``
- ``latex-absolute-y-coord-even``
- ``latex-absolute-opacity``
- ``latex-absolute-opacity-odd``
- ``latex-absolute-opacity-even``

The following LaTeX packages are required:

-  ``tikz``

Example
-------

Demonstration: Using
`pandoc-latex-absolute-image-sample.txt <https://raw.githubusercontent.com/chdemko/pandoc-latex-absolute-image/develop/docs/images/pandoc-latex-absolute-image-sample.txt>`__
as input gives output file in
`pdf <https://raw.githubusercontent.com/chdemko/pandoc-latex-absolute-image/develop/docs/images/pandoc-latex-absolute-image-sample.pdf>`__.

.. code-block:: shell-session

    $ pandoc --filter pandoc-latex-absolute-image pandoc-latex-absolute-image-sample.txt \
        -o pandoc-latex-absolute-image-sample.pdf

The `Tux` image is made available under the `Creative Commons CC0 1.0 Universal
Public Domain Dedication <https://creativecommons.org/publicdomain/zero/1.0/deed.en>`__
(https://commons.wikimedia.org/wiki/File:Tux.svg).
