# image2ascii

## Installing

```
git clone https://github.com/Frezzle/image2ascii
cd image2ascii
pip install .
```

## Usage

In Python 3.x or 2.7.x:

```
import image2ascii
image2ascii.convert('/path/to/image')
```

## Customize output

Reduce/increase `x_step` and `y_step` for more/less detail in the ASCII output:

```
image2ascii.convert('/path/to/image', x_step=5, y_step=10)
```

Colours can be inverted:

```
image2ascii.convert('/path/to/image', invert_colours=True)
```

## Attribution

[Default penguin image](https://pixabay.com/en/tux-penguin-animal-cute-linux-158547)

[ASCII character set inspiration](https://manytools.org/hacker-tools/convert-images-to-ascii-art)
