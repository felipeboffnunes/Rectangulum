<h2>How to add a new template</h2>

<h3>Steps</h3>
<ol>
<li>Choose a template at Overleaf</li>
<li>Create a full boxed pdf</li>
<li>Create blank styles</li>
<li>Separate categories from .cls</li>
<li>Create Python class for template</li>
</ol>

<h3>1. Choose a template at Overleaf</h3>
<p>Choose a template from Overleaf and check if it is already in the available templates at the documentation. 
Create it using the "Open as Template" and share it with pyrrhicbuddha@gmail.com. 
</p>

<h3>2. Create a full boxed pdf</h2>
<p>There are several packages from latex to create boxes. Some of them come with latex and some need to be uploaded to the Template.
If you are at the .tex file, to add a package you write <strong>\usepackage{name_of_package}</strong> after the \documentclass line. If you are 
at the .cls file you need to write <strong>\RequirePackage{name_of_package}</strong>, write it along with the others \RequirePackage that are already
in the beginning of the file.</p>
<p>Here are some of the packages I am using, there are probably more and when we find them they will probably help us to have more 
flexibility.</p>
<ul>
<li>\fbox - Used for one line text boxes</li>
<li>\begin{framed} - Used for paragraphs, images, tables, etc</li>
<li>\begin{mdframed} - Same as framed</li>
</ul>
<p>To create a full boxed pdf you need to wrap the content with those packages. You start first trying to put a box around the content <strong>directly
from the .tex file</strong>, if the box does not work, it means you have to go to the .cls file, find where that type of content is instantiated,
understand the logic the .cls is doing with the data of the content and find the place where you can wrap the content with the box.</p>
<h4>An example</h4>
<p>We will now try to add a box around the title. First we try to put a \fbox around the title in the .tex file</p>

```
\title{The Name of the Title is Hope}
```

<p>becomes</p>

```
\fbox{
\title{The Name of the Title is Hope}
}
```

<p>In this example, let's say it didn't work, it <strong>may be because we are using the wrong box package</strong>
(try using framed or mdframed then!). But on this example it's actually necessary to edit the .cls file.</p>
<p>To do this we must remember we are talking about the \title. We go to the .cls file and use ctrl + F and search for title.
On ACM Journal template, when you search title on .cls it gets 105 results. If we search better, we can find less results,
on this example the way to get few examples is searching \@title (as full word result), it gets 6 results. We have to go one 
by one and see if that is the one we are looking for. Of course (!), if the title is in the middle of a whole word like 
pdfdisplaydoc<strong>title</strong>, then you can rapidly discard it from the possibilities. We are looking for something like this:</p>

```
\def\@mktitle{%
  \ifcase\ACM@format@nr
  \relax % manuscript
    \@mktitle@i
  \or % acmsmall
    \@mktitle@i
  \or % acmlarge
    \@mktitle@i
  \or % acmtog
    \@mktitle@i
  \or % sigconf
    \@mktitle@iii
  \or % siggraph
    \@mktitle@iii
  \or % sigplan
    \@mktitle@iii
  \or % sigchi
    \@mktitle@iii
  \or % sigchi-a
    \@mktitle@iv
  \fi
}
```

<p>This is the mktitle. As it shows it just decides which version of mktitle it will use (i, iii or iv), dependending on the
template style (acmsmall, acmlarge, sigplan...). <strong>This is important!</strong> It means that there are three different ways
of instantiating the title in the document, depending on the template style used. Since we will be using all styles and parameters
available on each template, it means <strong>we have to edit each mktitle version</strong>.</p>
<p>This is the mktitle@iii:</p>

```
\def\@mktitle@iii{\hsize=\textwidth
    \setbox\mktitle@bx=\vbox{\@titlefont\centering
      \@ACM@title@width=\hsize
      \if@ACM@badge
        \advance\@ACM@title@width by -2\@ACM@badge@width
        \advance\@ACM@title@width by -2\@ACM@badge@skip
        \parbox[b]{\@ACM@badge@width}{\strut
          \ifx\@acmBadgeL@image\@empty\else
            \raisebox{-.5\baselineskip}[\z@][\z@]{\href{\@acmBadgeL@url}{%
                \includegraphics[width=\@ACM@badge@width]{\@acmBadgeL@image}}}%
          \fi}%
        \hskip\@ACM@badge@skip
      \fi
      \parbox[t]{\@ACM@title@width}{\centering\@titlefont
        \@title
        \ifx\@subtitle\@empty\else
          \par\noindent{\@subtitlefont\@subtitle}
        \fi
      }%
      \if@ACM@badge
        \hskip\@ACM@badge@skip
        \parbox[b]{\@ACM@badge@width}{\strut
          \ifx\@acmBadgeR@image\@empty\else
            \raisebox{-.5\baselineskip}[\z@][\z@]{\href{\@acmBadgeR@url}{%
                \includegraphics[width=\@ACM@badge@width]{\@acmBadgeR@image}}}%
          \fi}%
      \fi
      \par\bigskip}}%
```

<p>We can see that the title is intantiated as \@title right after  \parbox[t]{\@ACM@title@width}{\centering\@titlefont. As we are
talking about a line of text, it can be intuitive to put a \fbox around it. But we must think more! Maybe the title is long 
enough to actually become two lines, we need to use framed or mdframed then.</p>
<p>This is how mktitle@iii (zoomed a little bit) needs to be edited:</p>

```
\parbox[t]{\@ACM@title@width}{\centering\@titlefont
        \begin{framed}
        \@title
        \end{framed}
        \ifx\@subtitle\@empty\else
          \par\noindent{\@subtitlefont\@subtitle}
        \fi
      }%
```





