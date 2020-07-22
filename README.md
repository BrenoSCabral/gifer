# gifer

<p>Gifer is a simple script to create gifs using only the imageio library for python.</p>

<h3>Setup</h3>

<h4>Here's the documentation to install imageio https://imageio.readthedocs.io/en/stable/installation.html </h4>
<h4>And here's their website: https://imageio.github.io/</h4>

<p>Firstly, you'll need to install the imageio libary, you can do so by typing this into your terminal:</p>

```bash
  pip install imageio
```

<h3>Usage </h3>
<p> I recommend you to open save the script in the folder where the images are, then open it and check lines 18 and 19. You'll have to see if your files are jpg or png and uncomment the line of your files type and comment the other one. The default one is png</p>

<h5>Once this is done, to generate the gif:</h5>

```bash
  python gifer.py
```

<h3>Notes</h3>

- This script has been tested to create gifs from jpg and png files. It contains a function to check if the extension is .jpg or .png. Other image types require testing to assure its functionality.

- Although it works with every image, it works better if you assure that every image has the same dimensions.

<h3>Final Considerations</h3>

<h5>There are coments all over the code to make it simpler to understand, hope it's useful to you :)</h5>
