# finalCapstone 

# Project name : "inventory"
# The aim of the project is to provide a shoe wholesaler service
***The project:
1/ The project was made using object-oriented programming (OOP) in pyth;on
2/ The main file used in the project is inventory complete.py.
3/ The file uses the inventory.txt - text file:
  Country, Code, Product, Cost, Quantity
  This information is used in projcet.
4/ menu in the inventory file:
        so - Read shoe data/create shoe object;
        cds - Capture data shoe;
        va - Print the detailes of the shoe;
        lst - Shoe with the lowest stocke ==> to be re-stored;
        sc - Search shoe by the code;
        tvd - Display the total value for each item;
        hq - Shoe with the highest quantity ==> it has to sel
        
 Option so - Read shoe data/create shoe object - This function open the file
            inventory.txt and read the data from this file, then create a
            shoes object with this data and append this object into the
            shoes list.
Option cds - Capture data shoe - This function allow a user to capture
            data about a shoe and use this data to create a shoe object
             and append this object inside the shoe list.
Option va - Print the detailes of the shoe - This function will iterate over the shoes list and
            print the details of the shoes returned from the __str__ function.
Option lst - Shoe with the lowest stocke ==> to be re-stored - This function will find the shoe object with the
             lowest quantity, which is the shoes that need to be re-stocked. Ask the user if they want to add this quantity of
             shoes and then update it.
Option  sc - Search shoe by the code - This function search for a shoe from the list
              using the shoe code and return this object so that it be printed.
Option  tvd - Display the total value for each item - This function will calculate the total value
              for each item and print this information on the console for all the shoes:
                            # value = cost * quantity
Option  hq - Shoe with the highest quantity ==> it has to sel - highest_qty - This functino determine the product with the
              highest quantity and print recommendations  "for sale"
              
