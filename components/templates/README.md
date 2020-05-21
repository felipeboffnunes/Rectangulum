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
<li>\frame - Used for everything, has no padding, but I don't know if it can be edited (so no blank style...)</li>
 <li>\framebox - Same as frame but with some extra difficulties.</li>
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

<h4>An advanced example</h4>

<p>Now we will try to put a box around the authors. We will skip the part where we try to put a box on .tex since by now we already know
  it won't work (it is definitely formatted by the .cls file). Well, let's search for \@author and see what we get. 27 results...
  Good, now we go one by one searching for a \def that creates the author in the first page of the pdf.</p>
<p> We found \def\@author##1{% while searching, this names looks like what we are searching, and it is inside \def\@mkauthors@i{%... bingo! It means @mkauthors is the function that creates the author, and that it also has different versions.</p>
<p>This is @mkauthors:</p>

```
\def\@mkauthors{\begingroup
  \hsize=\textwidth
  \ifcase\ACM@format@nr
  \relax % manuscript
    \@mkauthors@i
  \or % acmsmall
    \@mkauthors@i
  \or % acmlarge
    \@mkauthors@i
  \or % acmtog
    \@mkauthors@i
  \or % sigconf
    \@mkauthors@iii
  \or % siggraph
    \@mkauthors@iii
  \or % sigplan
    \@mkauthors@iii
  \or % sigchi
    \@mkauthors@iii
  \or % sigchi-a
    \@mkauthors@iv
  \fi
  \endgroup
}
```

<p>As the first example, it has three versions (i, iii, iv), we have to edit each one of them. Let's see how @mkauthors@iii is:</p>

```
\def\@mkauthors@iii{%
  \author@bx@wd=\textwidth\relax
  \advance\author@bx@wd by -\author@bx@sep\relax
  \ifnum\@ACM@authorsperrow>0\relax
    \divide\author@bx@wd by \@ACM@authorsperrow\relax
  \else
    \ifcase\num@authorgroups
    \relax % 0?
    \or  % 1=one author per row
    \or  % 2=two authors per row
       \divide\author@bx@wd by \num@authorgroups\relax
    \or  % 3=three authors per row
       \divide\author@bx@wd by \num@authorgroups\relax
    \or  % 4=two authors per row (!)
       \divide\author@bx@wd by 2\relax
    \else % three authors per row
       \divide\author@bx@wd by 3\relax
    \fi
  \fi
  \advance\author@bx@wd by -\author@bx@sep\relax
  \gdef\@currentauthors{}%
  \gdef\@currentaffiliation{}%
  \def\@author##1{\ifx\@currentauthors\@empty
    \gdef\@currentauthors{\par##1}%
  \else
    \g@addto@macro\@currentauthors{\par##1}%
  \fi
  \gdef\and{}}%
  \def\email##1##2{\ifx\@currentaffiliation\@empty
    \gdef\@currentaffiliation{\bgroup
      \mathchardef\UrlBreakPenalty=10000\nolinkurl{##2}\egroup}%
  \else
    \g@addto@macro\@currentaffiliation{\par\bgroup
      \mathchardef\UrlBreakPenalty=10000\nolinkurl{##2}\egroup}%
  \fi}%
  \def\affiliation##1##2{\ifx\@currentaffiliation\@empty
    \gdef\@currentaffiliation{%
      \setkeys{@ACM@affiliation@}{obeypunctuation=false}%
      \setkeys{@ACM@affiliation@}{##1}##2}%
  \else
    \g@addto@macro\@currentaffiliation{\par
      \setkeys{@ACM@affiliation@}{obeypunctuation=false}%
      \setkeys{@ACM@affiliation@}{##1}##2}%
  \fi
  \global\let\and\@typeset@author@bx
}%
  \hsize=\textwidth
  \global\setbox\mktitle@bx=\vbox{\noindent
    \box\mktitle@bx\par\medskip\leavevmode
    \lineskip=1pc\relax\centering\hspace*{-1em}%
    \addresses\let\and\@typeset@author@bx\and\par\bigskip}}
```

<p>Pretty big and full of stuff, oof. But it is where the authors are, so we need to find where to put the box. The answer is this: the authors are in the last line, they are the \addresses and the last author is the last \par on the last line. Why is the last author separated from the others? No clue.</p>
<p>Now we need to find where addresses gets the authors, let's go straight ahead to it.</p>

```
 \ifx\addresses\@empty
    \if@ACM@anonymous
      \gdef\addresses{\@author{Anonymous Author(s)%
        \ifx\@acmSubmissionID\@empty\else\\Submission Id:
          \@acmSubmissionID\fi}}%
      \gdef\authors{Anonymous Author(s)}%
    \else
      \gdef\addresses{\@author{#2}}%
      \gdef\authors{#2}%
    \fi
  \else
    \if@ACM@anonymous\else
      \g@addto@macro\addresses{\and\@author{frame{#2}}%
      \g@addto@macro\authors{\and#2}%
    \fi
  \fi
```
<p>There are two places where this is getting authors, on \gdef\addresses{\@author{#2}}% and \g@addto@macro\addresses{\and\@author{frame{#2}}%, this is because the authors of the first one come with information taken from another author, so they are dealt differently. There are two different approaches now:</p>
<ul>
  <li>Use the package frame for all the authors information, but we will mess with the layout a little bit(as is the case for my attempt) and use it.</li>
  <li>Use the package frame to only extract the name of the authors, withouth their affiliations, emails, etc.</li>
</ul>
<p><strong>Using frame for all info</strong></p>

```
\if@ACM@anonymous\else
      \g@addto@macro\addresses{
      \frame{\and\@author{#2}}
      }%
      \g@addto@macro\authors{\and#2}%
    \fi
```

<p><strong>Using frame for only names</strong></p>

```
\ifx\addresses\@empty
    \if@ACM@anonymous
      \gdef\addresses{\@author{Anonymous Author(s)%
        \ifx\@acmSubmissionID\@empty\else\\Submission Id:
          \@acmSubmissionID\fi}}%
      \gdef\authors{Anonymous Author(s)}%
    \else
      \gdef\addresses{\@author{\frame{#2}}}%
      \gdef\authors{#2}%
    \fi
  \else
    \if@ACM@anonymous\else
      \g@addto@macro\addresses{
      \and\@author{\frame{#2}}
      }%
      \g@addto@macro\authors{\and#2}%
    \fi
  \fi
```

<p>If we are using the frame for all info, we also need to edit the last author back in the @mkauthors@iii def, otherwise the approach with only names already gets all authors.</p>

```
\lineskip=1pc\relax\centering\hspace*{-1em}%
  \addresses\let\and\@typeset@author@bx
    \frame{\and\par\bigskip}}}
```

<p><strong>Which approach to choose?</strong></p>
<p>We want the most of the information to be inside boxes, so we should try as much as possible to be able to put a box around all the info from the authors. But, we also don't want to mess with the layout too much! The best option for this case is actually to only get the names, not only because it doesn't mess with the layout, but because the authors that use information from other authors appear together, so the number of boxes would be less than the amount of authors, a huge problem if we need to custom code the system for each class.</p>

