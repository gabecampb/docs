## docs
---
This is my simple static site generator, written in Python using the
[`markdown`](https://github.com/Python-Markdown/markdown) module.

You can use the command `python webgen.py [.md file]` to generate an HTML file.
The root directory for markdown files is `docs`.

The output of the `webgen.py` script will go to the `pages` directory, which is
intended to be the root directory of a web server.

To test the generator, run: `python webgen.py ../README.md` and then open
`pages/index.html` to see what this README would look like.

### Styling

`template.html` is the template used for generated pages. In this file,
`PAGE_CONTENT` is the location where the generated HTML markdown content will
be inserted. Note that this template configures level-three headings to be
horizontally centered, because I like to use them as centered section titles,
however the template can easily be configured by changing the CSS.
