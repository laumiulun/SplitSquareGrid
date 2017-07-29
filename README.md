# A Workflow of Nodal Attributes Generation from Petrel

## Developers

* Miu-Lun (Andy) Lau
* Yidong Xia

## Introduction
This document describes the workflow to generate a text doucment containing nodal coordinates with attributes from [Petrel](https://www.software.slb.com/products/petrel).

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
* On Models Toolbars and expand your desire models.
* Scroll down to **3D grid**, rightclick and select **Settings**

![Console](./contents/boundary1.png)

* Navigate to **Statistics** tab and record the XYZ boundaries on **AXIS** and the average Xinc,Yinc, and Zinc on **Description**

![Console](./contents/Statistics.png)

### Section 2. Use SplitSqaureGrid Python Script to generate Nodal File

* With nodal boundaries known, navigate to **../SplitSquareGrid** and enter the command:

```
./run_test
```
* Enter the limits of each axis, and the number of cells in each direction.
* A text document named **example.txt** that contain all nodes is generated in the same directory. 



### Section 3. Extract Attibutes Data from PETREL into Nodal File

* Start **PETREL**
* Open Petrel Project **"example.ptd"**
* Right click on blink space inside **Input Toolbar** and select **Import File**
* Navigate to the Nodal File(**"example.txt"**) select **Open**

Make sure the format is **Irap Classic Points(ASCII)**

* A window call **Input Data** will show up, make sure the Project(**"example.ptd"**) coordinates references system(CRS) and file(**"example.txt"**) is the same.
* Uncheck **[Neglect Z value when mostly positive]** and select **OK**

__________________________________
* To check if the Nodal File completely encapsulate the Petrel Project file
	* 	In Model Toolbar, check **[Top]**, **[Horizon]** and **[Bottom]**
	
_____________________________________

* In Input Toolbar,
	* Right click on **example.txt**
	* Select **Insert new attributes** and choose **Continous**
* In the operations tabs,
	* Expand **"expand values from property"** and choose **"Assign values from properties"**
	* On the right space, expand the Models and select the properites
	* Select one or more attributes in the models toolbar
	* Select right arrows to import attibutes and choose **Run** to apply
	* Repeat for additional properties.
* Right click on the Grid file (**example.txt**),
	* Select **Export Object**
	* Choose **Petrel Points with Attributes**

Again, check to make sure both files have the same CRS
