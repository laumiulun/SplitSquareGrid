# A Workflow of Nodal Attributes Generation from Petrel

## Developers

* Miu-Lun (Andy) Lau
* Yidong Xia

## Introduction
This document describes the workflow to generate a text doucment containing nodal coordinates with attributes from [Petrel](https://www.software.slb.com/products/petrel). In geothermal engineering, 


The workflow consists of three sections:

* **Section 1.** Identify Nodal boundaries from **PETREL** 
* **Section 2.** Use SplitSquareGrid script to generate a nodal file
* **Section 3.** Extract Attributes Data from **Petrel** into Nodal file

## Prerequisites
A list of software packages required for this workflow is as below:

* Python (Version 2.7.13)
* [Petrel](https://www.software.slb.com/products/petrel)

## WorkFlow
### Section 1. Identify Nodal Boundaries from PETREL

* Start **PETREL**
* Open Petrel project file **"example.ptd"**
* On Models Toolbars, hoover over to **3D grid**, rightclick and select **Settings**
* Select **Statistics** tab and record the XYZ boundaries on **AXIS** and the average Xinc,Yinc, and Zinc on **Description**

### Section 2. Use SplitSqaureGrid Python Script to generate Nodal File

* 

### Section 3. Extract Attibutes Data from PETREL into Nodal File

* Start **PETREL**
* Open Petrel Project **"example.ptd"**
* Right click on **Input Toolbar** and select **Import File**
* Navigate to the Nodal File(**"example.txt"**) you generate and import the file. 

Make sure the format is **Irap Classic Points(ASCII)** and Project(**"example.ptd"**) coordinate references system(CRS) and file(**example.txt**) crs is the same.

* Uncheck **[Neglect Z value when mostly positive]** and select **Okay**
* To check if 

