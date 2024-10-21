# webtlfs

## Info

In the box above you can upload your TLF structure (an `.xlsx`
specifying the structure of desidered TLF shells) and then click on
"Download TLF" to save the corresponding/produced `.docx` on your pc.

Some TLF structures for examples:
[example1](https://github.com/lbraglia/tlfs/raw/main/examples/example1.xlsx)
(simpler),
[example2](https://github.com/lbraglia/tlfs/raw/main/examples/example2.xlsx)
(from real life).

Once downloaded the `.docx`, table formatting in a unified way can be
achieved via VisualBasic macros; one tutorial is
[here](https://www.youtube.com/watch?v=kKtJx_VbLwk). Essentially:
- select `Development` tab;
- select `Macro`;
- enter a name for the formatting macro, say `format_tables` and click on `Create`
- locate `Sub format_tables()` and edit as follows
  ```basic
  Sub format_tables()
  '
  ' format_tables Macro
  '
  Dim t As Table
	  For Each t In ActiveDocument.Tables
	  t.Style = "[Custom Table Style Name]" 
  Next
  End Sub
  ```
  regarding `[Custom Table Style Name]`, look at the popup name
  visualized once you select the style of your interest and insert
  it. eg `"Tabella semplice - 1"`
- once saved, click on `Run` on `format_tables` from the Macro button
  in Development tab.



## What is this?

Basically it's [tlfs](https://pypi.org/project/tlfs/) (development
repo [here](https://github.com/lbraglia/tlfs)), but repacked as an
online streamlit service.

The live app is [here](https://webtlfs.streamlit.app); the
development repository is [here](https://github.com/lbraglia/webtlfs).
