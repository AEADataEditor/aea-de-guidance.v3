---
title: What is the __MACOSX folder?
orphan: true
tags:
  - Mac
  - ZIP
  - upload
  - troubleshooting
---

## What is that __MACOSX folder, which seems to contain a second copy of all the replication files?

I am not sure why this folder exists.

[MAC USERs ONLY] We are also not sure, but it is a standard feature of ZIP files created on Mac OSX systems using the graphical user interface. Here's a quick fix that helps all parties involved (adapted from this [source](https://wpguru.co.uk/2013/10/how-to-remove-__macosx-from-zip-archives/)):

1. Create your ZIP file as usual
2. Open the Terminal App
3. Start typing `zip -d ` (note space)
4. Drag the ZIP file onto the Terminal
5. Complete the command line with ` "__MACOSX*"` and hit enter.

The whole thing should look like this:
```
$ zip -d /Users/myname/Workspace/Folder/myzip.zip "__MACOSX*"
deleting: __MACOSX/
deleting: __MACOSX/myzip/
deleting: __MACOSX/myzip/._Proof_hi.pdf
deleting: __MACOSX/myzip/._README.pdf
deleting: __MACOSX/._myzip
```
You can now upload the file to openICPSR using the "Import from ZIP" functionality.

We should note that these folders do not show up in the public view of the repository once it is published. So while it is probably OK to leave them, it is better to remove them.
