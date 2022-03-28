

//Objective
// Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperature of the water.


// Q = waterMass ( finalTemperature – initialTemperature ) x 4184
// waterMass is water weight in kilograms
// finalTemperature and initialTemperature are temperatures in Celsius
// Q is the results in Joules










// Step 1: import Scanner library
import java.util.Scanner;

// Step 2: Initialize Class
class Main {
    public static void main(String[] args) {

// Step 3: Greet the User
        System.out.println("\n\nWelcome to the Joules Calculator! \n");

// Step 4: Set Scanner library to a variable
Scanner input = new Scanner(System.in);

// Step 5: Prompt the User to enter amount of water in kilograms(watermass)
System.out.print("\nEnter kilograms to the nearest decimal: ");
float kgFloat = input.nextFloat();
// System.out.println("\nYou've Entered: " + kgFloat);

// Step 6: Prompt the User to enter initial temp. of the water
System.out.print("\nEnter initial temperature to the nearest decimal in Celsius: ");
float initialTemperature = input.nextFloat();
// System.out.println("\nYou've Entered: " + initialTemperature);


// Step 7: Prompt the User to enter the final temp. of the water
System.out.print("\nEnter final temperature to the nearest decimal in Celsius: ");
float finalTemperature = input.nextFloat();
// System.out.println("\nYou've Entered: " + finalTemperature);


// Step 8: Calculate 
// Q = watermass(kg) ( finalTemperature - initialTemperature ) * 4184
float temperature = finalTemperature - initialTemperature;
//System.out.println("\nTemperature: " + temperature);
float total = kgFloat * temperature * 4184;
// System.out.println("\nTotal: " + total);



// Step 9: Give the output of the calculation 
System.out.print("\n---------------------------------------------------------- \n");
System.out.print("\n                      Calculations                       \n");
System.out.print("\nWatermass in kg     : " + kgFloat + " kg" + "\n");
System.out.print("Initial Temperature : " + initialTemperature + " degrees Celsius" + "\n");
System.out.print("Final Temperature   : " + finalTemperature + " degrees Celsius" + "\n");
System.out.print("\nTotal               : " + total + " Joules" + "\n");
System.out.print("\n---------------------------------------------------------- \n\n\n");


// Step 10: Close the Scanner Libaray with the input variable
input.close();
    }
}


//Step 11: Add resources used 
//Resources used: https://www.programiz.com/java-programming/operators