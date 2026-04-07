---
title: Aligning AEA RCT Registry and Data Repository
orphan: true
tags:
  - RCT
  - registry
  - DOI
  - trial data
---

## Aligning AEA RCT Registry and AEA Data and Code Repository

The [AEA RCT registry](https://www.socialscienceregistry.org) has a field that codes whether data associated with a registration is publicly available. Many authors will have this coded as "non public" prior to the publication of the replication package. When the replication package is about to be published on the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/aea), this field needs to be updated. Only the authors of the registry can update this field. Steps to follow:

- Log in to the [AEA RCT registry](https://www.socialscienceregistry.org) and select your registration
- Change the field to "public" / "published"
- [Compute the DOI](/faq/doi-openicpsr-deposit) of your forthcoming replication package publication and enter the resulting DOI in the URL field. 
  - **Do not use** the URL of the openICPSR project in the browser address bar!

[EXTRA] You should also record the RCT DOI as a related publication of your deposit on the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/aea):

- The RCT registry will show the DOI of your registration at the bottom of its public page. [Example](https://www.socialscienceregistry.org/trials/156):

![RCT DOI](/images/aearct-doi-citation.png)

- You can then enter that DOI (e.g., `10.1257/rct.156-1.1`) into the "Related Publication" field of the deposit on the AEA Data and Code Repository:

![Entering related publication](/images/project-related-icpsr.png)

- Choose the "Import via DOI" button:

![Selecting import via DOI](/images/project-related-icpsr-modal1.png)

- Fill in the DOI (e.g., `10.1257/rct.156-1.1`) and press "Import":

![Importing via DOI](/images/project-related-icpsr-modal2.png)

- Select "`is supplemented by`" and press "Save and Apply"

![Selecting relationship](/images/project-related-icpsr-modal3.png)
