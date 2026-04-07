---
title: Replication package has more than 1,000 files
orphan: true
tags:
  - file limits
  - upload
  - ZIP
  - large deposits
---

## I am trying to upload to the repository, but my replication package has more than 1,000 files

As of 2021, the 1,000 file limit is unfortunately a hard limit. Therefore, we relax the rule that all data and code should be unzipped, though we still insist on the "smallest possible configuration".

In most cases, it is a particular directory that is the primary culprit. Say you have

`Structure-pre:`
```
/code: 20 files
/data/
   src1/: 25 files
   src2/: 101 files
   src3/: 3,000 files
```

then the ideal structure, taking into account the 1,000 file limit, would be:

`Structure-post:`
```
/code: 20 files
/data/
   src1/: 25 files
   src2/: 101 files
   src3.zip: = 1 file, containing 3,000 files
```
(src3/ and its 3,000 files have been removed!)

Your README should provide instructions to the replicators how to recover the fully unzipped structure (there are cross-platform differences in unzipping, so be precise about the final structure, rather than the method of getting there).

Alternatively, the code can handle the unzipping - optional, but more robust.

Once you've adjusted that, zip up the whole structure (so a ZIP file that has inside it another zip file, plus the `/code`, `/data/src1/`, and `/data/src2/` directories), and "Import from ZIP" when uploading to ICPSR.

For an example on how to document this in your repository, see [this file](https://doi.org/10.3886/E125381V1-101422). You can incorporate such text into a separate file, into the README (preferred), or adjust your code to take this structure into account (much preferred).
