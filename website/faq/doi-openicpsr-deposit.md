---
title: What is the DOI of my openICPSR deposit?
orphan: true
tags:
  - DOI
  - openICPSR
  - citation
  - deposit
---

## What is the DOI of my openICPSR deposit? I have not yet published it, but am asked to add a citation to it in my manuscript?

Generically, each openICPSR project has a number (e.g., "109622"), that might show up on the right panel:
![Image of number](/images/project-number.png) 

Then

- if the openICPSR project has not been published, then the DOI will be "http://doi.org/10.3886/E" + number + "V1" (e.g. http://doi.org/10.3886/E109622V1)
- if the openICPSR project has already been published, then the CURRENT DOI is shown on the relevant page, but if there are any revisions the Data Editor has asked for, then the to-be-cited DOI would be the next version, e.g., "http://doi.org/10.3886/E" + number + "V3" if the current version is V2 and the next version would be V3.

Give it a try:

{% include deposit-doi.html %}
