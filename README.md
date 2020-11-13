Change Impact Analysis (CIA)
The main aim behind the impact analysis activity is to identify software artifacts (i.e., requirement, design, class and test artifacts) that are potentially to be affected by a change.

When changes in the requirements are proposed, the impact of these changes on other requirements, design elements and source code needs to be analyzed in order to determine parts of the software system to be changed. Determining the impact of changes on other development artifacts is called change impact analysis.
A trace-based approach relates requirements with other artifacts to indicate inter dependencies. These relations (traces) can be used during change impact analysis for more efficient and more correct identification of potential change locations.
There are two categories of impact analysis techniques which are static analysis technique and dynamic analysis technique. The static analysis technique develops a set of potential impacted classes by analyzing program static information that is generated from software artifacts (i.e., requirement, design, class and test artifacts). Conversely for the dynamic analysis technique, this technique develops a set of potential impacted classes by analyzing program dynamic information or executing code.
The static impact analysis will find the direct impacted classes which are the first layer of classes affected by a particular changes requirement without vertical traceability relations consideration. Then indirect impacted classes will be identified by complete traceability search through the CIP interactions to find all related classes to the changed requirement.

Techniques for CIA

    • Integration between static and dynamic analysis techniques. This integration intends to 
overcome the challenges on impact analysis implementation using static analysis and 
dynamic analysis techniques. 

    • Deep Learning based approaches to leverage trace links between different kinds of requirement artifacts.
    • Generating Rule based impact analysis techniques

    •  Integrate these models to ML approach. Existing works that base ML approaches are concerned on combining requirement artifacts with source code trace links. Thus we will involve ML models to the existing techniques with the artifacts requirements and test cases.

Possible input variables of traceability information for change impact analysis could be: volatility of requirements, total number of test cases, number of artifacts to be traced, number of requirements, trace effort per unit to trace, effort to create a new test case and so on.
The output of the change impact analysis approach in requirements models is a set of impacted requirements with proposed changes and a propagation path in the requirements model. Which is recommendation output showing ranked recommendations of specific artifacts that should be investigated further.
