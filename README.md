# finalCapstone 

# Project name : "inventory"<br />
# The aim of the project is to provide a shoe wholesaler service<br />
***The project:<br />
1/ The project was made using object-oriented programming (OOP) in python<br />
2/ The main file used in the project is inventory complete.py.<br />
3/ The file uses the inventory.txt - text file:<br />
  Country, Code, Product, Cost, Quantity<br />
  This information is used in projcet.<br />
4/ menu in the inventory file:<br />
<ul>
       <li>so - Read shoe data/create shoe object;</li><br />
        <li>cds - Capture data shoe;</li><br />
        <li>va - Print the detailes of the shoe;</li><br />
        <li>lst - Shoe with the lowest stocke ==> to be re-stored;</li><br />
        <li>sc - Search shoe by the code;</li><br />
        <li>tvd - Display the total value for each item;</li><br />
        <li>hq - Shoe with the highest quantity ==> it has to sel</li><br />
  </ul>
        
 <ul>Option so - Read shoe data/create shoe object - This function open the file<br />
            inventory.txt and read the data from this file, then create<br /> a
            shoes object with this data and append this object into the<br />
            shoes list.<br />
  </ul>
Option cds - Capture data shoe - This function allow a user to capture<br />
            data about a shoe and use this data to create a shoe object<br />
             and append this object inside the shoe list.<br />
Option va - Print the detailes of the shoe - This function will iterate over the shoes list and<br />
            print the details of the shoes returned from the __str__ function.<br />
Option lst - Shoe with the lowest stocke ==> to be re-stored - This function will find the shoe object with the<br />
             lowest quantity, which is the shoes that need to be re-stocked. Ask the user if they want to add this quantity of<br />
             shoes and then update it.<br />
Option  sc - Search shoe by the code - This function search for a shoe from the list<br />
              using the shoe code and return this object so that it be printed.<br />
Option  tvd - Display the total value for each item - This function will calculate the total value<br />
              for each item and print this information on the console for all the shoes:<br />
                            # value = cost * quantity<br />
Option  hq - Shoe with the highest quantity ==> it has to sel - highest_qty - This functino determine the product with <br />the
              highest quantity and print recommendations  "for sale"<br />
              
