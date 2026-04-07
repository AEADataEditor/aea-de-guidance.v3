---
title: How to update a published repository
orphan: true
tags:
  - openICPSR
  - revision
  - update
  - versioning
  - published
---

## I was wondering whether (and how) I can update the published repository for our paper

I was contacted by a researcher who is doing a replication ... couple of minor issues ... forgotten to include two auxiliary datasets in the repository without which one of the programs does not run successfully.

First off, excellent initiative. Our team cannot always conduct a full replication (not all data may be accessible, not enough time, no access to the software). We appreciate it when others are able to do that work, and when authors then correct the replication package.

Updating the repository is actually very easy, and updates likes these are exactly why we moved to the openICPSR repository for this. We have a policy how changes are then recorded, see [https://www.aeaweb.org/journals/data/policy-revisions](https://www.aeaweb.org/journals/data/policy-revisions).

1) Log back onto your openICPSR deposit. If you don't remember, simply click on the "Share Data" link on openICPSR, and it will show you your deposits.

2) You will need to click on "Create new version" if you created the deposit after after July 2020).

![Create a new version on openICPSR](/images/icpsr-create-new-version.png)

3) Update the README as [per the policy](https://www.aeaweb.org/journals/data/policy-revisions). The updated README should have a section called "Changes" (or a separate file called "CHANGES.txt"). Authors should list the files added, any changes made to the programs, and ideally the reason why. No more than a paragraph per version, e.g.,

> The data and code in this deposit have been updated after publication of the article.
>- V1: Original version
>- V2: The code has been simplified, and better instructions provided. All results are the same.
>- V3: Permission was obtained by the data provider to post additional data. "Master.do" and the instructions in the README have been updated. Figures 5, 8, and 10 are now reproducible with this archive. 

4) Once you updated all files (remember to update the README), choose "Submit to AEA" in "Change Status". Please *also* notify the Data Editor by email, separately.

![Submit to AEA](/images/change-status-button.png)

5) The AEA Data Editor will review that the criteria of the [Revision Policy](https://www.aeaweb.org/journals/data/policy-revisions) are satisfied, but conduct no other checks.

6) In most cases, the article will remain linked to the V1 deposit ("version of record"), but anybody navigating there will see a banner indicating that a more recent version exists (the V2 deposit).

![Banner for V2](/images/icpsr-version2-banner.png)
