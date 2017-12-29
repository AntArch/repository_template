

# Land Registration in Scotland workshop


This is a workshop about Land Registration. It is specifically about Land Registration in Scotland. Scotland has a long history of Land Registration. 

## The General Register of Sasines - 1617

[The General Register of Sasines](https://www.ros.gov.uk/services/registration/sasine-register) - also known as the sasine register - is the oldest national land register in the world, dating back to 1617. Its name comes from the old French word 'seizer', which means 'take'.

The sasine register is a chronological list of land deeds, which contain **written descriptions** of properties. It is gradually being replaced by the **map-based** land register.

## The Land Register of Scotland - 1979 (became law in 1981) to 2014

The [land register](https://www.ros.gov.uk/services/registration/land-register) is the primary register managed by [Registers of Scotland](https://www.ros.gov.uk/). Introduced in 1981, it's a register of who owns land and property in Scotland.

The land register (1979) was based on the Ordnance Survey map, and includes plans of registered land. Every plot of land on the register has a title sheet, which is guaranteed by the state. The title sheet defines the extent of the plot of land on a map and gives details of:

* current owners
* price
* mortgage details
* conditions affecting the property

## The Land Register of Scotland - 2012 (became law in 2014) to present

The [Land Registration etc (Scotland) Act 2012](http://www.legislation.gov.uk/asp/2012/5/introduction/enacted) came into force on 8 December 2014. The 2012 Act followed on from, and developed, the recommendations made by the Scottish Law Commission in their [report on land registration published in February 2010](http://www.scotlawcom.gov.uk/files/1112/7979/8376/rep222v1.pdf) (Reig and Gretton, who chaired this report, also published the book '[Land Registration](http://www.avizandum.co.uk/content/land-registration)' (there is a digital copy in the RoS library)). The 2012 Act put in place a new scheme of land registration. The main purpose of the act was to reform and restate the law on the registration of rights to land in the Land Register of Scotland. The act achieved this by repealing much of the current land registration statute: the Land Registration (Scotland) Act 1979, and the Land Registration (Scotland) Rules 2006 made under that act.

The 2012 Act realigned the law of land registration with property law. It also put on a statutory footing many of the policies and practices the keeper had developed since the introduction of the Land Register in 1981. The 2012 Act introduced new concepts, such as advance notices, and new rules that govern how the keeper registers deeds and makes up the register.

The changes introduced by the 2012 act are profound and have an impact on the two principal back end data systems:

* [Digital Mapping System](http://netconfluence1.core.rosdev.org.uk/display/AR/DMS+-+Digital+Mapping+System)
    * The requirement to demonstrate no overlapping *ownership in land* means that DMS is no longer *fit for purpose*
* [Land Registration System](http://netconfluence1.core.rosdev.org.uk/display/AR/LRS+-+Land+Registration+System)
    * Manages and represents 'legal settle'
    * It has been called a **string factory** in that is does not store data directly, but structures information using syntax and grammar rules so that sentences and paragraphs can be generated.
    * The **string factory** approach makes data extraction complex and means that it is difficult to either:
        * productise the land register
        * provide intelligence to support policy, business or operational decision. 




# The 'new model'

The new model will reflect changes to the Land Register demanded by the [Land Registration etc. (Scotland) Act 2012](http://www.legislation.gov.uk/asp/2012/5/introduction/enacted). 

RoS has the the following responsibilities

* From an ongoing basis RoS has to legally operate within the limits defined by the 2012 Act (LR_Act_2012: Land Registration etc. (Scotland) Act 2012) 
* The act has no mandated retrospective impact on records currently in the system - the new 'to be' system must be able to function with 'to be' and 'as is' records. 
    * However, Schedule 4 gives the Keeper powers to update records.

The goal is to develop the physical model of the Land Register that reflects these responsibilities. The aspiration is to align this model, wherever possible, to the [Land Administration Domain Model standard as described in ISO 19152](https://www.iso.org/standard/51206.html). [Land Registration](http://www.avizandum.co.uk/content/land-registration) (Reid and Gretton, 2017) provides useful supporting context that explains some of the reasoning behind the legislation. There is also significant content in the currently materialised LRS and DMS data models. 

The problem the modelling faces is the following:

* Ensuring legal compliance,
* while simplifying for the future,
* without losing legacy functions and
* aligning to standards


![The process of Land Registration](../notebooks/figures/example.png)

This workshop helps describe this journey.


# Who Is This Workshop For?

Add some text here

# Outline of the Workshop

Each section of this workshop ......

# Using Code Examples

This presentation is interactive. The expectation is that you will run the code associated with the notebooks. 

## Installation Considerations

Installing Python and the suite of libraries that enable scientific computing is straightforward . This section will outline some of the considerations when setting up your computer.

Though there are various ways to install Python, the one I would suggest for use in data science is the Anaconda distribution, which works similarly whether you use Windows, Linux, or Mac OS X.
The Anaconda distribution comes in two flavors:

- [Miniconda](http://conda.pydata.org/miniconda.html) gives you the Python interpreter itself, along with a command-line tool called ``conda`` which operates as a cross-platform package manager geared toward Python packages, similar in spirit to the apt or yum tools that Linux users might be familiar with.

- [Anaconda](https://www.continuum.io/downloads) includes both Python and conda, and additionally bundles a suite of other pre-installed packages geared toward scientific computing. Because of the size of this bundle, expect the installation to consume several gigabytes of disk space.

Any of the packages included with Anaconda can also be installed manually on top of Miniconda; for this reason I suggest starting with Miniconda.

To get started, download and install the Miniconda package–make sure to choose a version with Python 3–and then install the core packages used in this book:

```
[~]$ conda install numpy pandas scikit-learn matplotlib seaborn jupyter
```

Throughout the text, we will also make use of other more specialized tools in Python's scientific ecosystem; installation is usually as easy as typing **``conda install packagename``**.
For more information on conda, including information about creating and using conda environments (which I would *highly* recommend), refer to [conda's online documentation](http://conda.pydata.org/docs/).



