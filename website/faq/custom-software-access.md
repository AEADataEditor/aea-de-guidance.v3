---
title: Custom software - how to provide access
tags:
  - software
  - custom code
  - experiments
  - licensing
---

## We used custom software. How do we describe/provide access to that?

This case might arise if authors ran an experiment or a novel type of survey, using software specifically created for the task. Our [policy](https://www.aeaweb.org/journals/data/data-code-policy) does require 

> "information about [...] details of the computations sufficient to permit replication," 

and requires that "programs" be archived at the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/aea). Furthermore, 

> "replication materials shall also include [...] (g) computer code for experiment or survey collection mechanisms." 

However, we do *not* require that software, as opposed to code and programs that configure and instruct the software, be uploaded. 

> - Software: a "collection of instructions and data that tell a computer how to work" [[1](https://en.wikipedia.org/wiki/Software)], here best approximated by "[application software](https://en.wikipedia.org/wiki/Application_software)", "a computer program designed to carry out a specific task other than one relating to the operation of the computer itself." Stata, Matlab, Qualtrics, zTree are software for the purpose of the policy, as are compilers such as Intel or GNU Fortran. 
> - *Code* or *programs* here refers to instructions to the application software to produce a specific output - instructions that "allow end-users – people who are not professional software developers – to program computers." [[2](https://en.wikipedia.org/wiki/End-user_development)]. Stata code, Qualtrics configuration files, and to some extent Fortran source code are typically considered to be "code."

Much of economics research is conducted using proprietary software - Stata, Matlab, etc. Our policy requires that the software be available for use by others - possibly paying a fee - and that any configuration parameters ("code") be available. For experiments, this might mean providing [zTree](https://www.ztree.uzh.ch/) code, but not the software itself (which is subject to a license agreement); for surveys, this might mean providing [Qualtrics](https://www.qualtrics.com/) configurations, but not access to a Qualtrics subscription. We do not typically require information about how to purchase or download such frequently used, named software. In most cases, the software licenses prohibit redistribution, but even in the case of open-source software (R, Julia, Python, etc.), we do not require that authors upload the executable or source code.

In other cases, the software might have been custom-designed for the purposes of the authors' research. In that case, the README should contain information on how to obtain the software. If the software is under an open source license, this might entail providing a link to a website and the software's installation and compilation instructions. If the software is not under an open source license, the README might contain language such as

> "We contracted with (DEVELOPER) to develop the software used to conduct the experiment, at a cost of approximately (rounded to next $100 or $1000). To obtain the software, (DEVELOPER) can be reached at (EMAIL) or (WEBSITE)."

If software is not open source, then two cases may occur:

- If the developer retains ownership of the software, then we are talking about a licensing agreement, much like when a researcher purchases a yearly or permanent license to Stata or Matlab. No further information is required.
- However, if the authors contracted with the developer of the software, the authors *may* also have rights to the software. 
  - If developer and authors co-own the software, the README should state what rights authors confer automatically to any replicator. For instance, if the developer needs the authors' approval to license (at some price) to any other researcher, then the README should explicitly state that the authors provide such approval. 
  - If the authors obtained full rights to the end product (a true purchase), then they should provide a mechanism to obtain the software, and state explicitly again what rights replicators have to use the software. This might include demonstration modes sufficient to conduct the replication.
