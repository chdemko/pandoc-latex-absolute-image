from unittest import TestCase

from panflute import convert_text

import pandoc_latex_absolute_image


class AbsoluteImageTest(TestCase):
    def verify_conversion(
        self,
        text,
        expected,
        transform,
        input_format="markdown",
        output_format="latex",
        standalone=False,  # noqa: FBT002
    ) -> None:
        """
        Verify the conversion.

        Parameters
        ----------
        text
            input text
        expected
            expected text
        transform
            filter function
        input_format
            input format
        output_format
            output format
        standalone
            is the output format standalone ?
        """
        doc = convert_text(text, input_format=input_format, standalone=True)
        doc.format = output_format
        doc = transform(doc)
        converted = convert_text(
            doc.content,
            input_format="panflute",
            output_format=output_format,
            extra_args=["--wrap=none"],
            standalone=standalone,
        )
        print("-----------------------------------")
        print(converted)
        print()
        print(expected)
        self.assertEqual(converted.strip(), expected.strip())  # noqa: PT009

    def test_image(self):
        self.verify_conversion(
            """
---
pandoc-latex-absolute-image:
  - classes: [left]
    image: Tux.pdf
    x-coord: 1cm
    y-coord: 1cm
    width: 1cm
  - classes: [reset]
    reset: true
---

::: left
Image at left position
:::

\\newpage

::: reset
No image
:::
            """,
            """
\\renewcommand\\PandocLaTeXAbsoluteImage{%
\\ifodd\\value{page}%
\\begin{tikzpicture}[
    overlay,                         % Do our drawing on an overlay instead of inline
    remember picture,                % Allow us to share coordinates with other drawings
    shift=(current page.north west), % Set the top (north) left (west) as the origin
    yscale=-1,                       % Switch the y-axis to increase down the page
    inner sep=0,                     % Remove inner separator
]
\\node[] at (1cm, 1cm)
    {\\includegraphics[width=1cm]{Tux.pdf}};
\\end{tikzpicture}
\\else
\\begin{tikzpicture}[
    overlay,                         % Do our drawing on an overlay instead of inline
    remember picture,                % Allow us to share coordinates with other drawings
    shift=(current page.north west), % Set the top (north) left (west) as the origin
    yscale=-1,                       % Switch the y-axis to increase down the page
    inner sep=0,                     % Remove inner separator
]
\\node[] at (1cm, 1cm)
  {\\includegraphics[width=1cm]{Tux.pdf}};
\\end{tikzpicture}
\\fi
}

Image at left position

\\newpage

\\renewcommand\\PandocLaTeXAbsoluteImage{%
\\ifodd\\value{page}%

\\else

\\fi
}

No image
            """,
            pandoc_latex_absolute_image.main,
        )
