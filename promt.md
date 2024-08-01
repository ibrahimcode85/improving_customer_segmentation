# Title: Customer Segmentation for Medical Supplier

## Data:

#### Doctors contains information on doctors. Each row represents one doctor.

- "DoctorID" - is a unique identifier for each doctor.
- "Region" - the current geographical region of the doctor.
- "Category" - the type of doctor, either 'Specialist' or 'General Practitioner.'
- "Rank" - is an internal ranking system. It is an ordered variable: The highest level is Ambassadors, followed by Titanium Plus, Titanium, Platinum Plus, Platinum, Gold Plus, Gold, Silver Plus, and the lowest level is Silver.
- "Incidence rate" and "R rate" - relate to the amount of re-work each doctor generates.
- "Satisfaction" - measures doctors' satisfaction with the company.
- "Experience" - relates to the doctor's experience with the company.
- "Purchases" - purchases over the last year.
- "Purchases_Category" - Group "Purchases" column into three broad category ['Low', 'Medium', 'High'].
- "Satisfaction_Category" - Group "Purchases" column into three broad category ['Low', 'Medium', 'High'].

#### Orders contains details on orders. Each row represents one order; a doctor can place multiple orders.

- "DoctorID" - doctor id (matches the other tables).
- "OrderID" - order identifier.
- "OrderNum" - order number.
- "Conditions A through J" - map the different settings of the devices in each order. Each order goes to an individual patient.

---

Data has been pre-processed and is attached here.

## Instruction 1 - base clustering

- select the following features ['Region', 'Category', 'Rank', 'Incidence rate', 'R rate', 'Satisfaction_Category', 'Experience', 'Purchases_Category'], and perform k-means clustering.
- limit the number of cluster to maximum of 3. we want to make sure there is sizeable number of data in each cluster.
- show elbow graph to determine the number of cluster to perform
- draw PCA plot to visualise the clusters.
- draw scree plot to show that visualising PCA in 2-d is sufficient.
- describe the characteristic of each cluster based on the features. recommend a good sales strategy for each cluster.
- draw a radar plot to better visualise the important features of each clusters. describe how to interpret the plot.
- group the data by cluster, and create a pivot table for each categorical column (i.e each categorical column will have one table). please decode the value before creating the table so that it is easier

## Instruction 2 - region only clustering

- select only 'Region' feature - and do k-means clustering.
- for comparison purposes do this plot: x-axis is the 'Region', y-axis is the 'Purchases', and Hue for the clusters. Do the same plot but for clustering fit that includes all features.
- The purpose is to compare previous practice of using 'Region' for grouping and strategy.
